from core.services import SiteGeneratorService

def main():
    #you can change site name and his prompt from here ;)
    startup_name = "Albahagy"
    startup_concept = (
        "A website for an Egyptian software company specialized in developing "
        "mobile applications and web platforms. The site showcases innovative digital "
        "solutions for businesses and individuals, highlights services such as web design, "
        "app development, artificial intelligence, and digital marketing, and presents "
        "a portfolio of past projects with a modern, professional design that reflects "
        "the company’s identity and builds client trust."
    )

    generator = SiteGeneratorService(startup_name, startup_concept, folder_name="Albahagy_Site")
    generator.generate_and_save_site()

if __name__ == "__main__":
    main()
