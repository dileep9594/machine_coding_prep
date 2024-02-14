import json
import csv

class DataWriterTextToCSV:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def convert_and_save(self):
        try:
            # Read the data from the text file
            with open(self.input_file, 'r') as txt_file:
                # Assuming each line in the text file is a JSON-formatted dictionary
                data = [json.loads(line) for line in txt_file]

            # Extracting column names from the first row (assuming all rows have the same columns)
            columns = list(data[0].keys())

            # Writing data to the CSV file
            with open(self.output_file, 'w', newline='') as csv_file:
                # Creating a CSV writer
                csv_writer = csv.DictWriter(csv_file, fieldnames=columns)

                # Writing header
                csv_writer.writeheader()

                # Writing rows
                csv_writer.writerows(data)

            print(f"Conversion complete. Data saved to {self.output_file}")
        except Exception as e:
            print(f"Error converting and saving data: {str(e)}")


