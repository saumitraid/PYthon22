try:
    fp=open('mytext1.txt','w')
    print(fp.read())
except IOError:
    print("The file does not exists")
