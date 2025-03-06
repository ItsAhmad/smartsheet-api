import smartsheet
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

url = "https://api.smartsheet.com/2.0/sheets"

api_token2 = os.getenv("api_token2")

# Initialize the Smartsheet client
smartsheet_client = smartsheet.Smartsheet(api_token2)
SHEET_ID = 4331873408864132  # Replace with your actual Sheet ID
TARGET_COLUMN_NAME = "Tier 1"  # Replace with the column name you're looking for

sheet = smartsheet_client.Sheets.get_sheet(SHEET_ID)

# Extract column names and IDs
columns = sheet.columns
column_mapping = {column.title: column.id for column in columns}

# Print column names and IDs
print("Column Names and IDs:")
for title, col_id in column_mapping.items():
    print(f"{title}: {col_id}")

# Find the target column ID
target_column_id = column_mapping.get(TARGET_COLUMN_NAME)
if not target_column_id:
    print(f"Column '{TARGET_COLUMN_NAME}' not found in sheet.")
    exit()

# Get all rows in the sheet
print(f"\nRow values under column '{TARGET_COLUMN_NAME}':")
for row in sheet.rows:
    for cell in row.cells:
        if cell.column_id == target_column_id:
            value = cell.value if hasattr(cell, 'value') else "Empty"
            print(f"Row ID {row.id}: {value}")