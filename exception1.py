try:
    fp=open('mytext1.txt','w')
    print(fp.read())
except Exception as e:
    print(e)
