# your code goes here!

class Anagram:

    def __init__(self, word = '') -> None:
        self.word = word
        


    def match(self, word_list):
        match_list = []
        for word in word_list:
            if sorted(word) == sorted(self.word):
                match_list.append(word)
        return match_list
                


print(Anagram("enlist").match)

