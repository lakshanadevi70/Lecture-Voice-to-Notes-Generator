# 🎙️ Lecture Voice-to-Notes Generator
## 📌 Overview
Students often miss important points during lectures because it is difficult to listen and take notes at the same time.
Lecture Voice-to-Notes Generator solves this problem by converting spoken lectures into text using Speech-to-Text AI and then transforming that text into structured study materials such as summaries, quizzes, and flashcards using Generative AI.

This project is designed to improve learning efficiency and accessibility for students.

## 🚀 Features
- 🎤 Speech-to-Text Conversion – Converts recorded or live lecture audio into text
- 📝 Automatic Summarization – Generates concise and clear study notes
- ❓ Quiz Generation – Creates practice questions from lecture content
- 🧠 Flashcards Creation – Produces flashcards for quick revision
- ⏱️ Saves time and improves focus during lectures

## 🛠️ Tech Stack
- Programming Language: Python
- Speech-to-Text: OpenAI Whisper
- Generative AI: OpenAI (GPT models)
- Frontend: Streamlit

## 📂 Project Structure
Lecture-Voice-to-Notes-Generator/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (not pushed to GitHub)
├── lecture_video.mp4   # Sample lecture file
├── test_key.py         # API key testing script
└── README.md

## 🔐 API Key Setup (Important)
This project uses external AI APIs. API keys are NOT included in this repository for
security reasons.
1 - Steps to Configure:
      - Create a .env file in the root directory
      - Add your API key(s) as shown below:
OPENAI_API_KEY=your_api_key_here
SPEECH_API_KEY=your_speech_api_key_here
2 -  Ensure .env is added to .gitignore
     A sample file .env.example is provided for reference.

## ▶️ How to Run the Project
1 - # Clone the repository
git clone https://github.com/your-username/lecture-voice-to-notes-generator.git

2 - # Navigate to the project directory
cd lecture-voice-to-notes-generator

3 - # Install dependencies
pip install -r requirements.txt

4 - # Run the application
python app.py

## 📌 Use Cases
- Students attending online or offline lectures
- Revision before exams
- Accessibility support for hearing or writing difficulties
- Teachers generating learning materials automatically

## 🔮 Future Enhancements
- Live lecture transcription
- Multi-language support
- Export notes as PDF
- Mobile app integration
- Cloud storage for lecture history
