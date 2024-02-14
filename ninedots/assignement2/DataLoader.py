from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import json
from constant import Constants

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self): 
        try:
            # with open(self.file_path, 'r') as file:
            #     data = [json.loads(line) for line in file]
            # # data = pd.read_csv('/Users/dileeppandey/Downloads/transactions.txt', delimiter='\t', dtype=Constants.dtype)
            # return pd.DataFrame(data)
            df = pd.read_csv(self.file_path)
            return df
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return None
    
    # def load_partial_data(self, chunk_size=100, num_workers=4):
    #     try:
    #         chunks = []
    #         with open(self.file_path, 'r') as file:
    #             with ThreadPoolExecutor(max_workers=num_workers) as executor:
    #                 futures = []
    #                 for chunk in pd.read_json(file, lines=True, chunksize=chunk_size):
    #                     futures.append(executor.submit(chunk))
    #                     chunks.append(chunk)

    #                 # Wait for all processing to complete
    #                 for future in futures:
    #                     future.result()

    #         # Concatenate all chunks into a single DataFrame
    #         full_data = pd.concat(chunks, ignore_index=True)

    #         print("Data loading complete.")
    #         return pd.DataFrame(full_data)
    #     except Exception as e:
    #         print(f"Error loading data: {str(e)}")
    #         return None