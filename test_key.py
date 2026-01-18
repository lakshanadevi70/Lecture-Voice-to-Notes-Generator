from dotenv import load_dotenv
from openai import OpenAI
import os

# LOAD .env FILE
load_dotenv()

# CREATE CLIENT
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# TEST CALL
response = client.responses.create(
    model="gpt-4o-mini",
    input="Say hello"
)

print(response.output_text)

