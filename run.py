from scrapers.bot.main import run_scraper
from main import run_many, run_one

def run_service():
    run_scraper()
    run_many()
run_service()