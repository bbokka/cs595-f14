#!/usr/bin/env python

import os
import sys

#Main Function
def main () :
    saveFile       = open('friendsCount.txt.sort','r')
    writeFile      = open('numberNameCount.txt','w')
    writeFile.write("{:<10} {:<10} {} " .format('friendId' , 'friendFriendsCount', 'friendName'))
    writeFinalFile = open('finalSorted.txt','w')
    writeFinalFile.write("{:<10} {} " .format('friendId ', 'friendFriendsCount'))
    friendId          = 0
    for line in saveFile.readlines():
        nameCount          = line.split()        
        friendFriendsCount = nameCount[0]
        friendName         = nameCount[1]
        print friendFriendsCount , friendName , friendId
        friendId += 1
        writeFile.write('\n')
        writeFinalFile.write('\n')
        writeFile.write("{:<10} {:<10} {} " .format(friendId , friendFriendsCount , friendName))
        writeFinalFile.write("{:<10} {} " .format(friendId , friendFriendsCount))        
    writeFile.close()
    writeFinalFile.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)