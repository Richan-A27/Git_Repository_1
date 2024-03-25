#Write a Python program to get a single string from two given strings,separated by a space, and swap the first characters of each string.

S1=input("Enter a string:")
S2=input("Enter an another string:")

def swap_add_string(a,b):
    return b[0]+a[1:] +" "+a[0]+b[1:]
print(swap_add_string(S1,S2))

#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to ‘#’ except the first char itself.

first_chr= S1[0]
new_string= S1.replace(first_chr, "#")
mod_string= S1[0]+new_string[1:]
print(f"The output of the string is {mod_string}")

#Write a Python program to find the second most repeated word in a given string.

def second_repeated_word(a):
    word_count = {}
    words = a.split()
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    
    sorted_dict = dict(sorted(word_count.items(), key=lambda x: x[1], reverse=True))
    repeated_words = list(sorted_dict.keys())
    if len(repeated_words) > 1:
        return repeated_words[1]
    else:
        return "No second most repeated word"

sentence = "the quick brown fox jumps over the lazy dog the quick brown fox real quick"
print("The most repeated word is,",second_repeated_word(sentence))

#Write a Python program to count occurrences of a substring in a string.

def count_substring_occurrences(string, substring):
    return string.count(substring)

string = input("Enter string:")
substring = input("Enter substring:")

occurrences = count_substring_occurrences(string, substring)
print(f"Occurrences of '{substring}' in '{string}': {occurrences}")
