import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}

# This function extracts the URLs of the job postings from the search results
def url_data(job_title, location, max_jobs=None):

    # search on LinkedIn using the provided job title and location
    url = f"https://www.linkedin.com/jobs/search/?currentJobId=3919015426&geoId=102095887&keywords={job_title}&location={location}"
    # extract the URLs of all job postings from the search results
    response = requests.get(url, headers=headers)
    #print(response.request.headers)
    urlData = response.text

    # Display the list of job URLs scraped using beautifulsoup
    urlScrape = BeautifulSoup(urlData, 'html.parser')
    job_elements = urlScrape.find_all('a', class_='base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]')
    job_urls = []

    # start a counter to keep track of the number of jobs processed (stopping at the maximum number of jobs specified by the user)
    jobs_processed = 0 
    
    for job_element in job_elements:
        if max_jobs is not None and jobs_processed >= max_jobs:
            break 
        
        job_urls.append(job_element['href'])
        jobs_processed += 1  # Increment the counter for processed jobs
    #print(job_urls)
    return job_urls