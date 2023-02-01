import os
import time
from datetime import datetime
from decimal import Decimal
import django
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demos.settings")
django.setup()

from demo.models import Loan, Country, Sector, Currency


class GetEibLoans:
    def __init__(self):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.url = 'https://www.eib.org/en/projects/loans/index.htm'
        self.tableValues = []

    def get_source_code(self):
        driver = self.driver
        r = requests.get(self.url)
        if r.status_code == 200:
            driver.get(self.url)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="accept_cookies_footer"]'))).click()
            time.sleep(5)  # wait to load
            load_100 = driver.find_element(By.XPATH, '//*[@id="show-entries"]')
            load_100.send_keys("100 results per page")
            time.sleep(5)  # wait to load
            table_values = self.driver.find_elements(By.XPATH, '//div/article')
            loaded_data = self.table_loans(table_values)
            self.driver.quit()
            self.store_data(loaded_data)
        return self.tableValues

    def store_data(self, tableValues):
        data_objs = []
        for data in tableValues:
            """Store Data to Database if it does not exist"""
            currency, _ = Currency.objects.get_or_create(symbol=data["currency"])
            sector, _ = Sector.objects.get_or_create(name=data["sector"])
            country, _ = Country.objects.get_or_create(name=data["country"])

            data_objs.append(
                Loan(
                    title=data["title"],
                    signature_date=data["signature_date"],
                    signed_amount=data["signed_amount"],
                    sector=sector,
                    country=country,
                    currency=currency,
                )
            )

        Loan.objects.bulk_create(data_objs)

    def table_loans(self, table_values):
        try:
            for data in table_values[1:-1]:
                row_data = str(data.text).split("\n")
                # format date to str
                f_date = datetime.strptime(row_data[0], "%d %B %Y")
                # replace currency symbol
                f_signed_amount = Decimal(str(row_data[4][1:]).replace(",", ""))
                # and slice the first character of f_loan
                f_currency = row_data[4][0]
                f_country = row_data[2]
                f_title = row_data[1]
                f_sector = row_data[3]

                self.tableValues.append({
                    "signature_date": f_date,
                    "title": f_title,
                    "country": f_country,
                    "sector": f_sector,
                    "signed_amount": f_signed_amount,
                    "currency": f_currency,
                })

            return self.tableValues
        except Exception as e:
            print(e)


fire = GetEibLoans().get_source_code()
print(fire)
