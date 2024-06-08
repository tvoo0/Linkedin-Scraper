import url_data
import ExtractJobDetails
import writeToCSV

# prompting user to enter job title and location
if __name__ == '__main__':
    while True:
        job_title = input("Enter the job title: ").replace(" ", "%20")
        # Check if the job title is empty
        if not job_title:
            print("Job title cannot be empty. Please enter a valid job title.")
            continue

        while True:
            location = input("Enter the location: ").replace(" ", "%20")
            # Check if the location is empty
            if not location:
                print("Location cannot be empty. Please enter a valid location.")
            else:
                break

        # prompt user to enter the maximum number of jobs they'd like to see
        while True:
            max_jobs = int(input("Enter the maximum number of jobs you'd like to see (1-40): "))
            if 1 <= max_jobs <= 40:
                break
            else:
                print("Please enter a number between 1 and 40.")
                continue
        
        job_urls = url_data.url_data(job_title, location, max_jobs)

        # Check if there are any job URLs if not prompt the user to try again
        if not job_urls:
            print("Sorry, there are no jobs under these parameters, please try again.")
            continue
        else:
            # if there are job URLs, when extract the job details and write to cvs file
            print("Extracting job details please wait...")
            job_details = ExtractJobDetails.extract_job_details(job_urls)
            if not job_details:
                print("Sorry, there are no job details available under these parameters, please try again.")
            else:
                writeToCSV.write_to_csv(job_details)
                break