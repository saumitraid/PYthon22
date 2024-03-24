fp=open("mytext.txt", "w")
if fp is not None:
    if fp.write("This file has been created using Python.\n"):
        print('Write successfully')
    else:
        print('Could not write successfully')
else:
    print('File is not open successfully')