import re
import json

def removeComment(code):
    result = re.sub('#(.*)', '', code)
    return result

def parseTrue(code):
    result = re.sub('真', 'True', code)
    return result

def parseFalse(code):
    result = re.sub('假', 'False', code)
    return result

def parseNone(code):
    result = re.sub('无', 'None', code)
    return result

def parseIf(code):
    temp = re.sub('如果', 'if', code)
    result = re.sub(' 那么', '', temp)
    return result

def parseElseIf(code):
    temp = re.sub('否则', 'elif', code)
    result = re.sub('如果', '', temp)
    return result

def parseElse(code):
    result = re.sub('否则', 'else', code)
    return result

def parseAnd(code):
    result = re.sub('且', 'and', code)
    return result

def parseOr(code):
    result = re.sub('或', 'or', code)
    return result

def parseFunction(code):
    temp = re.sub('定义', 'def', code)
    result = re.sub(' 函数', '', temp)
    return result

def parseReturn(code):
    result = re.sub('返回', 'return', code)
    return result

def parseClass(code):
    temp = re.sub('定义', 'class', code)
    result = re.sub(' 类', '', temp)
    return result

def parsePass(code):
    result = re.sub('略', 'pass', code)
    return result

def parseGlobal(code):
    result = re.sub('全局化', 'global', code)
    return result

def parseLoop(code):
    result = re.sub('循环', 'for _ in range', code)
    return result

def parseForEach(code):
    index = re.match('以 (.*) 遍历', code).replace('以 ', '').replace(' 遍历', '')
    obj = re.match('遍历 (.*)', code).replace('遍历 ', '')
    result = re.sub('以 (.*) 遍历 (.*)', f'for {obj} in {index}', code)
    return result

def parseWhile(code):
    temp = re.sub('当', 'while', code)
    result = re.sub(' 循环', '', temp)
    return result

def parseContinue(code):
    result = re.sub('跳过', 'continue', code)
    return result

def parseBreak(code):
    result = re.sub('跳出', 'break', code)
    return result

def parseImport(code):
    temp = re.sub('从', 'from', code)
    result = re.sub('导入', 'import', temp)
    return result


try:
    file = open('../core/grammar/syntax', 'r')
except:
    file = open('core/grammar/syntax', 'r')
syntax = eval(file.read())
file.close()