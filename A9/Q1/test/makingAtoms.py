#!/usr/bin/env python

import sys

def main():
    x = open('blogAtomLinks.txt', 'r')
    add = "feeds/posts/default"
    for line in x:
        atom = line + add
        print atom


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)