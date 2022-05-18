import string

sentence = "This is another test"

def spin_words(sentence):
    sen = list(sentence)
    if len(sen) >= 1:
        c = ''
        res = sentence.split(' ')
        for i in res:
            if len(i) >= 5:
                y = list(reversed(i))

                x = '' 
                for i in y:
                    x += i

                c = c + x + ' '
                
            else:
                c = c+i+' '
                # print('xxxxxx'+i)
    else:
        c = list(reversed(len[0]))
        
    return c

n = spin_words(sentence)
print(n)