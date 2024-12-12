import csv
import pandas as pd
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_directory, '..', '..','Overall_data', 'extracted_data.csv')



df = pd.read_csv(csv_file_path)
selected_rows = df[df['Overall Question'] == "The distance of Luminara Gardens from most people's homes could be a concern, making Luminara Gardens unsuitable for parties. (Average Confidence)"]


selected_rows.to_csv('ChainC_data.csv', index=False)