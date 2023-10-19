import os
path = '/Users/jjyoun/Downloads/xx.mp4'

name = os.path.basename(path)
# print(name) # xx.mp4

# print(os.stat(path))

file = open('/Users/jjyoun/box/intuworks/vs-workspace/4python/study/test.txt', 'rb') 
data = file.read()
print(data)
file.close()
