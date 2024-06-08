# Linkedin-Scraper

## Description
This Linkedin Scraper uses the data scraping tool BeautifulSoup only to extract job postings from LinkedIn without having to be signed in.

The program will extract the following details and write to a CSV file:
1. Job Title
2. Job Description
3. Company
4. Company Size
5. Job URL

## Installation

In order to run the program, the user must install these Python Libraries and run these commands in their terminal (if not already installed):
```
pip install requests
pip install BeautifulSoup4
pip install re
pip install csv
```

## Source Code Description and Use

### URL_data.py

This file is in charge of searching for job postings with the user's inputs from main.py and extract the URLs of the specified amount of job postings. The function uses the python library requests to get the content of the search page then uses BeautidulSoup to parse the URLs from the HTML. The list of URLs will be returned for the next function to extract its properties. 

### ExtractJobDetails.py

This file goes into every URL that was extracted from URL_data.py and scraps the needed information listed above. Similar to URL_data, the function will use requests to get the page contents of the job posting and use BeautifulSoup to get the specific details. 

However, in the guest version of a LinkedIn job posting, not all that was needed were located on that page such as the employee size. Therefore I had to further parse the URL from the job posting to go to the company page in order to extract the company size information.

If the job/company page does not provide the information to extract, it that detail will be returned as "N/A".

Once all the job details have been parsed, they are sent to be written to a CSV file.

### WriteToCSV.py

This file is responsible for writing all the job details from ExtractJobDetails.py into a CSV file. This funtion will create a file in the project folder called "job_details.csv" and write all the job information into the file.

Once the function has completed writing the to the CSV file, the file will close and the program will shut down.


### Main.py

This file will prompt the user to enter a job title and location of their choice. If they enter an empty string they will be prompted once again to enter a valid input. 

```
Enter the job title: 
Enter the location: 
```

The user will then be prompted to provide the amount of jobs they would like to see with the max being 40 jobs.
```
Enter the maximum number of jobs you'd like to see (1-40): 
```

Once entered, URL_data.py will run to extract the job postings search with the given parameters. If URL_data returns an empty list, that indicates that there are no job postings under the user's inputs so the program will prompt the user to start over and input the job title and location once again. 

If the list is not empty, ExtractJobDetails.py and writeToCSV.py will run without the user having to see anything and successfully write the job contents to a CSV file that can be viewed.
