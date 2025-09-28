def build_site_prompt(startup_name: str, startup_concept: str) -> str:
    return f"""
You are an expert in modern web development and UI/UX design.

Your task is to generate a complete website structure based on the given site name and idea.

Instructions:
1. Analyze the provided site name and idea, then decide what pages are needed for this website.
2. For each page:
   - Provide the page name (use only English letters without spaces, e.g., "home.html", "about.html").
   - Provide the **full HTML code** for the page.
   - The code must be **complete and ready to run** with modern, professional design.
   - Use **HTML5, CSS3, and optionally Bootstrap or Tailwind CSS** for styling.
   - Include **widgets and interactive elements** (cards, buttons, forms, navigation bar, footer).
3. All pages must include a **navigation bar** with links to the other pages, using the page names you suggested.
4. The design must be **responsive**, **modern**, and **user-friendly**.
5. The output format must be a **JSON object**, where:
   - The key = the page name with `.html` extension.
   - The value = the complete HTML code of that page.
Site name: {startup_name}.
Site concept: {startup_concept}.

Return only a valid JSON object containing the pages as keys and their full HTML code as values, without any extra text.

"""
