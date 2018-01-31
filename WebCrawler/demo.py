import os

# Creating a function to create a directory to store the crawled websites


def createDirectory(directory):
    if not os.path.exists(directory):
        print("Creating the directory " + directory)
        os.makedirs(directory)
# Create a function to create two files :  onList => which is file to store list of links to be crawled and whatsDone is
# file which stores links which have been visited.


def createDataFiles(projectName, baseURL):
    onList = os.path.join(projectName, 'onList.txt')
    whatsDone = os.path.join(projectName, 'whatsDone.txt')
    if not os.path.isfile(onList):
        writeFile(onList, baseURL)
    if not os.path.isfile(whatsDone):
        writeFile(whatsDone, '')


def writeFile(path, data):
    with open(path, 'w') as fileWriter:
        fileWriter.write(data)


def appender(path, data):
    with open(path, 'a') as file:
        file.write(data, '\n')


def deleteIt(path):
    open(path, 'w').close()


def fileSetter(fileName):
    result = set()
    with open(fileName, 'rt') as file:
        for line in file:
            result.add(line.replace('\n', ''))
    return result


def setFile(links, fileName):
    with open(fileName, "w") as file:
        for line in sorted(links):
            file.write(line + "\n")
