from prompts import generate_prompt
from llm_evaluator import evaluate_answer
from formatter import display_result
from pdf_extractor import text_from_pdf,extract_qa_pairs
import json

print("Select Input Mode:")
print("1. Manual Input")
print("2. PDF Input")

choice=int(input("Enter your choice: "))

if choice==1:
    # Manual Input
    question=input("Enter interview question: ")
    answer=input("Enter candidate's answer: ")

    prompt_text = generate_prompt(question, answer)
    response_text = evaluate_answer(prompt_text)

    result = json.loads(response_text)

    display_result(result)

elif choice==2:
    #PDF Input
    file_path=input("Enter file path: ")

    text=text_from_pdf(file_path)
    qa_pairs=extract_qa_pairs(text)

    for question,answer in qa_pairs:
        prompt_text=generate_prompt(question, answer)
        response_text=evaluate_answer(prompt_text)

        result=json.loads(response_text)

        display_result(result)

else :
    print("Invalid Input")

