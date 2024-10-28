import PyPDF2
import pyttsx3

# Extract text from PDF
pdf_file = open('<directory_location/name.pdf>', 'rb') #enter the name and also specify the directory of the pdf file 
pdf_reader = PyPDF2.PdfReader(pdf_file)
text = ""

for page in pdf_reader.pages:
    text += page.extract_text()

pdf_file.close()

# Convert text to speech
tts_engine = pyttsx3.init()
tts_engine.save_to_file(text, '<dir/name.mp3>')#enter the name and also specify the directory of the audio file 
tts_engine.runAndWait()