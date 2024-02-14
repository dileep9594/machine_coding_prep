import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
import numpy as np


class DataGraphPlot:
    def __init__(self, data_frame):
        self.df = data_frame

    def plot_histogram(self):
        try:
            if self.df is not None:
                self.df['transactionAmount'].plot(kind='hist', bins=50, title='Transaction Amount Histogram')
                plt.show()
            else:
                raise Exception("Data not loaded.")
        except Exception as e:
            print(f"Error plotting histogram: {str(e)}")

    def norm_fit(df, column_name='transactionAmount', bins=30):
        try:
            # Plot histogram for the specified column
            plt.figure(figsize=(10, 6))
            sns.histplot(df[column_name], bins=bins, kde=False, color='blue', edgecolor='black', stat='density')
            
            # Fit a normal distribution to the data
            mu, std = norm.fit(df[column_name])
            xmin, xmax = plt.xlim()
            x = np.linspace(xmin, xmax, 100)
            p = norm.pdf(x, mu, std)
            
            # Plot the fitted normal distribution
            plt.plot(x, p, 'k', linewidth=2)
            
            # Set labels and title
            plt.xlabel(column_name.capitalize())
            plt.ylabel('Density')
            plt.title(f'Histogram with Fitted Normal Distribution for {column_name.capitalize()}')
            
            # Show the plot
            plt.show()
        except KeyError:
            print(f"'{column_name}' column not found in the DataFrame.")

