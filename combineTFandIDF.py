import re

def read_idf_values(idf_file_path):
    idf_values = {}
    with open(idf_file_path, 'r') as file:
        for line in file:
            term_id, idf = map(int, line.strip().split('\t'))
            idf_values[term_id] = idf
    return idf_values

def read_tf_values(tf_file_path):
    tf_values = {}
    with open(tf_file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.isdigit():
                # New document ID encountered, initialize a new dictionary for its TF values
                doc_id = int(line)
                tf_values[doc_id] = {}
            else:
                # Extract term IDs and TFs from the line and add them to the current document's TF dictionary
                term_freqs_str = line.strip('[]')
                term_freqs_str = re.split(r',\s*(?![^()]*\))', term_freqs_str)
                term_freqs = [tuple(map(int, tf.strip('()').split(','))) for tf in term_freqs_str]
                for term_id, tf in term_freqs:
                    tf_values[doc_id][term_id] = tf
    return tf_values

def combine_tf_idf(tf_values, idf_values, output_file_path):
    with open(output_file_path, 'w') as output_file:
        for doc_id, term_freqs in tf_values.items():
            output_file.write(f"Document {doc_id}:\n")
            for term_id, tf in term_freqs.items():
                idf = idf_values.get(term_id, 1)  # Default IDF value is 1 if term not found
                tfidf = tf / idf
                output_file.write(f"{term_id}:{tfidf:.2f} ")
            output_file.write("\n")
              # Write new line after each document

# Path to the output file
output_file_path = 'TFIDF_output.txt'

# Call the function to combine TF and IDF values and write to the output file

# Path to the TF and IDF files
tf_file_path = 'TFreducer_output.txt'
idf_file_path = 'IDFreducer_output.txt'

# Read TF and IDF values
tf_values = read_tf_values(tf_file_path)
idf_values = read_idf_values(idf_file_path)

# Combine TF and IDF values
combine_tf_idf(tf_values, idf_values, output_file_path)
    