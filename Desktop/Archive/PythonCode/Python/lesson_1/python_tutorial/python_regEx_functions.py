"""
import re:
- findall: Returns a list containing all matches: re.findall
- search: Returns a Match object if there is a match anywhere in the string: re.search
- split: Returns a list where the string has been split at each match: re.split
- sub: Replaces one or many matches with a string: re.sub
"""
import re, camelcase

txt = "The rain in Spain"
if __name__ == '__main__':
    x = re.sub("\s", "9", txt, 2)
    print(x)
if __name__ == '__main__':
    x = re.findall("ai", txt)
    print(x)
    y = re.findall("Portugal", txt)
    print(y)
if __name__ == '__main__':
    x = re.search("Spain", txt)
    y = re.search("Portugal", txt)
    print(x)
    print(y)
    c = camelcase.CamelCase()
    txt = "hello world"
    print(c.hump(txt))

