import requests
import random


def main(): 
    levels = []
    while len(levels)<3:
        levels.append(input("Choose difficulty:1-12:"))
        if len(levels) <3:
            answer = input("Do you want to add another level(up to 3 levels)? y/n: ")
        if answer =='n':
            break
    words,fakes = load(levels)
    words_list = []
    for word in words:
        definitions, examples, synonyms, antonyms = lookup(word)
        w = Word(word=word,definitions=definitions,examples=examples,synonyms=synonyms,antonyms=antonyms)
        words_list.append(w)
    score=0
    for w in words_list:
        print(f'Definition:{w.get_definition()}')
        
        
        candidates = w.get_fakes(fakes) +[w.word]
        
        random.shuffle(candidates)
        for i in candidates:
            print(i,end=' ')
        print('\n')
        answer = input("Which is the word?: " )
        if answer == w.word:
            print("Correct!!")
            score+=1
        else:
            print("incorrect")
        print('\n')
    print(f"Your Score was {score}")
    print("Thank you for playing!!")
    

# levels is lists
def get_wordlist(levels): 
    words,fakes = load(levels)
    words_list = []
    for word in words:
        definitions, examples, synonyms, antonyms = lookup(word)
        w = Word(word=word,definitions=definitions,examples=examples,synonyms=synonyms,antonyms=antonyms)
        quiz = w.get_fakes(fakes)
        quiz.append(word)
        random.shuffle(quiz)
        words_list.append({'word':word,'definition':w.get_definition(),'example':w.get_example(),'synonym':w.synonyms,'antonym':w.antonyms,'quiz':quiz})
    return words_list



# choose word from word file
def load(levels):
    words = []
    file_dict ={'1':'1stgrade.txt','2':'2ndgrade.txt','3':'3rdgrade.txt','4':'4thgrade.txt',
    '5':'5thgrade.txt','6':'6thgrade.txt','7':'7thgrade.txt','8':'8thgrade.txt',
    '9':'9thgrade.txt','10':'10thgrade.txt','11':'11thgrade.txt','12':'12thgrade.txt'}
    for level in levels:
        with open(f'quiz/word_game/word_list/{file_dict[level]}','r',encoding='utf-8',errors='ignore') as f:
             for word in f.read().splitlines():
                  words.append(word)
    #  get random ten words
    answers = random.sample(words,10)
    fakes = words.copy()
    for w in answers:
             fakes.remove(w)

    return answers,fakes


# lookup word from the api

def lookup(word):
    response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}').json()
    definitions = []
    examples = []
    synonyms = []
    antonyms = []
    for i in response[0]['meanings']:
        definitions.append(i['definitions'][0]['definition'])
        if 'example' in i['definitions'][0]:
            examples.append(i['definitions'][0]['example'])
        for syn in i['synonyms']:
            if syn !="":
                synonyms.append(syn)
            
        for ant in i['antonyms']:
                antonyms.append(ant)    
    return definitions, examples, synonyms, antonyms
   

# to keep data 
class Word():
    def __init__(self,word,definitions,examples,synonyms,antonyms):
        self.word = word
        self.definitions= definitions
        self.examples = examples
        self.synonyms = synonyms
        self.antonyms = antonyms 
    
    def __str__(self):
        return f'{self.word} quiz'
    def get_example(self):
        if len(self.examples)>0:
            return random.choice(self.examples)
    def get_definition(self):
        if len(self.definitions)>0:
            return random.choice(self.definitions)
    
    def get_synonym(self):
        if len(self.synonyms)>0:
            return random.choice(self.synonyms)
    def get_antonym(self):
        if len(self.antonyms)>0:
            return random.choice(self.antonyms)
    def get_fakes(self,ls):
          return random.sample(ls,3)

if __name__ == '__main__':
    main()