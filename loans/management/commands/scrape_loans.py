

import os
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from loans.models import Loan

class Command(BaseCommand):
    help = 'Scrape loan data and save it to the database'

    def handle(self, *args, **options):
        
        driver = webdriver.Chrome()

    
        urls = {
            'Personal Loan': "https://www.bankbazaar.com/personal-loan.html",

        }

        for bank, url in urls.items():
            driver.get(url)

            time.sleep(5)

        
            html_content = driver.page_source

            
            soup = BeautifulSoup(html_content, 'html.parser')

            
            loan_sections = soup.find_all('div', class_='ui grid offerInnerRowRenderer')

            for section in loan_sections:
                loan_type = section.find('h4', class_="ui header mb-md mr display-inline").get_text()

            
                spans = section.find_all('span', class_="ml")

                
                if len(spans) >= 4:
                    loan_amount = spans[0].get_text().strip()
                    interest_rate = spans[1].get_text().strip()
                    tenure = spans[2].get_text().strip()
                    processing_fee = spans[3].get_text().strip()
                else:
                    loan_amount = 'N/A'
                    interest_rate = 'N/A'
                    tenure = 'N/A'
                    processing_fee = 'N/A'

                
                Loan.objects.create(
                    bank=bank,
                    loan_type=loan_type,
                    loan_amount=loan_amount,
                    interest_rate=interest_rate,
                    tenure=tenure,
                    processing_fee=processing_fee
                )

        
        driver.quit()

        print("Data saved to the database")
