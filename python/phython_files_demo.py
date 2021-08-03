#file handling in python
'''
f=open("file.txt","r")
if f.mode=="r":
    contents=f.read()
    #print(contents)


f=open("newfile.txt","r")
if f.mode=="r":
    contents=f.read()
    print(contents)

#appending
f=open("newfile.txt","a+")
#f.write("how are you all")
contents=f.read()
print(contents)
f.close()


f=open("newfile.txt","w")
if f.mode=="w":
    f.write("hello world! how are you doing?")
    f.close()
'''
f=open("file.txt","r")
if f.mode=="r":
    contents=f.read()
l = len(contents)
#print(l)
split=contents.split(" ")
words =list(split)
print(words)


