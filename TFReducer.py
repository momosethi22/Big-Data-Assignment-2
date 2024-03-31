#!/usr/bin/env python3
# -*-coding:utf-8 -*
import sys

# Define the output file paths
output_file = 'TFreducer_output.txt'
vocabulary_file = 'vocabulary.txt'

# Initialize variables
current_article_id = None
vocabulary = set()

# Open the output file for writing
with open(output_file, 'w') as f_out, open(vocabulary_file, 'w') as f_vocab:
    # Read key-value pairs from the mapper and aggregate term frequencies
    for line in sys.stdin:
        # Split the input line by tab character
        parts = line.strip().split('\t')
        if len(parts) == 2:
            article_id, term = parts
            
            # Update vocabulary
            vocabulary.add(term)

    # Create a sorted list of unique terms
    sorted_vocabulary = sorted(vocabulary)

    # Write the vocabulary with assigned term IDs to the vocabulary file
    for term_id, term in enumerate(sorted_vocabulary):
        output_line = f'({term_id}, \'{term}\')\n'
        f_vocab.write(output_line)

    # Reset file pointer to beginning of input
    sys.stdin.seek(0)

    # Initialize variables for calculating term frequency
    current_article_id = None
    term_frequency = {term_id: 0 for term_id in range(len(sorted_vocabulary))}

    # Read key-value pairs from the mapper again and calculate term frequency
    for line in sys.stdin:
        # Split the input line by tab character
        parts = line.strip().split('\t')
        if len(parts) == 2:
            article_id, term = parts
            
            # Find term ID from vocabulary
            term_id = sorted_vocabulary.index(term)
            
            # If the article ID changes, write the term frequency for the previous article
            if current_article_id != article_id:
                if current_article_id:
                    # Write the article ID
                    output_line = current_article_id + '\n['
                    f_out.write(output_line)
                    
                    # Write term frequencies
                    term_freq_line = ', '.join(f'({term_id}, {frequency})' for term_id, frequency in term_frequency.items() if frequency > 0) + ']\n'
                    f_out.write(term_freq_line)
                
                # Reset term frequency for the new article
                current_article_id = article_id
                term_frequency = {term_id: 0 for term_id in range(len(sorted_vocabulary))}
        
            # Increment term frequency for the current article
            term_frequency[term_id] += 1

    # Write the term frequency for the last article
    if current_article_id:
        # Write the article ID
        output_line = current_article_id + '\n['
        f_out.write(output_line)
        
        # Write term frequencies
        term_freq_line = ', '.join(f'({term_id}, {frequency})' for term_id, frequency in term_frequency.items() if frequency > 0) + ']\n'
        f_out.write(term_freq_line)

print("TFreducer_output.txt and vocabulary.txt have been generated.")
