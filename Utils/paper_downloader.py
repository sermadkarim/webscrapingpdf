# Utils/paper_downloader.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
from io import BytesIO
import os

class PaperDownloader:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()

    def click_with_retry(self, element):
        try:
            element.click()
        except Exception as e:
            print("Click")
            time.sleep(1)
            ActionChains(self.driver).move_to_element(element).click().perform()

    def download_papers(self):
        self.driver.get(self.url)
        time.sleep(5)

        subject_dropdown_xpath = "//select[1]"
        subject_dropdown = self.driver.find_element(By.XPATH, subject_dropdown_xpath)
        self.click_with_retry(subject_dropdown)

        subject_options_xpath = "//select[@id='js-pastPaper-subjects']/option[position() > 1]"
        subject_options = self.driver.find_elements(By.XPATH, subject_options_xpath)

        for subject_option in subject_options:
            self.click_with_retry(subject_option)
            time.sleep(2)

            qualification_dropdown_xpath = "//select[@name='js-pastPaper-qualifications']"
            qualification_dropdown = self.driver.find_element(By.XPATH, qualification_dropdown_xpath)
            self.click_with_retry(qualification_dropdown)
            time.sleep(2)

            qualification_options_xpath = "//select[@name='js-pastPaper-qualifications']/option[position() > 1]"
            qualification_options = self.driver.find_elements(By.XPATH, qualification_options_xpath)

            for qualification_option in qualification_options:
                self.click_with_retry(qualification_option)
                time.sleep(2)

                spec_qualification_dropdown_xpath = "(//select)[3]"
                spec_qualification_dropdown = self.driver.find_element(By.XPATH, spec_qualification_dropdown_xpath)
                self.click_with_retry(spec_qualification_dropdown)
                time.sleep(2)

                spec_qualification_options_xpath = "//select[@name='js-pastPaper-specifications']/option[position() > 1]"
                spec_qualification_options = self.driver.find_elements(By.XPATH, spec_qualification_options_xpath)

                for spec_qualification_option in spec_qualification_options:
                    self.click_with_retry(spec_qualification_option)
                    time.sleep(2)

                    pdf_links = self.driver.find_elements(By.XPATH, '//div[@class=" u-ml1-5"]/p/a')

                    folder_path = '/Users/sermadkarim/Documents/Projects/TaskPDFs/PDFs'
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)

                    for link in pdf_links:
                        href = link.get_attribute('href')
                        filename = os.path.basename(href)
                        response = requests.get(href)

                        if response.status_code == 200:
                            pdf_content = BytesIO(response.content)

                            filename_on_page = link.text.strip()
                            file_path = os.path.join(folder_path, f'{filename_on_page}.pdf')

                            with open(file_path, 'wb') as pdf_file:
                                pdf_file.write(pdf_content.read())

        self.driver.quit()
