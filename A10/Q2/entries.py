import docclass
import feedfilter

def main():
    cl=docclass.fisherclassifier(docclass.getwords) 
    cl.setdb('bbokka.db')
    print "testing the program"
    feedfilter.read('test.xml',cl)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)