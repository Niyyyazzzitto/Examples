import re
def ex1(s): 
    return bool(re.fullmatch(r"ab*", s))

import re
def ex2(s): 
    return bool(re.fullmatch(r"ab{2,3}", s))

import re
def ex3(text): 
    return re.findall(r"[a-z]+_[a-z]+", text)

import re
def ex4(text): 
    return re.findall(r"[A-Z][a-z]+", text)

import re
def ex5(s): 
    return bool(re.search(r"a.*b$", s))

import re
def ex6(text): 
    return re.sub(r"[ ,.]", ":", text)

import re
def ex7(s):
    return re.sub(r"_([a-zA-Z])", lambda m: m.group(1).upper(), s)

import re
def ex8(s): 
    return re.split(r"(?=[A-Z])", s)

import re
def ex9(s): 
    return re.sub(r"(?<!^)(?=[A-Z])", " ", s)

import re
def ex10(s):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", s).lower()
