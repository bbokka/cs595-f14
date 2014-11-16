#!/usr/bin/env python

import sys
import recommendations

def main():
    results = {}
    resultsOfloadMovieLens = recommendations.loadMovieLens()
    uniqueValues = resultsOfloadMovieLens.keys()
    length = len(resultsOfloadMovieLens)

    for key in range(0,length):
        resultsOftopMatches = recommendations.topMatches(resultsOfloadMovieLens,uniqueValues[key],n=length)        
        for value in resultsOftopMatches:
            if value[1] == uniqueValues[key]:
                pass
              
    
    for key, value in sorted(results.items(), key=lambda e: e[1], reverse=True):        
        print key, results[key]
                

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)