userInput = raw_input(' >') # takes input typed into the shell and stores it into a variable called "userInput"  
tokens = userInput.split() # split up "userInput" into strings delimited by space, then store them into the "tokens" variable

lexicon = { # create dictionary called "lexicon" 
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
        'ASDFADFASDF': 'error', # all of these are taking a word (ex: "north") and pairing it to the corresponding token (ex: "direction")
        } # ending the list



def scan(sentence): # create function called "scan" and parameter "sentence"
        words = sentence.split() # take the "sentence" parameter, and split into strings delimited by space, and put them into the "words" variable
        result = [] # create empty list called "result"

        for word in words: # iterate a for loop with the variable "word" to process each index in the "words" variable
            try: # try this block, and if an error happens, then go to except
                number = int(word) # assign function "int()" to convert all string indices from "lexicon" dictionary into integers, to variable "number"
                result.append(('number', number)) # add tuple containing " 'number' " (string) and "number" (integer) variables in list result
            except ValueError: # if the "ValueError" exception happens, then | if the "number" variable has no integer indices, then
                if word in lexicon: # if index from variable "word" is in "lexicon" dictionary, 
                    token = lexicon[word] #  
                else: # or else, if index is not in "lexicon" dictionary 
                    token = 'error' # assign string "error" to variable "token"
                result.append((token, word)) # add tuple containing "token" and "word" variables in list "result"

        return result # "scan" function outputs "result" list

# the scan function should work by "scanning" the word given (ex: "north") and deciding what type of word it is (ex: direction)
