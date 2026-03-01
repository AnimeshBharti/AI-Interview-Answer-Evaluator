from openai import OpenAI
import os
import json
from dotenv import load_dotenv
load_dotenv()
client=OpenAI(api_key=os.getenv("API_KEY"))

def evaluate_answer(prompt_text):
    try:
        response=client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content":"You are an interview evaluator."},
                {"role": "user", "content": prompt_text}
            ],
            temperature=0.3,
            max_tokens=800,
        )
        content=response.choices[0].message.content.strip()
        try:
            return json.loads(content)
        except json.decoder.JSONDecodeError:
            print("JSON Parsing Error")
            print("Raw Output:", content)
            return None

    except Exception as e:
        print("API Error:", e)
        return None