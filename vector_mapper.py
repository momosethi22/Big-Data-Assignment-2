import sys

def mapper():
    for line in sys.stdin:
        line = line.strip()
        if line.startswith("Document"):
            doc_id = int(line.split()[1].strip(':'))
            tfidf_vector = {}
        else:
            term_tfidf_pairs = line.split()
            for pair in term_tfidf_pairs:
                term_id, tfidf = map(float, pair.split(':'))
                tfidf_vector[int(term_id)] = tfidf
            print(f"{doc_id}\t{tfidf_vector}")

if __name__ == "__main__":
    mapper()
