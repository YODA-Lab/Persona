import csv
import pandas as pd
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_directory, '..', '..','Overall_data', 'extracted_data.csv')



df = pd.read_csv(csv_file_path)
selected_rows = df[df['Overall Question'] == "Luminara Gardens is unsuitable for parties since it doesn't seem large enough. (Low Confidence)"]


selected_rows.to_csv('ChainA_data.csv', index=False)