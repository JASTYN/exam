"""
Write a loop that counts the number of words in a string
"""
space = ' '
count = 0
sentence = input("Enter a sentence: ")
for letter in sentence:
    if letter == space:
        count = count + 1

print(f'Your sentence has {count + 1} words')

    
