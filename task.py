# TODO:
# Write an application that reverses all the words of input text:
# Example "abcd efgh" => "dcba hgfe"

# All non-letter symbols should stay on the same places:

# Example "a1bcd efg!h" => "d1cba hgf!e"
# Use Latin alphabet for test only.

# You should write a function which returns reverse text
# Your script should print function result

# Hint
# Use statement "if __name__ == '__main__':" as wrapper for printing result of function.
# Test strings should be declared in statement "if __name__ == '__main__':"
# And call function should also be here.


def reverse_word(word):
    """Reverse all word of input text and return it""" 

    word_lengh = len(word)
    half_word_index = word_lengh / 2

    word = list(word)
    index = 0
    last_index = word_lengh-1

    while index < half_word_index:
        current_item = word[index]
        last_item = word[last_index]

        if not current_item.isalpha():
            index += 1
        elif not last_item.isalpha():
            last_index -=1
        else:
            word[index], word[last_index] = last_item, current_item

            index += 1
            last_index -=1

    return word
        



def anagram(sentence):
    """Return the reversed sentence"""       

    words_reversed = []
    words = sentence.rsplit(" ")
    result = ""
    
    for word in words:        
        words_reversed.append(reverse_word(word))        

    # result = " ".join(words_reversed)

    for item in words_reversed:                  
        for char in item:
            result += char             
        result += " "           

    return result        

print(anagram("a1bcd efg!h"))       
           
