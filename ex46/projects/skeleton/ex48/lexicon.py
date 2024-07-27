userInput = raw_input(' >')
tokens = userInput.split()

lexicon = {
        'north': 'direction',
        'south': 'direction',
        'east': 'direction',
        'west': 'direction',
        'go': 'verb',
        'kill': 'verb',
        'eat': 'verb',
        'the': 'stop',
        'in': 'stop',
        'of': 'stop',
        'bear': 'noun',
        'princess': 'noun',
        '3': 'number',
        '1234': 'number',
        '91234': 'number',
        'IAS': 'error',
        'ASDFADFASDF': 'error',
        }



def scan(sentence):
        words = sentence.split()
        result = []

        for word in words:
            if word in lexicon:
                token = lexicon[word]
            else:
                token = 'error'
            result.append((token, word))

        return result

# the scan function should work by "scanning" the word given (ex: "north") and deciding what type of word it is (ex: direction)
