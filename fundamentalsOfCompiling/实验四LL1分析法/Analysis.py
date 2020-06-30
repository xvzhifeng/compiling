"""
    @Author:sumu
    @Date:2020-06-07 19:00
    @Email:xvzhifeng@126.com
"""


from prettytable import PrettyTable

#输出分析表的表头
table = PrettyTable(["Steps", "Stack", "Input_a_now", "Remain_str", "Use_production"])

'''
 文法：
    E->TG
    G->+TG|—TG|ε
    T->FS
    S->*FS|/FS|ε
    F->(E)|i
 非终结符：
    E，G，T，S，F
 终结符:
    i,+,*,(,),-,/
'''

# 根据上面文法构造预测分析表
dicts = {('E', 'i'): 'TG', ('E', '('): 'TG',
         ('G', ')'): 'ε', ('G', '—'): '—TG', ('G', '#'): 'ε', ('G', '+'): '+TG',
         ('T', 'i'): 'FS', ('T', '('): 'FS',
         ('S', ')'): 'ε', ('S', '—'): 'ε', ('S', '/'): '/FS', ('S', '#'): 'ε', ('S', '+'): 'ε', ('S', '*'): '*FS',
         ('F', 'i'): 'i', ('F', '('): '(E)'
         }


#文法开始符
StartSym = 'E'

# 构造终结符集合
Vt = ('i', '+', '*', '(', ')','/','-')

# 构造非终结符集合
Vn = ('E', 'G', 'T', 'S', 'F')

# 获取输入栈中的内容
def Showstack(stack):
    ss = ''
    for i in stack:
        ss += i
    return ss

# 得到输入串剩余串
def Showstr(str, index):
    ss = ''
    for i in range(index, len(str)):
        ss += str[i]
    return ss

# 定义error函数
def error():
    print('Error')
    exit()

def error1(d):
    print("在分析表中位置",d,"为空所以出现错误！")
    exit()


# 分析程序
def Analysis(str,StartSym,table,dicts,Vt,Vn):
    '''
    总控程序，用于进程文法的判断
    '''

    stack = []  # 用列表模拟栈
    location = 0  # 当前位置
    str = '#' + str + '#'  # 输入串

    stack.append(str[location])  # 将#号入栈

    stack.append(StartSym)  # 将文法开始符入栈

    location += 1
    a = str[location]  # 将输入串第一个字符读进a中

    flag = True  # 分析结束标志
    count = 1  # 计算步骤

    #print(dicts)
    while flag:
        # 建表
       # print(dicts)
        if count == 1:      #文法开始
            temp = StartSym + '->' + dicts[(StartSym, a)]
            table.add_row([count, Showstack(stack), a, Showstr(str, location), temp])
        else:
            if stack[-1] in Vt:     #栈顶是终结符,所用产生式为空，即下一步的栈顶直接弹出
                table.add_row([count, Showstack(stack), a, Showstr(str, location), ''])
            elif stack[-1] in Vn:   #栈顶是非终结符，所用产生式为 M[x,a]
                if dicts[(stack[-1], a)] == " ":
                    error1((stack[-1], a))
                temp = stack[-1] + '->' + dicts[(stack[-1], a)]
                table.add_row([count, Showstack(stack), a, Showstr(str, location), temp])
            else:                   # 栈顶是结束符‘#’，分析成功
                table.add_row([count, Showstack(stack), a, Showstr(str, location), "Success!"])

        x = stack.pop()  # x为栈顶元素
        if x in Vt:  # 栈顶是终结符
            if x == str[location]:  # 该字符匹配，输入串向后挪一位
                location += 1
                a = str[location]
            else:  # 否则错误
                error()
        elif x == '#':  # 栈顶是结束符
            if x == a:  # 当前输入字符也是结束符，分析结束
                flag = False
            else:  # 否则错误
                error()
        elif (x, a) in dicts.keys():  # M[x,a]是产生式
            s = dicts[(x, a)]
            for i in range(len(s) - 1, -1, -1):  # 倒序入栈
                if s[i] != 'ε':
                    stack.append(s[i])
        else:
            error()
        count += 1


def ShowTable():
    # 表左对齐
    table.align['步骤'] = 'l'
    table.align['分析栈'] = 'l'
    table.align['剩余输入串'] = 'l'
    table.align['所用产生式'] = 'l'
    table.align['当前输入a'] = 'l'
    # 输出语法分析表
    print(table)

if __name__ == '__main__':
    str = input('>>>')
    # for i in str:
    #     if i not in Vt:
    #         exit("存在字符在文法里不存在！！！")
    Analysis(str,StartSym,table,dicts,Vt,Vn)
    ShowTable()     #表格输出结果分析结果

