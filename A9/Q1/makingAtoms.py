#!/usr/bin/env python

import sys

def main():
    saveFile = open('blogLinksLists.txt', 'r')
    writeFile = open('blogLinksAtom.txt', 'w')
    add = "feeds/posts/default?max-results=500"
    for line in saveFile:
        writeFile.write(line+add)
        writeFile.write("\n")
    saveFile.close()
    writeFile.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)