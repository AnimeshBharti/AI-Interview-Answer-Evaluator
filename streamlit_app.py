import streamlit as st
import json
from prompts import generate_prompt
from llm_evaluator import evaluate_answer
from formatter import display_result
from pdf_extractor import text_from_pdf, extract_qa_pairs

st.title("AI Interview Evaluator")
st.image("assets/Image.jpeg", use_container_width=True)

# Input mode selection
mode = st.radio("Select Input Mode", ["Manual Input", "Upload PDF"])

# ------------------ MANUAL INPUT ------------------
if mode == "Manual Input":
    question = st.text_area("Enter Interview Question")
    answer = st.text_area("Enter Candidate Answer")

    if st.button("Evaluate"):
        if question and answer:
            prompt = generate_prompt(question, answer)
            result = evaluate_answer(prompt)

            if result:
                st.subheader("Evaluation Result")

                st.write("### Scores")
                st.write(result)

                st.write("### Strengths")
                for point in result["strength"]:
                    st.write("- ", point)

                st.write("### Weaknesses")
                for point in result["weakness"]:
                    st.write("- ", point)

                st.write("### Suggestions")
                for point in result["suggestions"]:
                    st.write("- ", point)

            else:
                st.error("Failed to evaluate. Check API response.")

        else:
            st.warning("Please enter both question and answer.")

# ------------------ PDF INPUT ------------------
elif mode == "Upload PDF":
    uploaded_file = st.file_uploader("Upload Interview PDF", type=["pdf"])

    if uploaded_file and st.button("Evaluate PDF"):
        with st.spinner("Processing PDF..."):

            with open("temp.pdf", "wb") as f:
                f.write(uploaded_file.read())

            text = text_from_pdf("temp.pdf")
            qa_list = extract_qa_pairs(text)

            for question, answer in qa_list:
                prompt = generate_prompt(question, answer)
                result = evaluate_answer(prompt)

                if result:
                    st.subheader(f"Evaluation for Question: {question}")

                    st.write("### Scores")
                    st.write(result)

                    st.write("### Strengths")
                    for point in result["strength"]:
                        st.markdown(f"- {point}")

                    st.write("### Weaknesses")
                    for point in result["weakness"]:
                        st.markdown(f"- {point}")

                    st.write("### Suggestions")
                    for point in result["suggestions"]:
                        st.markdown(f"- {point}")

                else:
                   st.error(f"Evaluation failed for question: {question}")