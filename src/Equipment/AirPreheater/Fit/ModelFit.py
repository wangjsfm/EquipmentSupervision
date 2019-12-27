from sklearn.svm import SVR

from src.Equipment.AirPreheater.Dao import HandleExcel
from sklearn.model_selection import train_test_split

def FitModel():
    data = HandleExcel()['mw660']
    print(data)

class FitModle():

    def __init__(self,load):
        """
            获取对应负荷下的原始数据 string
        :param load:
        """
        self.originData= HandleExcel()[load]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.originData.iloc[:, 0:3],#data
            self.originData.iloc[:, 3:4],
            test_size = 0.25,
            random_state = 0
        )


    #支持向量机线性回归SVR模型
    def fit_LinearSVR(self):
        regr=SVR.LinearSVR()
        regr.fit(self.X_train,self.y_train)
        print('Coefficients:%s, intercept %s'%(regr.coef_,regr.intercept_))
        print('Score: %.2f' % regr.score(self.X_test, self.y_test))







if __name__ == '__main__':

    modle = FitModel('660')
    modle.fit_LinearSVR()
