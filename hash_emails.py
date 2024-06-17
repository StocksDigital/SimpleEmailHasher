
import hashlib
import os
import pandas as pd
import re


def sha256_hash(email):
    """Returns the SHA-256 hash of the given email."""
    return hashlib.sha256(email.encode()).hexdigest()


def find_emails(df):
    """Finds all email addresses in the DataFrame and returns a list of unique emails."""
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?')
    emails = set()

    for column in df.columns:
        if df[column].dtype == object:
            for value in df[column]:
                if pd.notna(value):  # Check if the value is not NaN
                    found_emails = email_pattern.findall(str(value))
                    emails.update(found_emails)
    return list(emails)


# Define input and output paths
input_path = 'input/emails_list.csv'
output_path = 'output/hashed_emails.csv'

# Ensure output directory exists
os.makedirs('output', exist_ok=True)

# Read the CSV file from the input directory with error handling
try:
    df = pd.read_csv(input_path)
except FileNotFoundError:
    print(f"Error: The file {input_path} was not found.")
    exit(1)
except pd.errors.EmptyDataError:
    print(f"Error: The file {input_path} is empty.")
    exit(1)
except pd.errors.ParserError:
    print(f"Error: The file {input_path} could not be parsed.")
    exit(1)

# Find all unique email addresses in the DataFrame
emails = find_emails(df)

# Hash the email addresses
hashed_emails = [sha256_hash(email) for email in emails]

# Create a DataFrame with the hashed emails
hashed_df = pd.DataFrame(hashed_emails, columns=['hashed_emails'])

# Write the hashed emails to a new CSV file in the output directory with error handling
try:
    hashed_df.to_csv(output_path, index=False)
    print(f"Hashed emails have been written to {output_path}")
except Exception as e:
    print(f"Error: Could not write to file {output_path}. {e}")
    exit(1)
