''' counting the words in a text file and assigning the number as the value to the word using dict funtion  '''

ent=input("enter the file name")
words=open(ent)
d=dict()
ftext=words.read()
word=ftext.split()
for c in word:
    if c not in d:
        d[c]=1
    else:
        d[c]=d[c]+1
print(d)

"to check this program use the word file-https://www.py4e.com/code3/words.txt"
"copy and past the link and save the word file"
"Then check the code"
