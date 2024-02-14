import json
from multiprocessing import process
import pandas as pd
from pymongo import MongoClient
from DataGraph import DataGraphPlot
from DataInfo import DataInfoDescription

from DataLoader import DataLoader
from DataWrangling import DuplicateTransactionIdentifier
from FraudDetection import FraudDetectionModelBuilder
from datawriter import DataWriterTextToCSV

if __name__ == '__main__':
    # Connect to MongoDB
    # client = MongoClient("mongodb+srv://root:root@cluster0.upi4ff4.mongodb.net/?retryWrites=true&w=majority")
    # db = client["assginements"]
    # collection = db["transactions"]

    # Insert data into MongoDB
    # collection.insert_many(transactions)

    # Print the number of documents in the collection
    # print(collection.count_documents({}))

    input_file = "/Users/dileeppandey/Downloads/transactions.txt"
    output_file = "/Users/dileeppandey/machine_coding_prep/ninedots/assignement2/transactions.csv"
    # Create an instance of the class
    # data_writer = DataWriterTextToCSV(input_file, output_file)
    # Call the method to convert and save data
    # data_writer.convert_and_save()

    data_loader = DataLoader(output_file)
    data_frame = data_loader.load_data()
    info_description = DataInfoDescription(data_frame)
    print(data_frame.isnull().sum())
    info_description.data_inforamation()
    info_description.describe_data()

    graph_plotter = DataGraphPlot(data_frame)
    graph_plotter.plot_histogram()
    duplicate_identifier = DuplicateTransactionIdentifier(data_frame)
    # Call the methods
    duplicate_identifier.identify_duplicates()
    duplicate_identifier.calculate_totals()
    duplicate_identifier.print_results()
    fraud_model_builder = FraudDetectionModelBuilder(data_frame)
    fraud_model_builder.build_fraud_model()
