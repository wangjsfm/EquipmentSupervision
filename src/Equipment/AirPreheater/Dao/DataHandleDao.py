import  pandas as pd


def HandleExcel(filepath='../../Resource/data.xlsx'):
    """
        获取excel数据并转为map，同时按照不同负荷，对数据进行分类
    :param filepath: 文件名称
    :return:
    """
    data = pd.read_excel(filepath)

    tempMap = {}

    tempMap['mw660'] = data.loc[:, ['H', 'B', 'A']]
    tempMap['mw660']['M'] = '660'  #增加负荷数据列
    tempMap['mw660'] = tempMap['mw660'].loc[:,['M','H', 'B', 'A']]

    tempMap['mw590'] = data.loc[:, ['G', 'B', 'A']]
    tempMap['mw590']['M'] = '590'
    tempMap['mw590'] = tempMap['mw590'].loc[:, ['M', 'G', 'B', 'A']]

    tempMap['mw540'] = data.loc[:, ['F', 'B', 'A']]
    tempMap['mw540']['M'] = '540'
    tempMap['mw540'] = tempMap['mw540'].loc[:, ['M', 'F', 'B', 'A']]

    tempMap['mw460'] = data.loc[:, ['E', 'B', 'A']]
    tempMap['mw460']['M'] = '460'
    tempMap['mw460'] = tempMap['mw460'].loc[:, ['M', 'E', 'B', 'A']]

    tempMap['mw400'] = data.loc[:, ['D', 'B', 'A']]
    tempMap['mw400']['M'] = '400'
    tempMap['mw400'] = tempMap['mw400'].loc[:, ['M', 'D', 'B', 'A']]

    tempMap['mw330'] = data.loc[:, ['C', 'B', 'A']]
    tempMap['mw330']['M'] = '330'
    tempMap['mw330'] = tempMap['mw330'].loc[:, ['M', 'C', 'B', 'A']]
    return  tempMap



if __name__ == '__main__':
    filepath = '../../Resource/data.xlsx'
    mapData = HandleExcel(filepath)
    temp = mapData['mw330']
    data = temp.iloc[:,0:3]
    target = temp.iloc[:,3:4]
    print(target)


