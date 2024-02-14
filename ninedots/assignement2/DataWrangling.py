# class DuplicateTransactionIdentifier:
#     def __init__(self, data_frame):
#         self.df = data_frame

#     def identify_duplicates(self):
#         try:
#             if self.df is not None:
#                 reversed_transactions = self.df[self.df['transactionType'] == 'REVERSAL']
#                 multi_swipe_transactions = self.df.duplicated(subset=['customerId', 'transactionAmount'])
#                 return reversed_transactions, multi_swipe_transactions
#             else:
#                 raise Exception("Data not loaded.")
#         except Exception as e:
#             print(f"Error identifying duplicates: {str(e)}")
#             return None, None

# import pandas as pd

class DuplicateTransactionIdentifier:
    def __init__(self, df):
        self.df = df
        self.reversed_transactions = None
        self.multi_swipe_transactions = None
        self.total_reversed_transactions = 0
        self.total_reversed_amount = 0
        self.total_multi_swipe_transactions = 0
        self.total_multi_swipe_amount = 0

    def identify_duplicates(self):
        try:
            filtered_df = self.df[self.df['transactionType'].isin(['PURCHASE', 'REVERSAL'])]
            self.reversed_transactions = filtered_df[filtered_df['transactionType'] == 'REVERSAL']
            self.multi_swipe_transactions = filtered_df[filtered_df.duplicated(subset=['accountNumber', 'transactionAmount', 'merchantName', 'transactionDateTime'], keep=False)]
            self.exclude_first_occurrence()
        except Exception as e:
            print(f"Error identifying duplicates: {str(e)}")

    def exclude_first_occurrence(self):
        try:
            self.reversed_transactions = self.reversed_transactions[~self.reversed_transactions.duplicated(subset=['accountNumber', 'transactionAmount', 'merchantName', 'transactionDateTime'], keep='first')]
            self.multi_swipe_transactions = self.multi_swipe_transactions[~self.multi_swipe_transactions.duplicated(subset=['accountNumber', 'transactionDateTime'], keep='first')]
        except Exception as e:
            print(f"Error excluding first occurrence: {str(e)}")

    def calculate_totals(self):
        try:
            self.total_reversed_transactions = len(self.reversed_transactions)
            self.total_reversed_amount = self.reversed_transactions['transactionAmount'].sum()

            self.total_multi_swipe_transactions = len(self.multi_swipe_transactions)
            self.total_multi_swipe_amount = self.multi_swipe_transactions['transactionAmount'].sum()
        except Exception as e:
            print(f"Error calculating totals: {str(e)}")

    def print_results(self):
        print(f"Total Reversed Transactions: {self.total_reversed_transactions}")
        print(f"Total Reversed Amount: {self.total_reversed_amount}")
        print(f"Total Multi-Swipe Transactions: {self.total_multi_swipe_transactions}")
        print(f"Total Multi-Swipe Amount: {self.total_multi_swipe_amount}")

