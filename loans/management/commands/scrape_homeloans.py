from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from loans.models import HomeLoanData

class Command(BaseCommand):
    help = 'Scrape loan data and store it in the database'

    def handle(self, *args, **kwargs):
        # Set up the Chrome driver using the webdriver_manager
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        urls = {
            'Home Loan': "https://www.bankbazaar.com/home-loan.html"
        }

        for bank, url in urls.items():
            driver.get(url)
            time.sleep(5)  #it is for wait to close the page

            html_content = driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')

            table = soup.find('tbody')

            # Extract the data
            for row in table.find_all('tr')[1:]:
                cols = row.find_all('td')
                data = [col.get_text(strip=True) for col in cols]

                # Save to the database
                HomeLoanData.objects.create(
                    bank_name=data[0],
                    interest_rate=data[1],
                    processing_fee=data[2],
                    loan_amount_tenure=data[3]
                )

        driver.quit()
        self.stdout.write(self.style.SUCCESS('Successfully scraped and stored loan data'))
