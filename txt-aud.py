import PyPDF2
import pyttsx3

# Extract text from PDF
pdf_file = open('name_with_directory_of_pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
text = ""

for page in pdf_reader.pages:
    text += page.extract_text()

pdf_file.close()

# Convert text to speech
tts_engine = pyttsx3.init()
tts_engine.save_to_file(text, 'directory_and_name_of_audioFile')
tts_engine.runAndWait()