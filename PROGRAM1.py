string=input("What do you wnat to say?: ")
wrd=1
for i in string:
    if(i == ' '):
        wrd =wrd+1
print("Number of words that you entered: ",wrd)

vowels=0
consonant=0

sentence= (string)
thisVowels="AEIOUaeiou"
for i in sentence:
    if i in thisVowels:
        vowels+=1
    else:
        consonant+=1    
    
print("Number of vowels that you entered: ",vowels)
print("Number of consonants that you entered: ",consonant )       





         