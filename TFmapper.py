#!/usr/bin/env python3
import sys

# Open the output file in append mode
with open('mapper_output.txt', 'a') as f:
    # Read key-value pairs from the input
    for line in sys.stdin:
        # Split the input by tab character
        parts = line.strip().split('\t')
        if len(parts) == 2:
            # Extract article ID and section text
            article_id, section_text = parts
            
            # Split the section text into words
            words = section_text.split()
            
            # Emit (article_id, term) pairs for each term in the section text
            for word in words:
                print(f'{article_id}\t{word}')
                f.write(f'{article_id}\t{word}\n')
