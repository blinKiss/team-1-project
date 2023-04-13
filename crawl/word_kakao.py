from hanspell import spell_checker
import re
 
eng = '[A-Za-z]'
kor = '[가-힣]+'
received = '알리제는french아이유는korean알리샤는미쿡가수'

if re.search(eng, received):
    print('나는 편식쟁이 한글만 먹지')
    k = re.findall(kor, received)
    k2 = ''.join(k)
    sentence = spell_checker.check(k2).checked
    words = sentence.split()
    print(words)

    
    
    
else:
    print('한글마시따')
    sentence = spell_checker.check(received).checked
    # print(sentence)
    words = sentence.split()
    print(words)
