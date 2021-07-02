import re

try:
    file = open('../core/grammar/symbol', 'r')
except:
    file = open('core/grammar/symbol', 'r')
symbol = eval(file.read())
file.close()

def parseSymbol(code):
    for item in symbol:
        code = re.sub(item, symbol[item], code)
    return code