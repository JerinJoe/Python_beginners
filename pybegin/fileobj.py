#file object

# f = open('test.txt','r')
# print(f.mode)
# f.close()

#use context manager    

with open('test.txt','r') as f:
    # f_contents = f.read()
    # f_contents = f.readlines()
    # f_contents = f.readline()
    # print(f_contents,end='')
    
    # for line in f:
    #     print(line,end='')
    # print(f_contents)
    size_to_read = 5
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents,end='*')
        f_contents = f.read(size_to_read)
        # f.tell() used to find position in f_contents