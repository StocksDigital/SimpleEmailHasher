# SimpleEmailHasher

SimpleEmailHasher is a Python script designed to read a CSV file containing email addresses, hash these email addresses using SHA-256, and output the hashed emails to a new CSV file. This tool is useful for ensuring the privacy of email addresses when sharing or processing email lists.

## Features

- Reads email addresses from a CSV file.
- Finds all unique email addresses in the file.
- Hashes email addresses using the SHA-256 algorithm.
- Outputs the hashed emails to a new CSV file.

## Requirements

- Python 3.9+
- pandas

## Installation

1. Clone the repository or download the `hash_emails.py` script.
   ```bash
   git clone https://github.com/StocksDigital/SimpleEmailHasher.git
   cd SimpleEmailHasher
2. Install dependancies using `pip install -r requirements.txt`

## Usage

1. Add email_list.csv to the input file
2. `python hash_emails.py` to run the program
3. The hash list will appear in the output file

## Testing 

1. Move the email_list.csv file into the input file 
2. python `hash_emails.py` to run the program


