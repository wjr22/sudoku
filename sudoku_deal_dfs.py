#! python
#encoding:utf-8
import csv
import tool



def dfs(sudoku, x, y):
    """
    暴力推解法
    :param sudoku:
    :param x: 横坐标 以0开头，递增
    :param y: 纵坐标 同理
    :return:
    """
    if tool.is_finish(sudoku):
        print(sudoku)
        return
    else:
        for i in range(x,9):    #y先不变(range 左闭右开)
            if sudoku[i][y] == 0:  # 有了跳过
                # 跳过  事实证明这样跳不了
                # dfs(sudoku,x+1,y+1)
                for k in range(1, 10):
                    if tool.judge(sudoku, i, y, k):
                        sudoku[i][y] = k
                        if y == 8:
                            dfs(sudoku, 0, y + i + 1)
                        else:
                            dfs(sudoku, y + 1, i)
                        sudoku[i][y] = 0







