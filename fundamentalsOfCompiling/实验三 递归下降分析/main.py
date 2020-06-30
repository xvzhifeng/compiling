"""
    @Author:sumu
    @Date:2020-06-07 15:22
    @Email:xvzhifeng@126.com

"""


"""
（1）E->TG
（2）G->+TG|—TG
（3）G->ε
（4）T->FS
（5）S->*FS|/FS
（6）S->ε
（7）F->(E)
（8）F->i
"""
sym = ""

source = ""
count = 0
result = ""

def advance():

    global count,sym,result
    result = result+source[count]
    count = count + 1
    if count < len(source):
        sym = source[count]
        print("当前匹配的字符:",sym)

def error():
    print("进入到推导式F时匹配的字符不是i导致匹配失败")
    exit(1)

def error1():
    print("括号匹配匹配失败")
    exit(1)

def E():
    """
    E->TG
    :return:
    """
    #print("E ")
    T()
    G()


def G():
    """
    G->+TG|—TG
    G->ε
    :return:
    """
    #print("G ")
    if sym == '+':
        advance()
        T()
        G()
    elif sym == '-':
        advance()
        T()
        G()



def T():
    """
    T->FS
    :return:
    """
    #print("T ")
    F()
    S()

def S():
    """
    S->*FS|/FS
    S->ε
    :return:
    """
    #print("S ")
    if sym == '*':
        advance()
        F()
        S()
    elif sym== '/':
        advance()
        F()
        S()



def F():
    """
    F->(E)
    F->i
    :return:
    """
    #print("F ")
    if sym == 'i':
        advance()
    elif sym == '(':
        advance()
        E()
        if sym==')':
            advance()
        else:
            error1()

    else:
        error()


def init(s):
    """
    初始化
    :return:
    """

    global source, count, sym
    source = s
    count = 0
    sym = source[count]
    print("当前匹配的字符:",sym)

if __name__ == "__main__":


    print("递归下降程序，编制人：徐志锋 201751060340 计科一班!!!")
    # 测试的表达式
    s = "i+i*i/i++1"
    s = input("输入一串符号串(包括+—*/（）i)例如（i+i*i）：")
    init(s)
    E()
    if result == s:
        print("输出结果：",s,"为合法符号串！！！")
    else:
        print("匹配到：",result,"时下一个字符",sym,"匹配失败")
        print("输出结果：",s,"为不合法符号串")



