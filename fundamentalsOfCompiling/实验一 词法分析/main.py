"""
    @Author:sumu
    @Date:2020-06-06 20:25
    @Email:xvzhifeng@126.com

"""


"""
功能：
类C/C++语言单词识别
1.识别保留字：if、int、for、while、do、return、break、continue等等；
保留字类别码为1。
2.其他的都识别为标识符；单词类别码为2。
3.常数为无符号整形数；单词类别码为3。
4.运算符包括：+、-、*、/、=、>、<、>=、<=、!= ；类别码为4。
5.分隔符包括：,、;、{、}、(、)； 类别码为5。
6.错误字符 类别码为 6。
以上为参考，具体可自行增删

"""
import re
keyword = {'main':1, 'int':1, 'char':1, 'if':1, 'else':1, 'for':1, 'while':1,'return':1,'void':1,'break':1,'continue':1,
           'auto':1, 'register':1, 'extern':1, 'static':1,"double":1,'float':1}



Symbol = {'=': 4, '+': 4, '-': 4, '*': 4, '/': 4, '(': 5, ')': 5, '[': 5, ']': 5, '{': 5,
          '}': 5, ',': 5, ':': 5, ';': 5, '>': 4, '<': 4, '>=': 4, '<=': 4, '==': 4, '!=': 4}

#总正则表达式
all=re.compile('([0-9]+[a-z|A-Z|_]+[0-9]*|\d+\.\d+[eE][-+]?\d+|\d+\.\d+|[1-9]\d*|0[0-7]+|0x[0-9a-fA-F]+|\*/|'+
               '[a-z|A-Z|0-9|_]*\".*?\"[a-z|A-Z|0-9|_]*|[a-zA-Z_]\w*|\".*\"|>>|<<|'
               '::|->|\+=|\-=|\*=|/=|%=|>=|<=|==|!=|&&|\+|\||\-|\*|//|/\*|=|>|'
               '<|!|\^|%|\~|\?|:|,|;|\(|\)|\[|\]|\{|\}|\"|\'|/)')

ne = re.compile('\d+\.\d+[eE][-+]?\d+|\d+\.\d+|[1-9]\d*|0[0-7]+|0x[0-9a-fA-F]+')

nflag = 0


def Judge(s):
    if s[0].isalpha() and s in keyword:         #判断关键字
        print('( ',keyword[s],',',s,' )')
    elif s[0].isalpha() and s not in keyword and s.isalnum():     #判断标识符
        print('( ', 2,',',s, ' )')
    elif s.isdigit() or ne.findall(s):#判断数字
        print('( ', 3, ',', s, ' )')
    elif s in Symbol:                           #判断运算符或边界符
        print('( ', Symbol[s], ',', s, ' )')

    else:

        if len(s) >= 2 and s[0] == '"' and s[-1] == '"':    #判断字符串
            print('( ',"字符串", ',', s, ' )')
        elif ne.findall(s):
            print('( ', 3,',',s, ' )')
        else:                                   #没定义或者错误串
            print('( ','错误字符或暂未定义',',',s,' )')

def Judge1(s1,s2,s3,i):

    if s1.isdigit() or ne.findall(s1) or s1[0].isalpha() and s1 not in keyword and s1.isalnum():#判断数字
        print('( ', Symbol[s2], ',', s2, ' )')
        return False
    else:
        print('( ', 3, ',', s2+s3, ' )')
        return True

if __name__ == '__main__':
    #读取文件
    f = open('data/data2.txt', 'r')
    result = []
    flag = False
    # 取出每一个单词并且去除注释
    for line in f:
        if len(line) == 1:
            result.extend(line)
        else:
            if len(all.findall(line)) != 0:
                if all.findall(line)[0] == '//' :
                    pass
                else:
                    if line.__contains__('//'):
                        for i in all.findall(line):
                            if i != '//':
                                result.append(i)
                            else:
                                break
                    elif line.__contains__('/*') or flag:
                        print(all.findall(line))
                        for i in all.findall(line):
                            if i != '/*' and flag == False:
                                result.append(i)
                                #print(i)
                            elif i=='/*':
                                flag =True
                            elif i == '*/':
                                flag = False
                    else:
                        result.extend(all.findall(line))
    print(result)
    # 去掉列表中残留的空字符
    for i in result:
        if '' in result:
            result.remove('')
    flag = False
    #词法分析
    for i in range(len(result)):

        if result[i] == '-':
            flag=Judge1(result[i-1],result[i],result[i+1],i)
        elif flag == True:
            flag = False
        else:
            Judge(result[i])






# import re
# all=re.compile('([0-9]+[a-z|A-Z|_]+|\d+\.\d+[eE][-+]?\d+|\d+\.\d+|[1-9]\d*|0[0-7]+|0x[0-9a-fA-F]+|'
#                '[a-z|A-Z|0-9|_]*\".*\"[a-z|A-Z|0-9|_]*|[a-zA-Z_]\w*|\".*\"|>>|<<|'
#                '::|->|\+=|\-=|\*=|/=|%=|>=|<=|==|!=|&&|\|\||\+|\-|\*|/|=|>|'
#                '<|!|^|%|~|\?|:|,|;|\(|\)|\[|\]|\{|\}|\"|\')')
#
# ss = 'int main(){ int a = 1;"}'
# list = []
# f = open('E://test.txt','r')
# for line in f:
#     if len(line) == 1:
#         list.extend(line)
#     else:
#         list.extend(all.findall(line))
# print(list)
