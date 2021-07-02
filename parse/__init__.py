from .core import *

if __name__ == '__main__':
    main = Interpreter("""
定义 函数 打印（*参数）：
\t循环（10）：
\t\t输出（*参数）
打印（‘文本’，1，真）""")
    main.run()