#!/usr/bin/env python3
import sys
import re

# Initialize an empty list to store document ID arrays
id_arrays = []

# Process input from stdin
for line in sys.stdin:
    line = line.strip()
    if line.isdigit():
        # New document ID encountered, initialize a new array
        id_array = []
        id_arrays.append(id_array)
    else:
        # Extract term IDs from the line and add them to the current document's array
        term_freqs_str = line.strip('[]')
        term_freqs_str = re.split(r',\s*(?![^()]*\))', term_freqs_str)
        term_freqs = [tuple(map(int, tf.strip('()').split(','))) for tf in term_freqs_str]
        ids = [term_id for term_id, _ in term_freqs]
        id_array.extend(ids)

# Output document ID arrays as key-value pairs to stdout and write to a file
with open("IDFmapper_output.txt", "w") as output_file:
    for i, id_array in enumerate(id_arrays):
        output_str = f"Document {i+1} IDs: {id_array}\n"
        print(output_str, end='')  # Print to stdout
        output_file.write(output_str)  # Write to file
