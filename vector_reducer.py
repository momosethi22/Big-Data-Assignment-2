import sys

def reducer():
    for line in sys.stdin:
        doc_id, tfidf_vector_str = line.strip().split('\t')
        tfidf_vector = eval(tfidf_vector_str)
        print(f"Document {doc_id}: {tfidf_vector}")

if __name__ == "__main__":
    reducer()
