import feedparser
import re
import math
import docclass


# Takes a filename of URL of a blog feed and classifies the entries
def read(feed,classifier):

    splitExpression = re.compile(r"<[^>]+>")
    num = 0
    print "first 50 entry classification"
    # Get feed entries and loop over them
    f=feedparser.parse(feed)

    for entry in f['entries'][0:50]:
        num = num+1
        print
        print '-----'

        # Print the contents of the entry
        title = entry['title'].encode('utf-8').replace("'","")
        print 'Title: '+title

        summary = splitExpression.sub("", entry["summary"])
        print summary

        # Combine all the text to create one item for the classifier
        fulltext = '%s\n%s' % (entry['title'], entry['summary'])
        fulltext = fulltext.replace("'","") 
        predictedString = str(classifier.classify(fulltext))

        # Print the best guess at the current category
        print "predicted category",predictedString

        # Ask the user to specify the correct category and train on that
        
        actual =raw_input('Enter the actual category it belongs to: ')        
        classifier.train(fulltext,actual)

    print "entering into another mode"
    num = 50
    print "other 50 entry classification"
    # Get feed entries and loop over them
    f=feedparser.parse(feed)
    for entry in f['entries'][50:100]:
        num = num+1
        print
        print '-----'

        # Print the contents of the entry
        title = entry['title'].encode('utf-8').replace("'","")
        print 'Title: '+title

        summary = splitExpression.sub("", entry["summary"])
        print summary

        # Combine all the text to create one item for the classifier
        fulltext = '%s\n%s' % (entry['title'], entry['summary'])
        fulltext = fulltext.replace("'","") 
        predicted= str(classifier.classify(fulltext))

        # Print the best guess at the current category
        print "predicted category",predicted

        # Ask the user to specify the correct category and train on that
        
        actualS =raw_input('Enter the actual category it belongs to: ')
        feature = raw_input('Enter a string to classifier')


        cprobabilty = round(classifier.cprob(feature,predicted),4)
        print cprobabilty
        
        #classifier.train(fulltext,actual)










