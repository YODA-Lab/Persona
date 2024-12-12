import csv
import pandas as pd
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_directory, '..', '..','Overall_data', 'extracted_data.csv')



df = pd.read_csv(csv_file_path)
selected_rows = df[df['Overall Question'] == "The advertisements contain false promotions, making Luminara Gardens unsuitable for parties. (High Confidence)"]


selected_rows.to_csv('ChainB_data.csv', index=False)