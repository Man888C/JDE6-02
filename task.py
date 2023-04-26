import random

text = './news.txt'
f = open(text, "r")
print(f.readlines())


def hammer_pickOneMemeber():
    '''example function'''

    teamJDE = ['hammer', 'billy', 'chistina']
    result = random.sample(teamJDE, 1)
    return result


if __name__ == "__main__":
    print(hammer_pickOneMemeber())
    # print(taskOne())
    # print(taskTwo())
    # print(taskThree())
    # print(taskFour())

    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
           
        def taskOne(text):
        
        detectList = ['a', 'e', 'i', 'o' 'u']
        counter = 0
        for char in text:
            if char in detectList:
                counter += 1
        return counter
    
    if __name__ == "__main__":

        with open(text, 'r') as ff:
            content = ff.read()
            print (content)

            print(taskOne(content))
            
    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I
    
    def reverse_slicing(s):
        return s[::-1]

    input_str = 'I am a boy'

    if __name__ == "__main__":
        print('Reverse String using slicing =', reverse_slicing(input_str))

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
