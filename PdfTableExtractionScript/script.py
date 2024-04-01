import subprocess

# Install pdfplumber
subprocess.run(['pip', 'install', 'pdfplumber'])
import pdfplumber
import pandas as pd

pdf = pdfplumber.open("sample.pdf")
combined_df = pd.DataFrame()  # Initialize an empty DataFrame

for i in range(2, 153):
    page = pdf.pages[i - 1]
    table = page.extract_table()
    cleaned_table = [row[1:] for row in table]
    df = pd.DataFrame(cleaned_table[2:], columns=cleaned_table[1])
    combined_df = pd.concat([combined_df, df], ignore_index=True)

# Write the combined dataframe to a new CSV file
combined_df.to_csv('combined_data.csv', index=False)