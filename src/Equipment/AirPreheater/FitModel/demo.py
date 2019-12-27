from src.Equipment.AirPreheater.Dao.DataHandleDao import HandleExcel,K_LIST


if __name__ == '__main__':
    origoData = HandleExcel()['sulphur']
    so2 = 2700
    sulphur= round(so2/K_LIST['mw330'],1)
    print(sulphur)





