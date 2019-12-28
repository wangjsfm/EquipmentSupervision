from src.Equipment.AirPreheater.FitModel.SulphurModle import SulrPhlurAlerm
import pandas as pd
import  numpy as np
from sklearn.metrics import mean_squared_error


from sklearn.metrics import mean_squared_error

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

def HandleExcel(filepath='../src/Resource/predict.xlsx'):
    """
        获取excel数据并转为map，同时按照不同负荷，对数据进行分类
    :param filepath: 文件名称
    :return:
    """
    data = pd.read_excel(filepath)
    x =data.loc[:, ['mw','so2']]
    y = data.loc[:, ['target']]

    return  x,y





if __name__ == '__main__':
    # x,y = HandleExcel()
    #
    # x= np.array(x).tolist()
    # y_true = np.array(y).tolist()
    #
    # y_pred = []
    # for item in range(len(x)):
    #     tempdata = x[item]
    #     tem = round(SulrPhlurAlerm(tempdata[0], tempdata[1]), 2)
    #     y_pred.append(tem)
    #
    # de = mean_squared_error(y_true,y_pred)  #偏差2.55
    #
    # print(de)

    load = 330
    so2 = 2165
    print(SulrPhlurAlerm(load,so2))







