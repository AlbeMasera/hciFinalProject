from pathlib import Path
from .llm_client import paraphrase
import json


def pharaphrase_text(text):
    prompt = Path("backend/api/prompts.txt").read_text().replace("{text}", text)
    prompt = prompt.replace("\n", " ")
    answer = paraphrase(prompt)
    response = json.loads(answer)
    print("Response: ", response)
    return response
