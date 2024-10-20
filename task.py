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
    """Reverse all alphabetic word of input text and return it"""

    only_alphabetic = []    

    for char in word:
            if char.isalpha():
                only_alphabetic.append(char)

    reversed_word_without_special_char = list(reversed(only_alphabetic))

    return reversed_word_without_special_char  



def anagram(sentence):
    """Return the reversed sentence""" 

    words = sentence.rsplit(" ")    
    reversed_sentence = []
    words_count = 0

    for word in words:
        words_count +=1
        reversed_chars = reverse_word(word)         

        for  item in word:
            if item.isalpha():                
                replace_with = reversed_chars.pop(0)
                reversed_sentence.append(replace_with)
            else:
                reversed_sentence.append(item)

        if len(words) != words_count:
            reversed_sentence.append(" ")

        result = "".join(reversed_sentence)

    return result


if __name__ == "__main__":
    test_1 = "a1bcd e3fg!h"
    test_2 = "abcd efgh"
    print(anagram(test_2))
    print(anagram(test_1))


