# PDF Table Extraction Script

This Python script is designed to extract tables from a PDF file using the `pdfplumber` library, clean them, and combine them into a single CSV file.

## Requirements
- Python 3.x
- `pdfplumber` library

## Installation
Install the required library using pip:
```
pip install pdfplumber
```

## Usage
1. Place your PDF file named `sample.pdf` in the same directory as the script.
2. Run the script.

## Description
- The script extracts tables from pages 2 to 152 of the PDF file.
- It cleans the extracted tables by removing the first row and the first column.
- Extracted tables are combined into a single Pandas DataFrame.
- The combined DataFrame is then exported to a CSV file named `combined_data.csv`.

## Files
- `pdf_table_extraction.py`: Main Python script.
- `sample.pdf`: Sample PDF file containing tables.

## Output
- `combined_data.csv`: Combined and cleaned data extracted from the PDF tables.

## Author
Fikri