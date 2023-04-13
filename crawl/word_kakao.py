from hanspell import spell_checker
import re

eng = '[A-Za-z]'
kor = '[가-힣]+'
received = 'dontgolook'

if re.search(eng, received):
    print('영어가 있으면 여기')
    k = re.findall(kor, received)
    k2 = ''.join(k)
    e = re.findall(eng, received)
    e2 = ''.join(e)
    sentence = spell_checker.check(k2).checked
    words = sentence.split()
    # print(words)
    sentence2 = spell_checker.check(e2).checked
    words2 = sentence2.split()
    words.extend(words2)
    print(words)


else:
    print('한글만')
    sentence = spell_checker.check(received).checked
    words = sentence.split()
    print(words)
