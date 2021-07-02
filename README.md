# 最新特性	
- 标点智能转换：-将中文符号转化为英文符号-，再也不用在两套输入法之间来回切换。	
- 语法补充	
- 内置函数补充	
# 语法	
- 包含python的-全部语法-，例如：	
1. 条件判断（if...elif...else）	
```python
数字 = 1
如果 数字 > 0: # 或 -> 如果 数字 > 0 那么
    输出（数字）
否则 如果 数字 < 0: # 或 -> 否则如果 数字 > 0 那么
    输出（-数字）
否则：
    输出（0）
```
2. 函数 （def）	
```python
定义 函数 Hello（名字）:
    输出（“HelloWorld”+名字）
```
3. 循环、遍历 （for/while）	
```python
以 i 遍历 [1，2，3，4]：
    输出（i）

循环（5）：
    输出（‘\a’）

a = 1
当 a > 1 循环：
    a -= 1
```
- 全部语法可在/core/grammar/syntax中查看（以正则格式）	
# 编译
cmd输入以下语句：
```python
::只运行：debug
 项目文件夹/codech -f debug .cc文件路径
::只编译：compile 
项目文件夹/codech -f compile .cc文件路径 
::运行+编译：run 
项目文件夹/codech -f run .cc文件路径
``` 