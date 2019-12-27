import  pandas as pd
import  numpy as np

#y=ks 系数k的值
K_LIST = {
        'mw330':2425,
        'mw400': 2584,
        'mw460': 2650,
        'mw540': 2660,
        'mw590': 2700,
        'mw660': 2850,
    }


def HandleExcel(filepath='../../../Resource/data.xlsx'):
    """
        获取excel数据并转为map，同时按照不同负荷，对数据进行分类
    :param filepath: 文件名称
    :return:
    """
    data = pd.read_excel(filepath)

    tempMap = {}
    tempMap['mw660'] =SelectData(np.array(data.loc[:, ['H']]).tolist())
    tempMap['mw590'] =SelectData(np.array(data.loc[:, ['G']]).tolist())
    tempMap['mw540'] = SelectData(np.array(data.loc[:, ['F']]).tolist())
    tempMap['mw460'] = SelectData(np.array(data.loc[:, ['E']]).tolist())
    tempMap['mw400'] = SelectData(np.array(data.loc[:, ['D']]).tolist())
    tempMap['mw330'] = SelectData(np.array(data.loc[:, ['C']]).tolist())
    tempMap['sulphur']= SelectData(np.array(data.loc[:, ['B']]).tolist())

    return  tempMap


def SelectData(list1):
    """
    将2维数组转为 1维数组
    :param list1:
    :return:
    """
    tempList=[]
    for item in list1:
        tempList.append(item[0])
    return  tempList

if __name__ == '__main__':
    filepath = '../../../Resource/data.xlsx'
    mapData = HandleExcel(filepath)
    temp = mapData['mw330']
    data = temp.iloc[:,0:3]
    target = temp.iloc[:,3:4]
    print(target)


