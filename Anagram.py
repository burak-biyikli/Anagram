import time


#Secondary Check to ensure Elements (So that {1,1,1,} is not subset of {1})
def check(master,substring):
    for i in master:
        if master.count(i)<substring.count(i):
            return False
    return True

#Character Input
RawChars = input("Enter 6 chars")
chars = list(RawChars)
chars.sort()
#Debug
print(chars)

#Dramatic Pause
time.sleep(.5)

#Declare Place To store words
words = [ [],[],[],[] ]

#Read In First File
file = "20k.txt"
with open(file) as g:
    stuff = g.readlines()
stuff = [x.strip() for x in stuff]

#Check File
for i in stuff:

    if (len(i)<3 or len(i)>6):
        continue

    t = list(i)
    if ( set(t).issubset(chars) ):
        if( check(chars,t)):
            words[len(i)-3].append(i)

#Read in second file
file = "words_alpha.txt"
with open(file) as g:
    stuff = g.readlines()
stuff = [x.strip() for x in stuff]

#Check Second File
for i in stuff:

    if (len(i)<3 or len(i)>6):
        continue

    t = list(i)
    if ( set(t).issubset(chars) ):
        if( check(chars,t)):
            if(i not in words[len(i)-3]):
                words[len(i)-3].append(i)

#Print Results in array
for i in reversed(words):
    for c in i:
        print(c)
        input()

#Stay open just in case
time.sleep(60)
