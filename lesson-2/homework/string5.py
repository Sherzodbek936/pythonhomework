word='hello'
vowels='aeuioAEUIO'
a= (word[0] in vowels)+(word[1] in vowels)+(word[2] in vowels)+(word[3] in vowels)+(word[4] in vowels)
c=len(word)-a
print(word)
print("Number of vowels",a)
print("Number of consonants",c)