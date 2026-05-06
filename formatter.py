import streamlit as st

def display_result(result):
    st.write("\n----Interview Evaluation Result----")

    st.write(f"Technical Accuracy: {result['technical_accuracy']}/25")
    st.write(f"Clarity: {result['clarity']}/15")
    st.write(f"Structure: {result['structure']}/10")
    st.write(f"Depth: {result['depth']}/25")
    st.write(f"Communication: {result['communication']}/25")

    st.write("\nStrengths:")
    for point in result["strength"]:
        st.markdown(f"  - {point}")

    st.write("\nWeaknesses:")
    for point in result["weakness"]:
        st.markdown(f"  - {point}")

    st.write("\nSuggestions:")
    for point in result["suggestions"]:
        st.markdown(f"  - {point}")


    st.write(f"\nOverall Interview Score: {result['overall_interview_score']}/100")