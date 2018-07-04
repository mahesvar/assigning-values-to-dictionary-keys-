" the get method automatically handles the case"
" where a key is not in a dictionary"
" we can reduce four lines down to one and eliminate the if statement"

ent=inout('enter file name')
words=open(ent)
d=dict()
ftext=words.read()
word=ftext.split()
for c in word:
    d[c]=d.get(c,0)+1 
print(d)


#else use if statement instead og get function inside for loop
#the will look like
"""
if c not in d:
    d[c]=1
else:
    d[c]=d[c]+1
"""


