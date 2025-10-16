def longestWord(word):
    max_length = len(word_list[0])
    for item in word_list:
        length = len(item)
        if length > max_length:
            max_length = length
    return max_length
words = input("Enter a list of words separated by spaces: ")
word_list = words.split()
result = longestWord(word_list)
print(f"The length of the longest word is: {result}")
