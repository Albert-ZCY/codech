import json
import re
from .syntax import *
from .builtin import *
from .symbol import *


class Interpreter():
    def __init__(self, content):
        self.content = content
        self.parse()

    def parse(self):
        self.parseSymbol()
        self.parseSyntax()
        self.parseBuiltin()
        return self.content

    def parseSymbol(self):
        self.content = parseSymbol(self.content)

    def parseSyntax(self):
        self.content = removeComment(self.content)
        self.lines = self.content.split('\n')
        self.keywords = syntax.keys()
        for i in range(len(self.lines)):
            line = self.lines[i]
            for keyword in self.keywords:
                exist = re.findall(re.compile(keyword), line)
                if exist:
                    line = syntax[keyword](line)
                    self.lines[i] = line
        self.content = '\n'.join(self.lines)

    def parseBuiltin(self):
        self.content = parseBuiltin(self.content)
    
    def run(self):
        exec(self.content)