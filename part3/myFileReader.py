
class MyFileReader:
    def __init__(self):
        self.fileDict = {}

    def readFile(self, filename):

        with open(filename) as f:
            content = f.readlines()

            self.fileDict[filename] = content

    def getFileContents(self, filename):
        return self.fileDict[filename]

    def getFileDict(self):
        return self.fileDict

