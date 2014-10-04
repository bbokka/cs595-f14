#!/usr/bin/env python

import sys
import math

# Main Function
def main():
    total_doc_corpus = 20000000000
    docs_with_term   = 653000000
    
    #open the file to read word_count , total_count ,
    f = open('cal.txt', 'r') 

    inverse_term = math.log(
        (float(total_doc_corpus) / docs_with_term),
        2
    )

    
    for line in f.readlines():
        # splitting the line based on space
        data        = line.split()
        # data is stored the data list so pull out using index values
        # url is 4rth element stored at 3 index
        url         = data[3]
        # word_count is 1st element stored at 0 index
        word_count  = int(data[0])
        # total_count is 2nd element stored at 1 index
        total_count = int(data[1])
        # TF calculation
        term_frequency = float(word_count)/total_count
        # TFIDF calculation
        term_inverse_frequency= term_frequency* inverse_term

        print url , word_count, total_count,term_frequency ,inverse_term , term_inverse_frequency


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)