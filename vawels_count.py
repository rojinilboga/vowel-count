sentence=input("What is you name??? ")
#Create a dictonary
vowels={"a":0,"e":0,"i":0,"o":0,"u":0}



for chr in sentence:
    if chr in vowels:
        vowels[chr]+=1
print(vowels)
