from core.prompts import build_site_prompt
from infrastructure.ai_client import GeminiClient
from infrastructure.file_manager import FileManager

class SiteGeneratorService:
    def __init__(self, startup_name: str, startup_concept: str, folder_name: str = "site_output"):
        self.startup_name = startup_name
        self.startup_concept = startup_concept
        self.folder_name = folder_name
        self.client = GeminiClient()

    def generate_and_save_site(self):
       
        prompt = build_site_prompt(self.startup_name, self.startup_concept)

        response_text = self.client.generate_site(prompt)

        fm = FileManager(self.folder_name)
        fm.save_pages(response_text)
