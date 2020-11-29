str1 = input("Please enter a sentence: ")

print("The words in that sentence are: ", str1.split())

unique = set(str1)
print("Here are the unique words in that sentence: ",unique)