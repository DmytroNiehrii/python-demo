import os

# iterate file system
for i in os.walk('./files'):
    print(i)

# collect paths
paths = []
allFiles = []
for path, dirs, files in os.walk('./files'):
    paths.append(path)
    for file in files:
        allFiles.append(os.path.join(path, file))
print('paths:', paths)
print('allFiles:', allFiles)

# read lines from files
lineCount = 0
for file in allFiles:
    f = open(file, 'r')
    lineCount += len(f.readlines())
print('Found totally', lineCount, 'lines')