

#write a python code for calculating following from the text file
#1. number of characters
#2. number of words
#3. numbers of lines
#4. number of repeated words
#5. numbers of times the words have been repeated


file = open("mani2.txt","r")

    
       
#1. number of characters

content=file.read()
num_charac=len(content)
print("Number of characters:")
print(num_charac)


#2. number of lines

num_of_lines=content.split("\n")
print("Number of lines:")
print(len(num_of_lines))

#3. number of words

content_split=content.split()
print(content_split)
no_of_words=len(content_split)
print("Number of words:")
print(no_of_words)
