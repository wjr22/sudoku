import csv

def read(path):
    """
    从csv读数据（9*9）
    :param path:
    :return:
    """
    f = csv.reader(open(path, 'r'))
    sudo_str = [i for i in f]
    sudo_int = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(9)]
    for i in range(len(sudo_str)):
        for j in range(len(sudo_str[i])):
            sudo_int[i][j] = int(sudo_str[i][j])
    return sudo_int


def get_area(x,y):
    """
    获取坐标为(x,y)的所属九宫格
    :param x:
    :param y:
    :return:
    """
    t_x = x // 3
    t_y = y // 3
    return t_x*3, t_y*3


def is_finish(sudoku):
    """
    判断数独是否完成
    :param sudoku:
    :return:
    """
    temp = 0
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                temp = temp + 1
    if temp == 81:
        return True
    return False


def output(sudoku):
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j],end=' ,')
        print('\n')


def judge(sudoku, x, y, num):
    """
    判断x,y位置能不能填数字num，
    :param x:
    :param y:
    :param num:
    :return: True：可以，False：不行
    """
    t_x, t_y = get_area(x, y)
    for i in range(9):
        if sudoku[x][i] == num:   #行不能有一样的
            return False
        if sudoku[i][y] == num:   #列不能有一样的
            return False
    for i in range(3):
        for j in range(3):      #九宫格内不能一样
            if sudoku[t_x+i][t_y+j] == num:
                return False
    return True


def is_only(sudoku, back, x, y):
    """
    判断x,y处是否只能填一个数
    :param x:
    :param y:
    :return:
    """
    s = back[x][y]
    for i in s:
        if i != 0:
            m, n = 0, 0
            if judge(sudoku, x, y, i):
                m = i
                n = n+1
