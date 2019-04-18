#! python
#encoding:utf-8
from python import sudoku_deal_sole as sole, tool

"""
    主程序入口
    项目说明：一个解法一个文件，一个工具文件
"""
# 内置数独
sudo = [[0,0,0,9,0,0,6,0,0],
        [6,4,0,0,0,0,0,3,1],
        [8,0,0,0,1,0,0,0,9],
        [0,0,5,0,2,0,0,0,0],
        [9,0,0,0,7,0,0,1,5],
        [0,7,4,0,0,0,9,2,0],
        [0,0,6,8,3,0,0,5,7],
        [0,1,0,0,0,0,0,9,6],
        [0,5,0,0,9,0,2,0,0]]

back = [[[]]]


def main():
    """
    启动程序，应包括数独库的输入、调用以及返回结果
    :return:
    """
    sudoku = tool.read('../data/data_mid.csv')
    sole.iteration(sudoku)

    return


if __name__ == '__main__':
    main()