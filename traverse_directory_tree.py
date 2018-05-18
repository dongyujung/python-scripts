from os import walk

rootDir = 'C:\Users\Documents\Yujung'

for dirName, subdirList, fileList in os.walk(rootDir):
    print 'Found directory: %s' % dirName
    for fname in fileList:
        print '\t%s' % fname
