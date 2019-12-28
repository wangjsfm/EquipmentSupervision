
import  numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression



def SelectData(list1):
    """
    将2维数组转为 1维数组
    :param list1:
    :return:
    """
    tempList=[]
    for item in list1:
        tempList.append(round(item[0],2))
    return  tempList

def HandleExcel(filepath='../src/Resource/tempData.xlsx'):
    """
        获取excel数据并转为map，同时按照不同负荷，对数据进行分类
    :param filepath: 文件名称
    :return:
    """
    data = pd.read_excel(filepath)
    x =data.loc[:, ['s']]
    y = data.loc[:, ['t']]

    return  x,y


if __name__ == '__main__':
    x,y = HandleExcel()
    lr = LinearRegression()
    lr.fit(x,y)

    print(lr.predict( [[1.12],
                       [1.6],
                      [ 2.5],

                       ] ))