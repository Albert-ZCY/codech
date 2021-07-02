import sys
import os
from parse import *

class Config():
    def __init__(self, argv):
        self.argv = argv[1:]
        self.parseCommand()

    def parseCommand(self):
        self.allowedExt = ['.cc',]
        self.com = []
        self.arg = []
        for item in self.argv:
            if item.startswith('-'):
                self.arg.append(item)
            else:
                self.com.append(item)
        if len(self.com) >= 2:
            if '-c' in self.arg:
                self.content = self.com[1]
                self.call()
            else:
                self.opath = self.com[1]
                ext = os.path.splitext(self.opath)[-1]
                if ext in self.allowedExt:
                    ofile = open(self.opath, 'r')
                    self.content = ofile.read()
                    ofile.close()
                    self.call()
                else:
                    self.quit('Not an allowed file. All files should be ".cc" files.')
        else:
            self.quit('Not enough commands. Example: "codech run -f test.cc".')

    def call(self):
        inp = Interpreter(self.content)
        self.code = inp.parse()
        if self.com[0] == 'debug':
            inp.run()
        elif self.com[0] == 'compile':
            self.compile()
        elif self.com[0] == 'run':
            self.compile()
            inp.run()
        else:
            self.quit('Not an allowed command')
        
    def compile(self):
        self.spath = self.opath.replace('.cc', '.py')
        sfile = open(self.spath, 'w')
        sfile.write(self.code)
        sfile.close()

    def quit(self, info):
        print('fatal: '+info)
        sys.exit(0)


if __name__ == '__main__':
    main = Config(sys.argv)
