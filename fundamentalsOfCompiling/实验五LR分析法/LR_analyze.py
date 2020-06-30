"""
    @Author:sumu
    @Date:2020-06-08 03:23
    @Email:xvzhifeng@126.com

"""

"""
LR(1) 分析程序，直接运行输入测试案例：i+i*i# 等。
"""

"""
文法：
（1）E->E+T
（2）E->E—T
（3）T->T*F
（4）T->T/F
（5）F->(E)
（6）F->i
（7）E->T
（6）T->F

"""

from prettytable import PrettyTable

#输出分析表的表头
table = PrettyTable(["步骤", "状态栈", "符号栈", "剩余输入串", "动作"])

# coding:UTF-8
class Stack(object): # 栈的实现
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def show(self):
        print(self.items, end='')


GOTO = dict(list()) # GOTO表
ACTION = dict(list()) # ACTION表
MAP = dict(list()) # 文法产生式
stat = Stack() # 状态栈
symbol = Stack() # 符号栈
left = Stack() # 剩余字符串


def init(original): # 给定分析表
    # GOTO['E'] = (1, -1, -1, -1, 8, -1, -1, -1, -1, -1, -1, -1)
    # GOTO['T'] = (2, -1, -1, -1, 2, -1, 9, -1, -1, -1, -1, -1)
    # GOTO['F'] = (3, -1, -1, -1, 3, -1, 3, 10, -1, -1, -1, -1)
    #
    # ACTION['i'] = ('s.5', '0', '0', '0', 's.5', '0', 's.5', 's.5', '0', '0', '0', '0')
    # ACTION['+'] = ('0', 's.6', 'r.2', 'r.4', '0', 'r.6', '0', '0', 's.6', 'r.1', 'r.3', 'r.5')
    # ACTION['*'] = ('0', '0', 's.7', 'r.4', '0', 'r.6', '0', '0', '0', 's.7', 'r.3', 'r.5')
    # ACTION['('] = ('s.4', '0', '0', '0', 's.4', '0', 's.4', 's.4', '0', '0', '0', '0')
    # ACTION[')'] = ('0', '0', 'r.2', 'r.4', '0', 'r.6', '0', '0', 's.11', 'r.1', 'r.3', 'r.5')
    # ACTION['#'] = ('0', 'A', 'r.2', 'r.4', '0', 'r.6', '0', '0', '0', 'r.1', 'r.3', 'r.5')
    #
    # MAP[1] = ("E", "E+T")
    # MAP[2] = ("E", "T")
    # MAP[3] = ("T", "T*F")
    # MAP[4] = ("T", "F")
    # MAP[5] = ("F", "(E)")
    # MAP[6] = ("F", "i")



    GOTO['E'] = ( 1, -1, -1, -1, -1, -1, 7, -1, -1, -1, -1, -1, -1, 14, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,-1)
    GOTO['T'] = ( 27, -1, 3, -1, -1, -1,22, -1, -1, 10, -1, -1, -1, 22, -1, -1, 17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 3)
    GOTO['F'] = ( 26, -1, 26, -1, 5, -1,21, -1, -1, 21, -1, 12, -1, 21, -1, -1, 21, -1, 19, -1, -1, -1, -1, -1, 25, -1, -1, -1,26)



    ACTION['#'] = ('0'   , 'A'   , '0'   , 'r.1', '0', 'r.3', '0', '0', 'r.5', '0', '0', '0', '0', '0', '0', '0', '0', '0','0', '0', '0', '0', '0', 'r.6', '0', 'r.4', 'r.8', 'r.7', '0')
    ACTION['i'] = ('s.23', '0'   , 's.23', '0', 's.23', '0', 's.20', '0', '0', 's.20', '0', 's.20', '0', 's.20', '0', '0', 's.20', '0','s.20', '0', '0', '0', '0', '0', 's.23', '0', '0', '0', 's.23')
    ACTION[')'] = ('0'   , '0'   , '0'   , '0', '0', '0', '0', 's.8', '0', '0', 'r.1', '0', 'r.3', '0', 's.15', 'r.5', '0', '0','0', 'r.4', 'r.6', 'r.8', 'r.7', '0', '0', '0', '0', '0', '0')
    ACTION['('] = ('s.6' , '0'   , 's.6' , '0', 's.13', '0', '0', 's.13', '0', 's.13', '0', 's.13', '0', '0', 's.13', '0', 's.13', '0','0', '0', '0', '0', '0', '0', 's.6', '0', '0', '0', 's.6')
    ACTION['/'] = ('0'   , '0'   , '0'   , 's.24', '0', 'r.3', '0', '0', 'r.5', '0', 's.18', '0', 'r.3', '0', '0', 'r.5', '0', 's.18','0', 'r.4', 'r.6', 'r.8', 's.18', 'r.6', '0', 'r.4', 'r.8', 's.24', '0')
    ACTION['*'] = ('0'   , '0'   , '0'   , 's.4' , '0', 'r.3', '0', '0', 'r.5', '0', 's.11', '0', 'r.3', '0', '0', 'r.5', '0', 's.11','0', 'r.4', 'r.6', 'r.8', 's.11', 'r.6', '0', 'r.4', 'r.8', 's.4', '0')
    ACTION['-'] = ('0'   , 's.28'   , '0'   , 'r.1', '0', 'r.3', '0', 's.16', 'r.5', '0', 'r.1', '0', 'r.3', '0', 's.16', 'r.5', '0', 'r.2','0', 'r.4', 'r.6', 'r.8', 'r.7', 'r.6', '0', 'r.4', 'r.8', 'r.7', '0')
    ACTION['+'] = ('0'   , 's.2'   , '0'   , 'r.1', '0', 'r.3', '0', 's.9', 'r.5', '0', 'r.1', '0', 'r.3', '0', 's.9', 'r.5', '0', 'r.2','0', 'r.4', 'r.6', 'r.8', 'r.7', 'r.6', '0', 'r.4', 'r.8', 'r.7', '0')

    MAP[1] = ("E", "E+T")
    MAP[2] = ("E", "E-T")
    MAP[3] = ("T", "T*F")
    MAP[4] = ("T", "T/F")
    MAP[5] = ("F", "(E)")
    MAP[6] = ("F", "i")
    MAP[7] = ("E", "T")
    MAP[8] = ("T", "F")

    r_original = original[::-1] # 输入字符串逆序入栈成为剩余字符串
    for each in r_original:
        left.push(each)

    stat.push(0) # 开始状态入符号栈
    symbol.push('#') # 终结符入状态栈


def Create_table(cnt, act): # 输出当前栈内信息
    # print(cnt, '\t\t\t', end='')
    # #stat.show()
    # print(stat.items,'\t\t\t', end='')
    # symbol.show()
    # print('\t\t\t\t', end='')
    # left.show()
    # print('\t\t\t\t', end='')
    # print(act)
    production = []
    production.append(cnt)
    production.append(list(stat.items))
    production.append(list(symbol.items))
    production.append(list(left.items))
    production.append(act)
    table.add_row(production)
    production.clear()


def run():
    #print('步骤\t\t  ', '状态栈\t\t\t', '符号栈\t\t\t\t\t', '剩余输入串\t\t\t\t\t', '动作')
    cnt = 0
    action_log = "初始化"
    Create_table(cnt, action_log)
    while True: # 开始分析过程
        stat_ = stat.peek()
        left_ = left.peek()

        act = ACTION[left_][stat_]
        if 's' in act: # 移进
            stat.push(int(act.split('.')[1]))
            symbol.push(left.pop())
            action_log = "移进"
        elif 'r' in act: # 规约
            action_log = "规约"
            tmp = int(act.split('.')[1])
            key = MAP[tmp][0]
            value = MAP[tmp][1]
            key_r = key[::-1]
            value_r = value[::-1]

            t_str = ""
            while t_str != value_r:
                # print("t_str= ", t_str," value= ", value_r)
                t_str += symbol.peek()
                symbol.pop()

            for each in key_r:
                symbol.push(each)

            stat.pop()
            stat.push(GOTO[symbol.peek()][stat.peek()])
        elif 'A' in act: # 接受
            #cnt += 1
            table.del_row(cnt)
            Create_table(cnt, "ACCEPT")
            #print('ACCEPT')
            return

        else: # 出错
            Create_table(cnt, act)
            print("Error")
            break

        while symbol.size() is not stat.size(): # 状态栈和符号栈平衡过程，也许应该放到规约过程中（未测试）
            stat.pop()

        cnt += 1

        Create_table(cnt, action_log)

def ShowTable():
    # 表左对齐
    table.align['步骤'] = 'l'
    table.align['状态栈'] = 'l'
    table.align['符号栈'] = 'l'
    table.align['剩余输入串'] = 'l'
    table.align['动作'] = 'l'
    # 输出语法分析表
    print(table)

def main():
    string = input("字符串：")
    init(string)
    run()
    ShowTable()


if __name__ == "__main__":
    main()
