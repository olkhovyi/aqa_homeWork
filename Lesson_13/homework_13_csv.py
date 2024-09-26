import csv
from pathlib import Path


# Function to read a CSV file with the correct extension
def read_csv(file_name, delimiter):
    with open(file_name, mode='r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        data = [row for row in reader]
    return data

# Reading data from two CSV files
data1 = read_csv('rmc.csv', delimiter=';')
data2 = read_csv('r-m-c.csv', delimiter=';')

# Merge data from both files (including header)
combined_data = data1 + data2

header = combined_data[0]  # the first line is the title
rows = combined_data[1:]   # other terms are data

# Duplicate removal
unique_rows = []
for row in rows:
    if row not in unique_rows:
        unique_rows.append(row)

result_path_file = Path('result_olkhovyi.csv')

# Write data to a new CSV file
with open(result_path_file, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(header)
    writer.writerows(unique_rows)

print(f"Done: {result_path_file}")


