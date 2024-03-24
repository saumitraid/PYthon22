fp=open("mytext.txt", "a")
if fp is not None:
    if fp.write("This new content has been append using Python.\n"):
        print('Append successfully')
    else:
        print('Could not append successfully')
else:
    print('File is not open successfully')