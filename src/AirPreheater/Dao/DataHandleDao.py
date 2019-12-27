import  pandas as pd


def HandleExcel():
    filepath = '../../Resource/data.xlsx'
    data = pd.read_excel(filepath)
    print(data)


if __name__ == '__main__':
    HandleExcel()


