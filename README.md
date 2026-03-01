# 🤖 AI Interview Evaluator
An AI-powered Interview Evaluation System built using Streamlit and the OpenAI API.
This application evaluates candidate answers and provides structured scoring, strengths, and improvement suggestions — similar to a real technical interview evaluation panel.
---

## 📌 Overview
The AI Interview Evaluator allows users to:
- Submit interview answers manually
- Upload a PDF containing Question–Answer pairs
- Receive strict and unbiased evaluation
- Get structured scoring across multiple parameters
- View strengths and areas for improvement

The system uses GPT-based evaluation with controlled temperature and structured JSON output to ensure consistent scoring.
---

## 🎯 Evaluation Parameters
Each answer is scored based on:
- **Technical Accuracy** (0–25)
- **Clarity** (0–15)
- **Structure** (0–10)
- **Depth** (0–10)

The system also provides:

- ✅ Strengths  
- ⚠ Areas for Improvement  
- 📊 Total Score
---

## 🛠 Tech Stack
- Python  
- Streamlit  
- OpenAI API  
- PDFPlumber  
- Regex  
- python-dotenv
---

## 📂 Features
- Manual interview answer evaluation
- PDF-based Question–Answer extraction
- Supports flexible formats like:
  - `Question:`
  - `Question)`
  - `Question-`
  - `Question=`
  - `Question~`
- Structured JSON-based evaluation
- Clean and professional UI
- Secure API key management using `.env`
---

## 🗂 Project Structure

```
AI-Interview-Answer-Evaluator/
│
├── app.py                  # Streamlit frontend application
├── streamlit_app.py        # Streamlit UI for answer evaluation
├── llm_evaluator.py        # LLM/OpenAI API evaluation logic
├── pdf_extractor.py        # Extracts questions & answers from PDFs
├── formatter.py            # Formats evaluation output and scoring
├── prompts.py              # Prompt templates and evaluation rules
├── requirements.txt        # Python project dependencies
├── README.md               # Project documentation
├── .gitignore              # Files and folders ignored by Git
├── assets                  # Images and static files
```

## ▶ How To Run Locally
### 1️⃣ Clone the repository
```bash
git clone https://github.com/AnimeshBharti/AI-Interview-Answer-Evaluator.git
cd AI-Interview-Answer-Evaluator
```
### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Add your OpenAI API Key
Create a `.env` file in the root folder:
```
API_KEY=your_openai_api_key_here
```
### 4️⃣ Run the application
```bash
streamlit run streamlit_app.py
```
---

## 🔐 Environment Variables
Required variable:

```
API_KEY
```

The `.env` file is excluded from version control for security reasons.
---

## 🚀 Future Improvements
- Export evaluation as downloadable PDF  
- Add overall candidate grading (A/B/C)  
- Add evaluation history tracking  
- Deploy publicly on Streamlit Cloud
---

## 📌 Use Case
This project can be used by:
- Students practicing interviews
- Trainers evaluating candidates
- Educational institutions
- HR professionals
---

## 👨‍💻 Author
Developed as a practical AI application project to demonstrate:
- Prompt engineering
- API integration
- Structured data handling
- Streamlit application development
- Clean project architecture
---
