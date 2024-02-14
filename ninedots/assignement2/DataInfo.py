class DataInfoDescription:
    def __init__(self, data_frame):
        self.df = data_frame

    def data_inforamation(self):
        try:
            if self.df is not None:
                print(self.df.info())
            else:
                raise Exception("Data not loaded.")
        except Exception as e:
            print(f"Error Knowing data: {str(e)}")

    def describe_data(self):
        try:
            if self.df is not None:
                print("Data Structure:")
                print(self.df.shape)
                print(f"Number of Fields in Each Record: {self.df.columns}")
                print(f"how many recors are null: {self.df.isnull().sum()}")
                print(self.df.describe())
                print("\nSummary Statistics:")
               
            else:
                raise Exception("Data not loaded.")
        except Exception as e:
            print(f"Error describing data: {str(e)}")

    def get_categorical_attributes_and_unique_values(self):
        for column in self.df.select_type(include='object').columns:
            print(f"Unique records for {column} : {self.df[column].unique()}")
    