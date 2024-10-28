git clone https://github.com/your-username/your-repo.git
cd your-repo
'''import PyPDF2
import pyttsx3

# Extract text from PDF
pdf_file = open('P:/python/660440237-Maine-Apni-Behnon-Ko-Kaise-Choda-Aur-Un-Ko-Chudwaya-Part-1.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
text = ""

for page in pdf_reader.pages:
    text += page.extract_text()

pdf_file.close()

# Convert text to speech
tts_engine = pyttsx3.init()
tts_engine.save_to_file(text, 'P:/python/output_audio.mp3')
tts_engine.runAndWait()'''