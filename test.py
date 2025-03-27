print(""" 
                           ___________
                          |__       __|      ______                __________________________________________ 
                             |     |        |______|              [_   _____    ______________        _______]
                             |     |          |  |                  | |     |  |              |      |  ___|
                 ____________|     |__________|__|__________________| |     |  |______________|      | |___|
                (__________________________________________________/  |_____|                        |_____|____________
                 (                   ______       ___       _____     _     ___    __    ___   ___    __    __        __]
                 |                  |      |     / _ \     |_   _|   | |    \  \  /  \  /  /  / _ \   \ \  / /       |
                 |                  |    __|    / /_\ \      | |     | |     \  \/    \/  /  / /_\ \   \ \/ /        |
                 |                  | |\ \     / _____ \    _| |_    | |__    \    /\    /  / _____ \   |  |         |___ 
                 |__________________|_|_\_\   /_/     \_\  |_____|   |____|    \__/  \__/  /_/     \_\  |__|             | 
                /=========================\______________________________________________________________________________|
               /__________________________________________________________________________________________________________]
_______________((  (#)  ))===((  (#)  ))===((  (#)  ))===((  (#)  ))===((  (#)  ))===((  (#)  ))===((  (#)  ))===((  (#)  ))____________________""")


# Function to initialize the seats
def initialize_seats(total_seats):
    # Create a list with None values representing available seats
    seats = [None] * total_seats
    return seats


# Function to view all available seats
def view_available_seats(seats):
    print("Available Seats:")
    available_seats = [i + 1 for i, seat in enumerate(seats) if seat is None]
    if available_seats:
        for seat in available_seats:
            print(seat, end=' ')
        print()  # Print a newline
    else:
        print("No seats available")


# Function to book a seat
def book_seat(seats, seat_number, passenger_name):
    if 1 <= seat_number <= len(seats):
        if seats[seat_number - 1] is None:
            seats[seat_number - 1] = passenger_name
            print(f"Seat {seat_number} successfully booked for {passenger_name}.")
        else:
            print(f"Seat {seat_number} is already booked.")
    else:
        print("Invalid seat number.")


# Function to cancel a reservation
def cancel_reservation(seats, seat_number):
    if 1 <= seat_number <= len(seats):
        if seats[seat_number - 1] is not None:
            passenger_name = seats[seat_number - 1]
            seats[seat_number - 1] = None
            print(f"Reservation for seat {seat_number} under the name {passenger_name} has been canceled.")
        else:
            print(f"Seat {seat_number} is not currently booked.")
    else:
        print("Invalid seat number.")


# Function to view all booked seats
def view_booked_seats(seats):
    print("Booked Seats:")
    booked_seats = [(i + 1, seat) for i, seat in enumerate(seats) if seat is not None]
    if not booked_seats:
        print("No seats are currently booked.")
    else:
        for seat, name in booked_seats:
            print(f"Seat {seat}: {name}")


# Main function to run the train reservation system
def main():
    total_seats = 10  # For demonstration, using 10 seats
    seats = initialize_seats(total_seats)
    
    while True:
        # Print the menu options
        print("\nTrain Reservation System")
        print("1. View Available Seats")
        print("2. Book Seat")
        print("3. Cancel Reservation")
        print("4. View Booked Seats")
        print("5. Exit")
        choice = input("Enter your choice: ")

        # Perform action based on user's choice
        if choice == '1':
            view_available_seats(seats)
        elif choice == '2':
            seat_number = int(input("Enter seat number to book: "))
            passenger_name = input("Enter passenger name: ")
            book_seat(seats, seat_number, passenger_name)
        elif choice == '3':
            seat_number = int(input("Enter seat number to cancel: "))
            cancel_reservation(seats, seat_number)
        elif choice == '4':
            view_booked_seats(seats)
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
main()
