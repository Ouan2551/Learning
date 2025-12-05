# 1) open/ open modes
path = r'D:\Important files Nannaphat\coding\Learning\python\2.Python_IO\myfile.txt'
animals = open(path, 'a+')
# r = open for read (default)
# w = open for write, truncate
# r+ = open for write and read
# w+ = open for read/write, truncate
# a+ = open for read/append

# 2) read
text = animals.read()
print(text)

# 3) read lines
for animal in animals:
    print(animal)
    
# 4) write and append
animals.write('bye\n')
animals.write('bye\n')

# 5) close
animals.close()