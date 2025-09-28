import os
import json

class FileManager:
    def __init__(self, folder_name: str):
        self.folder_name = folder_name
        os.makedirs(folder_name, exist_ok=True)

    def save_pages(self, json_text: str):
        try:
            pages = json.loads(json_text)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format")

        for name, code in pages.items():
            file_path = os.path.join(self.folder_name, name)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(code)
        print(f"Saved {len(pages)} pages in '{self.folder_name}'")
