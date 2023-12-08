
# Web Scraping PDF Downloader

This Python script uses Selenium to automate the process of downloading a large number of PDFs from the AQA website's past papers and mark schemes page. The script navigates through various dropdown menus to select specific subjects, qualifications, and specifications, and then extracts and downloads the PDF links available on the page.




## Requirements

Ensure you have the following libraries installed:

```bash
 pip install selenium requests
```
Additionally, make sure you have the ChromeDriver installed and available in your system's PATH.

## Install Requirements
1. Clone the Repository
```bash
git clone https://github.com/sermadkarim/webscrapingpdf.git
```

2. Install the required libraries
```bash
pip install -r webscrapingpdf/requirements.txt
```
3. Run your script
```bash
python3 webscrapingpdf/main.py
```


## Code Explanation
The script is designed to download PDFs from the AQA website and is divided into the following sections:
1. Importing libraries
```bash
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
from io import BytesIO
import os
```

2. Class Definition - PaperDownloader

The PaperDownloader class initializes the Chrome WebDriver and contains methods to handle clicks with retries and download papers.

3. __init__ Method
```bash
def __init__(self, url):
    self.url = url
    self.driver = webdriver.Chrome()
```

4. 'click_with_retry' Method
```bash
def click_with_retry(self, element):
    try:
        element.click()
    except Exception as e:
        print("Click")
        time.sleep(1)
        ActionChains(self.driver).move_to_element(element).click().perform()
```
The click_with_retry method handles clicking on web elements with retries to overcome occasional errors.

5. 'download_papers' Method
```bash
def download_papers(self):
    # ... (code for navigating through dropdowns and downloading PDFs)
    self.driver.quit()

```
The download_papers method automates the process of navigating through dropdowns, extracting PDF links, and downloading the corresponding files.

6. Main Execution
```bash
if __name__ == "__main__":
    url = 'https://www.aqa.org.uk/find-past-papers-and-mark-schemes?fbclid=IwAR050K1AJ7ej8hMDKweXl4Th9maH4PUYxgOa7Wf9J-GVUHRzBVm_pgwvZcU'
    downloader = PaperDownloader(url)
    downloader.download_papers()
```
The main block creates an instance of the PaperDownloader class, passing the AQA website URL, and invokes the download_papers method.

## Output

The script downloads PDF files to the specified folder (/Users/sermadkarim/Documents/Projects/TaskPDFs/PDFs). The filenames are derived from the text of the corresponding links on the webpage.

Note: Make sure to update the folder path to your preferred destination.


# Others Folder
Python Scripts

### Automatic Web Scraper (autoscraper.py):
This script utilizes the autoscraper library to automatically extract data from web pages. It is designed for ease of use and quick setup. Customize the scraper according to your specific needs.
### Manual Web Scraper (scraper.py):
This script uses the Selenium library for manual web scraping. It navigates through web pages, interacts with elements, and extracts information. Customize the script based on the structure of the target website.
### PDF to LaTeX Converter (latex.py):
The latex.py script converts PDF files to LaTeX format. It is a useful tool for transforming PDF documents into a format suitable for LaTeX typesetting.
### LaTeX Output (output.tex):
The output.tex file is the result of the PDF to LaTeX conversion. Customize and further edit this LaTeX file as needed.
### Utils Folder:
The 'Utils' folder contains utility classes used in the main program. Organizing classes into this folder promotes modularity and maintainability.

# Utils Folder
This folder (Utils) contains utility modules for web scraping and PDF manipulation. The primary module in this folder is paper_downloader.py, which includes the PaperDownloader class for automating the download of papers from a website.

### 'paper_downloader.py'

## Overview

The paper_downloader.py module provides a class, PaperDownloader, designed to streamline the process of downloading papers from a specific website. It uses Selenium for web automation and Requests for downloading PDFs.

### Dependencies
selenium: Web automation library
requests: HTTP library for handling requests

Install the dependencies using:
```bash
pip install selenium requests
```
## Usage
Import the PaperDownloader class in your main script.
```bash
from Utils.paper_downloader import PaperDownloader
```

## Create an instance of PaperDownloader and invoke the download_papers method.
```bash
if __name__ == "__main__":
    url = 'https://www.example.com/papers'
    downloader = PaperDownloader(url)
    downloader.download_papers()
```
# Note
Ensure you have the correct web driver (e.g., ChromeDriver) installed for Selenium. Update the script if needed.
Be aware of the website's terms of service and legal requirements when using web scraping techniques.
