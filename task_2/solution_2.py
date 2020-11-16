# your code here
user_input = input()
most_frequent_character = user_input[0]
frequency = 0
for smth in user_input:
    if smth == most_frequent_character:
        frequency = frequency + 1      
for i in user_input:
    count = 0
    frequency = 0
    symbol = i
    for smth in user_input:
        if smth == symbol:
            count = count + 1
    for smth in user_input:
        if smth == most_frequent_character:
            frequency = frequency + 1
    if count > frequency:
        most_frequent_character = i
print(most_frequent_character)
