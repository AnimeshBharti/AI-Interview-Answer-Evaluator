import pdfplumber
import re


def text_from_pdf(file_path):
    text=""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() +"\n"

    return text

def extract_qa_pairs(text):
    """
    Extract QA pairs from a text(PDF)
    Support:
    Question: , Question) , Question~ , Question- , Question= , Question.
    Answer: , Answer) , Answer~ , Answer- , Answer= , Answer.
    """
    pattern=r"""
    Question\s*[:\)\~\-\=\.]\s*(.*?)       #Question's all format expected in pdf
    \s*
    Answer\s*[:\)\~\-\=\.]\s*(.*?)         #Answer's all format expected in pdf
    (?=\n\s*Question\s*[:\)\.\~\-\=]|\Z)   #For next question or end
    """

    matches = re.findall(pattern, text, re.DOTALL | re.VERBOSE)

    qa_pairs=[]

    for question, answer in matches:
        qa_pairs.append((question.strip(), answer.strip()))

    return qa_pairs
