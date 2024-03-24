fp=open('mytext.txt','r')
if fp is not None:
    print(fp.read())
else:
    print("File does not exists")