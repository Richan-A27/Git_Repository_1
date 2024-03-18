#
with open ("Experiment-5b.txt", mode="w") as file:
    print('''To stop, type "EOF"''')
    while True:
        line = input("Enter line: ")
        if (line=="EOF"): 
            break
        file.write(line + "\n")
    
#
def count_upper_lower(filename):
    with open (filename,"r") as file:
        upper,lower = 0,0
        content = file.read()
        for chr in content:
            if chr.isupper():
                upper+=1
            elif chr.islower():
                lower+=1
            else:
                continue
        
def word_search_replace(filename):
    word = input("Enter the word to search:")
    replace_word= input("Enter the word to be replaced with: ")
    with open (filename, "r+" )  as file:
        content=file.read()
        modifie_content= content.replace(word,replace_word)
        file.seek(0)
        file.write(modifie_content)

#
def longest_word(filename):
    with open (filename, "r") as file:
        content = file.read()
        words=content.split()
        longest__word=""
        for word in words:
            if len(word)>len(longest__word):
                longest__word=word

        print(f'''The longest word in the file {filename} is "{longest__word}"''')

longest_word("Experiment-5b.txt")



