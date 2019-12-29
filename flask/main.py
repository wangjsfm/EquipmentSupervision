
from flask import  Flask,escape,request,Response
from src.Equipment.AirPreheater.FitModel.SulphurModle import SulrPhlurAlerm
import  json
app = Flask(__name__)

@app.route('/')
def hello():
    load =float( request.args.get("load"))
    so2 =  float(request.args.get("so2"))
    print(load,so2)
    alrmValue = SulrPhlurAlerm(load, so2)
    return json.dumps(alrmValue,ensure_ascii=False)

if __name__ == '__main__':
    app.debug = True # 设置调试模式，生产模式的时候要关掉debug
    app.run()