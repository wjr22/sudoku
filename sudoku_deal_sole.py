"""
'''
    思路：维护一个background三维列表，其中前二维定位位置，
    最后一维为10个元素，如果第i个元素为0，则代表此位置不能填该数字（即它所在的行/列/九宫格有相同数字）
    迭代至sudoku数组完成即可
'''
"""
import tool

def iteration(sudoku):
    """
    v1.0 迭代法感觉没戏了，我重写dfs剪枝吧
    v2.0我又回来了
    :param sudo:
    :param back:
    :return:
    """
    while True:
        back = generate_back_array(sudoku)  # 迭代后台数组
        if tool.is_finish(sudoku): # 完成退出迭代
            tool.output(sudoku)
            break
        # 只能填一个
        for i in range(9):
            for j in range(9):
                m, n=0, 0 #
                for k in range(1,10):
                    if back[i][j][0] ==0 and back[i][j][k] != 0: # (i,j)位可以填k
                        m = k
                        n = n+1
                if n == 1:
                    back[i][j][0] = m
                    # sudoku[i][j] = m
        # 迭代行
        row_only(sudoku, back)
        # 迭代列
        line_only(sudoku,back)
        # 迭代九宫格
        group_only(sudoku,back)
        # 循环调用
        # iteration(sudoku) 它会爆
    return

def generate_back_array(sudoku):
    """
    根据 sudoku 生成back 三元数组
    :return:
    """
    # 法1：循环生成法 十个元素，第一个为标识位，该位上的数字表示数独中（该）填的数字
    back = []
    for i in range(9):
        back.append([])
        for j in range(9):
            back[i].append([])
            back[i][j] = [k for k in range(10)]
            if sudoku[i][j] != 0:
                for k in range(1,10):
                    back[i][j][k] = 0 # 设置已经有的为0
                back[i][j][0] = sudoku[i][j]
    # 法2：列表生成器 不会用算了放弃了
    # 除了设置已有的为0，还要把候选集中相同的去除（upgrade_back_array方法）
    return upgrade_back_array(sudoku, back)


def upgrade_back_array(sudoku, back):
    """
    更新候选集合，去掉行重复、列重复、九宫格重复
    :param sudoku:
    :param back:
    :return:
    """
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] != 0:
                for i in range(9):
                    back[x][i][sudoku[x][y]] = 0 #行去重
                    back[i][y][sudoku[x][y]] = 0 #列去重
                # 九宫格去重
                t_x, t_y=tool.get_area(x,y)
                for i in range(3):
                    for j in range(3):
                        back[t_x+i][t_y+j][sudoku[x][y]] = 0
                # 添加信息
                back[x][y][0] = sudoku[x][y]
    return back


def row_only(sudoku, back):
    """
    根据行确定唯一能填的数,
    例如
    （1)6 2 1 3 8 _ 4 5 7,则只能填9
    同理，候选数字中若某个数只出现一次，则该数一定填此位置
    :param sudoku:
    :param back:
    :param row:
    :return:
    """
    for x in range(9):
        for num in range(1,10):
            m, n = 0, 0
            for y in range(9):
                if back[x][y][num] != 0:
                    n = n + 1
                    m = y
            if n == 1:
                back[x][m][num] = 0
                back[x][m][0] = num
                sudoku[x][m] = num
        # 设置函数+返回有个问题：如果有多个这样的数呢？
        # return x, y, n


def line_only(sudoku, back):
    """
    根据列确定唯一能填的数,与行相似
    :param sudoku:
    :param back:
    :param row:
    :return:
    """
    for y in range(9):
        for num in range(1,10):
            m, n = 0, 0
            for x in range(9):
                if back[x][y][num] != 0:
                    n = n + 1
                    m = x
            if n == 1:
                back[m][y][num] = 0
                back[m][y][0] = num
                sudoku[m][y] = num


def group_only(sudoku, back):
    """
    根据九宫格确定唯一能填的数,与行相似又有区别
    1：直接全盘遍历，找九宫格再进行相似步骤
    2：将全盘划分成9个区域，遍历每个区域

    :param sudoku:
    :param back:
    :param row:
    :return:
    """
    for i in range(9): #序号1-9，从左上到右下，每三个一行
        for num in range(1,10): # 数字1-10
            p, q, n = 0, 0, 0
            for j in range(9): # 九宫格内部
                x_start = (i % 3) * 3 # x开始位置
                x_step = j % 3 # x增加
                y_start = (i // 3) * 3
                y_step = j // 3
                if back[x_start + x_step][y_start + y_step][num] != 0:
                    n = n + 1
                    p = x_step + x_start
                    q = y_start + y_step
            if n == 1:
                back[p][q][0] = num
                back[p][q][num] = 0
                sudoku[p][q] = num



#---------------------------------------------以下无用
