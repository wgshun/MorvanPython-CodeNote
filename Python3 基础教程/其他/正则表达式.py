# 正则表达式 (Regular Expression) 又称 RegEx, 是用来匹配字符的一种工具。
# 通过正则表达式可以更方便的从大量复杂的字符串中获取自己想要的东西。
# reg exp.png 为各种正则表达式总结，出自：https://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html

# 最简单的字符匹配
# 比如 从 a reg exp d 里面匹配出 reg
str1 = 'reg'
str2 = 'regu'
string = 'a reg exp d'
print(str1 in string) # 返回 True
print(str2 in string) # 返回 False
# 使用 python 的正则表达式模块进行上述操作
import re
str1 = 'reg'
str2 = 'regu'
string = 'a reg exp d'
print(re.search(str1, string)) # 存在就返回一个object类并表明字符所在位置
print(re.search(str2, string)) # 不存在则返回 None

# 更多复杂匹配方式
# 使用[]框起来，如下，在匹配的时候就匹配 reg 或 rag，相当于匹配一个列表中的元素
str1 = 'r[ea]g'
string = 'a reg exp d'
print(re.search(str1, string)) # <_sre.SRE_Match object; span=(2, 5), match='reg'>
print(re.search(str1, 'a rg exp d')) # None
# 使用[]框起来的也可以是一个区间，比如[a-z]指从a到z的所有小写字母,[A-Z].[1-9],[0-9a-z]指0到9和a到z都包括
str1 = 'r[a-z]g'
str2 = 'r[0-9]g'
str3 = 'r[A-Z]g'
str4 = 'r[0-9a-z]g'
string = 'a reg exp d'
print(re.search(str1, string))# <_sre.SRE_Match object; span=(2, 5), match='reg'>
print(re.search(str2, string))# None
print(re.search(str3, string))# None
print(re.search(str4, string))# <_sre.SRE_Match object; span=(2, 5), match='reg'>

# 按一些既定的规则去匹配
# \d: 任何数字
print(re.search(r"r\dg", 'r6g')) # <_sre.SRE_Match object; span=(0, 3), match='r6g'>
print(re.search(r"r\dg", 'reg')) # None
# \D: 任何非数字
print(re.search(r"r\Dg", 'r6g')) # None
print(re.search(r"r\Dg", 'reg')) # <_sre.SRE_Match object; span=(0, 3), match='reg'>
# \s: 任何像 \n\t 的空格系列
print(re.search(r"r\sg", 'r\tg')) # <_sre.SRE_Match object; span=(0, 3), match='r\tg'>
print(re.search(r"r\sg", 'reg')) # None
# \S: 任何非空格系列
print(re.search(r"r\Sg", 'r\tg')) # None
print(re.search(r"r\Sg", 'reg')) # <_sre.SRE_Match object; span=(0, 3), match='reg'>
# \w: 任何大小写字母和数字
print(re.search(r"r\wg", 'r!g reg')) # <_sre.SRE_Match object; span=(0, 3), match='reg'>
print(re.search(r"r\wg", 'r!g')) # None
# \W: 任何非大小写字母和数字
print(re.search(r"r\Wg", 'reg')) # None
print(re.search(r"r\Wg", 'r!g')) # <_sre.SRE_Match object; span=(0, 3), match='r!g'>
# \b: 如下:表示 reg 的前后是否是字母和数字
print(re.search(r"\breg\b", 'reg'))# 不是 <_sre.SRE_Match object; span=(0, 3), match='reg'>
print(re.search(r"\breg\b", '1reg'))# 是 None
# \B: 如下:表示 reg 的前后是否是非字母非数字
print(re.search(r"\Breg\B", 'reg')) # 是 None
print(re.search(r"\Breg\B", '1reg1')) # 不是 <_sre.SRE_Match object; span=(1, 4), match='reg'>
# \\:匹配\符号在字符串中后面无字母或数字
# \符号在字符串中后面有字母或数字匹配同字母数字
print(re.search(r'\\re', '\re')) # None
print(re.search(r'\re', '\re')) # <_sre.SRE_Match object; span=(0, 3), match='\re'>
print(re.search(r"re1\\", "re1\ "))# <_sre.SRE_Match object; span=(0, 4), match='re1\\'>
print(re.search(r"re1\\", "re1\1"))# None
# . : 可以匹配任何字符,除了 \n
print(re.search(r'r.g', 'r~g'))# <_sre.SRE_Match object; span=(0, 3), match='r~g'>
print(re.search(r'r.g', 'reg'))# <_sre.SRE_Match object; span=(0, 3), match='reg'>
print(re.search(r'r.g', 'r\ng'))# None
# ^ : 匹配字符串的开头
print(re.search(r'^reg', 'reg if '))# <_sre.SRE_Match object; span=(0, 3), match='reg'>
print(re.search(r'^reg', '1 reg if '))# None
# 如果一个多行的字符串匹配非第一行开头的时候
string = '''
reg if.
exp id.
'''
print(re.search(r'^exp', string))# None
print(re.search(r'^exp', string, flags=re.M))# <_sre.SRE_Match object; span=(9, 12), match='exp'>
# $: 匹配字符串的结尾
print(re.search(r'reg$', 'if reg'))# <_sre.SRE_Match object; span=(3, 6), match='reg'>
print(re.search(r'reg$', 'if reg 0'))# None
# ()?: ?前面括号里的可有可无
print(re.search(r'reg(ular)?', 'regular')) # <_sre.SRE_Match object; span=(0, 7), match='regular'>
print(re.search(r'reg(ular)?', 'reg'))# <_sre.SRE_Match object; span=(0, 3), match='reg'>

# 匹配重复使用
# * ：重复零次或多次
print(re.search(r'sb*', 's')) # <_sre.SRE_Match object; span=(0, 2), match='sb'>
print(re.search(r'sb*', 'sbbbbb'))# <_sre.SRE_Match object; span=(0, 6), match='sbbbbb'>
# + : 重复一次或多次
print(re.search(r'sb+', 's')) # None
print(re.search(r'sb+', 'sbbbbbb'))# <_sre.SRE_Match object; span=(0, 7), match='sbbbbbb'>
# {n, m}: 重复n到m次 {n}是重复n次
print(re.search(r'sb{1,3}','s')) # None
print(re.search(r'sb{1,3}','sb')) # <_sre.SRE_Match object; span=(0, 2), match='sb'>
# 通过() 给找到的字符串内容分组
gr = re.search(r'(\d+),Data:(.+)', 'ID:12312,Data:Feb/19/2019')
print(gr.group(1)) # 12312
# 通过?P(name)给分的组命名
gr = re.search(r'(?P<id>\d+),Data:(?P<data>.+)', 'ID:12312,Data:Feb/19/2019')
print(gr.group('data')) # Feb/19/2019

## 以上的re.search均是匹配上的第一项，使用findall输出所有的匹配项
print(re.findall(r'r.g', 'reg r1g'))# ['reg', 'r1g']
# | 是 or 的意思
print(re.findall(r'reg|r1g', 'reg r1g r2g'))# ['reg', 'r1g']

# replace正则替换使用re.sub()
print(re.sub('r[ea]g', 'rrr', 'eee reg ggg')) # eee rrr ggg

# split 字符串分割更为方便
print(re.split(r'[,./]', 'r,e.g,e.x/p'))# ['r', 'e', 'g', 'e', 'x', 'p']

# compile 编译后的正则,先经过编译然后直接进行正则操作
compile_re = re.compile(r'r[ea]g')
print(compile_re.search('reg r'))# <_sre.SRE_Match object; span=(0, 3), match='reg'>