# io have 3 main types => text I/O, binary I/O, raw I/O

# Text I/O => expect and produce 'str' objects (natively made of bytes)
# 1) create a text stream is with 'open()', optional => create with specific an encoding
f = open("myfile.txt", "r", encoding='utf-8')
# Binary I/O => expects bytes-like objects and (natively produces bytes objects) No encoding
# create a binary stream is with open() with 'b' in the mode string
f = open("MYFILE.jpg", "rb")