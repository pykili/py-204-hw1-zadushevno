# your code here
user_input = input()
most_frequent_character = user_input[0]
print(most_frequent_character)
for i in user_input:
    if user_input.count(i) > user_input.count(most_frequent_character):
        most_frequent_character = i
print(most_frequent_character)
