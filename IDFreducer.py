#!/usr/bin/env python3
import sys

def calculate_idf(id_arrays):
    max_id = max(max(ids) for ids in id_arrays)  # Find the maximum unique ID
    idf_values = {}

    # Iterate through each unique ID from 0 to max_id
    for term_id in range(max_id + 1):
        count = 0  # Counter for the number of documents containing the current ID
        # Iterate through each document's ID array
        for id_array in id_arrays:
            # Check if the current ID exists in the document's ID array
            if term_id in id_array:
                count += 1  # Increment the counter if the ID is found in the array
        # Calculate IDF for the current ID
        idf = count
        idf_values[term_id] = idf

    return idf_values

# Initialize an empty list to store document ID arrays
id_arrays = []

# Process input from stdin
for line in sys.stdin:
    line = line.strip()
    if line.startswith("Document"):
        # Extract the document ID array from the line
        id_array = [int(id_str) for id_str in line.split(":")[1].strip()[1:-1].split(',')]
        id_arrays.append(id_array)

# Calculate IDF values
idf_values = calculate_idf(id_arrays)

# Write IDF values to the output file
with open("IDFreducer_output.txt", "w") as output_file:
    # Write IDF values as key-value pairs
    for term_id, idf in idf_values.items():
        output_file.write(f"{term_id}\t{idf}\n")

# Print IDF values
for term_id, idf in idf_values.items():
    print(f"Term ID: {term_id}, IDF: {idf}")
