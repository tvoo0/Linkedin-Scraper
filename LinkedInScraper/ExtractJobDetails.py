import requests
from bs4 import BeautifulSoup
from lxml import html
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}

# This function extracts the job details from the URLs of the job postings
def extract_job_details(job_urls):
    job_details_list = []
    
    for job_url in job_urls:
        response = requests.get(job_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # extracting the url to the company page to extract company size
        company_url = soup.find('a', class_='topcard__org-name-link topcard__flavor--black-link')
        company_url_parsed = company_url['href']
        company_info = requests.get(company_url_parsed, headers=headers) 
        company_info_parsed = html.fromstring(company_info.text)
          
        # title
        try:
            title = soup.find('h1', class_='top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0 topcard__title').text.strip()
        except AttributeError:
            title = 'N/A'
        
        # company
        try:
            company = soup.find('a', class_='topcard__org-name-link topcard__flavor--black-link').text.strip()
        except AttributeError:
            company = 'N/A'
        
        # description
        try:
            description = soup.find('div', class_='description__text description__text--rich').text.strip()
            description = description.replace('\n', '')  # Replace newlines with spaces
            description = re.sub(r'Show more|Show less', '', description)  # Remove "Show more" and "Show less"
        except AttributeError:
            description = 'N/A'
        
        # size
        try:
            # using xpath to extract the company size as the class name is not unique
            size = company_info_parsed.xpath('//*[@id="main-content"]/section[1]/div/section[1]/div/dl/div[3]/dd/text()')[0].strip()
            size = re.sub(r'\s+', ' ', size)
        except AttributeError:
            size = 'N/A'
        
        job_details_list.append({
            'Title': title,
            'Company': company,
            'Description': description,
            'Size': size,
            'URL': job_url
        })

    return job_details_list