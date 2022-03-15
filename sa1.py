# If and else
# myAge = int(input("Enter your age"))

# if(myAge > 10):
#     print("Old man")
# elif(myAge > 5):
#     print("child")
# else: 
#     print("You don't have a clue what your are")


#for loops
# myFriendList = [ "Dante", "Homer", "Virgil" ]

# for friend in myFriendList:
#     print(friend)


#while
# count = 5

# while( count >= 0 ):
#     print(count)
#     count = count-1 


#Program to count no. of characters and words in given sentence
inTwoStrings = input("Enter your introduction")
character_count = 0
word_count = 1

for i in inTwoStrings:
    character_count = character_count + 1

    if(i == ' '):
        word_count = word_count + 1

print("Character Count = ", character_count)
print("Word Count = ", word_count)