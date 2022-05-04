""" Write a solution to find the character that has the highest number of occurrences within a certain string, ignoring
case. If there is more than one character with equal highest occurrences, return the character that appeared first
within the string. """

# strCount =
# charCount counts how many character occurences
charCount = 0
# compareCount gets the new highest charCount
compareCount = 0
# freqChar stores the most frequent char
freqChar = " "
strInput = str(input("Enter a string: "))
strInput = strInput.lower()
print("You inputted ", strInput)
# strCount = len(strInput)
# print(strCount)

for j in strInput:
    for i in strInput:
        if i == j:
            charCount += 1
    if charCount > compareCount:
        freqChar = j
        compareCount = charCount
    charCount = 0

# print("Number of occurrences is ", compareCount)
print("Most frequent character in string is ", freqChar)
