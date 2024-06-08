import csv

# Function to write the job details to a CSV file
def write_to_csv(job_details_list, filename='job_details.csv'):
    # Define the column names
    fieldnames = ['Title', 'Company', 'Description', 'Size', 'URL']

    # Open the file in write mode
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        # Write the job details
        for job in job_details_list:
            writer.writerow(job)

    print(f"Data written to {filename} successfully.")