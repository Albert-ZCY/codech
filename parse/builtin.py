import re

try:
    file = open('../core/grammar/builtin', 'r')
except:
    file = open('core/grammar/builtin', 'r')
builtin = eval(file.read())
file.close()

def parseBuiltin(code):
    for item in builtin:
        code = re.sub(item, builtin[item], code)
    return code