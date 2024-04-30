import requests
import json
import csv
import pandas as pd

output_file = "outputs.csv"

# Open the file in read mode
with open('./2.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        # Process each line as needed
        url = "https://api.p.2chat.io/open/whatsapp/check-number/+601125857802/"+line.strip()
        payload={}
        headers = {
          'X-User-API-Key': 'UAKfc7c901b-9c91-4b2e-8413-a3204b6924f3'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        
        # response to json
        json_data = json.loads(response.text)
        # json to csv
        row = {
            'phone_number': json_data['number']['e164_format'],
            'is_valid': json_data['is_valid'],
            'iso_country_code': json_data['number']['iso_country_code'],
            'region': json_data['number']['region'],
            'carrier': json_data['number']['carrier'],
            'timezone': ', '.join(json_data['number']['timezone']),
            'on_whatsapp': json_data['on_whatsapp'],
        }

        if(row['on_whatsapp'] == True):
          # Open the CSV file in write mode
          with open(output_file, 'a', newline='') as csvfile:
            # Define field names based on the keys of the dictionary
            fieldnames = row.keys()

            # Create a CSV writer object
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Check if the file is empty and write header if needed
            if csvfile.tell() == 0:
                writer.writeheader()

            # Write the row of data
            writer.writerow(row)


