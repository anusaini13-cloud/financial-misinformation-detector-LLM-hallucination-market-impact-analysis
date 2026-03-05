from groq import Groq
import time
from dotenv import load_dotenv
import os

def build_prompt(headline):
    return f"""You are a financial fact-checking assistant specializing in Indian and global financial markets.

Your task is to classify the following financial news headline as either FACTUAL or MISLEADING.

- FACTUAL: The headline accurately represents a real financial event, uses precise language, and does not exaggerate or distort facts.
- MISLEADING: The headline exaggerates, distorts, omits critical context, uses sensational language, or is designed to manipulate market sentiment.

Headline: "{headline}"

Respond in this exact format and nothing else:
CLASSIFICATION: <FACTUAL or MISLEADING>
CONFIDENCE: <HIGH or MEDIUM or LOW>
REASONING: <one sentence explaining your decision>"""


load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
def generate_content(prompt):
    chat = client.chat.completions.create(
      model="llama-3.1-8b-instant",  # smaller = faster response time
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return chat.choices[0].message.content

def parse_response(text):
    try:
        lines = text.strip().split('\n')
        # filter empty lines
        lines = [l for l in lines if l.strip()]
        classification = lines[0].split(':')[1].strip()
        confidence = lines[1].split(':')[1].strip()
        reasoning = lines[2].split(':')[1].strip()
        return {
            'classification': classification,
            'confidence': confidence,
            'reasoning': reasoning
        }
    except Exception as e:
        return {
            'classification': 'ERROR',
            'confidence': 'ERROR',
            'reasoning': str(e)
        }