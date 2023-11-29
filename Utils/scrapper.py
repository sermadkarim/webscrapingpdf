from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from io import BytesIO
import os

driver = webdriver.Chrome()

url = 'https://www.aqa.org.uk/find-past-papers-and-mark-schemes?fbclid=IwAR050K1AJ7ej8hMDKweXl4Th9maH4PUYxgOa7Wf9J-GVUHRzBVm_pgwvZcU'

driver.get(url)

time.sleep(20)

pdf_links = driver.find_elements(By.XPATH, '//div[@class=" u-ml1-5"]/p/a')

folder_path = '/Users/sermadkarim/Documents/Projects/TaskPDFs/PDFs'

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

for link in pdf_links:
    href = link.get_attribute('href')

    filename = os.path.basename(href)

    response = requests.get(href)

    if response.status_code == 200:
        pdf_content = BytesIO(response.content)

        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'wb') as pdf_file:
            pdf_file.write(pdf_content.read())

driver.quit()