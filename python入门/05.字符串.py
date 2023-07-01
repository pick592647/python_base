# 字符串(str)
# 字符串用来表示一段文本信息，字符串是程序中使用的最多的数据类型
# 在Python中字符串需要使用引号引起来

s = 'hello'
# s = abc # 字符串必须使用引号引起来，不使用不是字符串
# 引号可以是双引号，也可以是单引号，但是注意不要混着用
s = 'hello'
s = "hello"
# s = 'hello" 引号不能混合使用  SyntaxError: EOL while scanning string literal

# 相同的引号之间不能嵌套
# s = "子曰:"学而时习之，乐呵乐呵！""
s = '子曰:"学而时习之，乐呵乐呵！"'

# 长字符串
# 单引号和双引号不能跨行使用
s = '锄禾日当午，\
汗滴禾下土，\
谁知盘中餐，\
粒粒皆辛苦'

# 使用三重引号来表示一个长字符串 ''' """
# 三重引号可以换行，并且会保留字符串中的格式

s = '''锄禾日当午，
汗滴禾下土，
谁知盘中餐，
粒粒皆辛苦'''

# 转义字符
# 可以使用 \ 作为转义字符，通过转义字符，可以在字符串中使用一些特殊的内容
# 例子：
#   \' 表示'
#   \" 表示"
#   \t 表示制表符
#   \n 表示换行符
#   \\ 表示反斜杠
#   \uxxxx 表示Unicode编码
s = "子曰:\"学而时习之，\\\\n乐呵乐呵！\""

s = '\u2250'
# 可以使用unicode来打印各种不同的特殊符号！！
print(s)