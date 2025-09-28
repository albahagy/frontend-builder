from google import genai
from config import API_KEY, MODEL_NAME

class GeminiClient:
    def __init__(self):
        self.client = genai.Client(api_key=API_KEY)

    def generate_site(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        return response.text.strip()
