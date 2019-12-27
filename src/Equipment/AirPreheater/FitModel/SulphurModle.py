from src.Equipment.AirPreheater.Dao.DataHandleDao import HandleExcel,K_LIST
import  matplotlib.pyplot as plt

def ThresholdModel(so2,load):
        """
            根据so2浓度、负荷值确定硫份定值
        :param so2:
        :param load:
        :return:硫份定值
        """
        return round(so2/K_LIST[load],2) # 生成定值

def FitSurphur(so2,start,end):
    """
    根据so2 负荷段拟合硫份
    :param so2:
    :param start:
    :param end:
    :return:
    """
    sulphurEnd = ThresholdModel(so2, 'mw'+str(end)) #末端点硫份
    sulphurStart = ThresholdModel(so2, 'mw'+str(start))#首端硫份
    k = (sulphurEnd - sulphurStart) / (end-start) #硫份变化率

    laodRate = load - start #负荷变化量
    return round(laodRate * k + sulphurStart, 2)  # y = kx + b  拟合结果


def FittingFixedValue(so2,load):
    """
        根据so2 、负荷获取   入炉煤硫份
    :param so2:
    :param load:
    :return:
    """
    if load<330 & load >660:
        #暂不处理
        return

    elif load>=330 & load<=400 :
        return  FitSurphur(so2,330,400)

    elif load>400 & load<460 :
        return FitSurphur(so2, 400, 460)

    elif load >= 460 & load <= 540:
        return FitSurphur(so2, 460, 540)

    elif load > 540 & load < 590:
        return FitSurphur(so2, 540, 590)

    elif load >= 590 & load <= 660:
        return FitSurphur(so2, 590, 660)








if __name__ == '__main__':

    so2 =6050
    load = 540
    # sulphur400 =ThresholdModel(s02,'mw400')
    # sulphur330 = ThresholdModel(s02, 'mw330')
    # print(sulphur400,sulphur330)
    # k = (sulphur400 - sulphur330) / (400 - 330)
    # print(k*40)
    # print(k*40+sulphur330)
    surphlur = FittingFixedValue(so2,load)
    print(surphlur)



