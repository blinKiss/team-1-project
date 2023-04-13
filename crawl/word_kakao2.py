# import nltk
# nltk.download('punkt')

# from nltk.tokenize import word_tokenize

# text = "dontgolookatmewithoutlookinyouteyes"
# words = word_tokenize(text)
# spaced_text = " ".join(words)
# print(spaced_text)


# import re

# text = "dontgolookatmewithoutlookinyoureyes"
# pattern = r"(?<!^)(?=[A-Z])"
# splitted_text = re.sub(pattern, " ", text)

# print(splitted_text)

# import nltk
# nltk.download('punkt')

# from nltk.tokenize import word_tokenize

# text = "dontgolookatmewithoutlookinyoureyes"
# words = word_tokenize(text)
# spaced_text = " ".join(words)
# print(spaced_text)

import pyphen

text = "iamnotagirlnotyetawoman"
dic = pyphen.Pyphen(lang='en')

# 단어 분리
words = dic.inserted(text).split("-")
print(words)