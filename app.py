from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from ulits.logger import logger



app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return jsonify("msg":"ok")

@app.route('/api/outh', methods=['POST'])
def api_outh():
    data = request.form  # 获取JSON数据
    usertoken = data.get('usertoken', '')  # 获取usertoken
    carid = data.get('carid', '')  # 获取carid
    logger.info(f"User ID: {carid}")  
    logger.info(f"User Token: {usertoken}")
    if usertoken == "adminAAA123456":
        reqs={
        "code": 0,
        "msg": "登陆失败时的提示信息"
        }
    else:
        reqs={
            "code": 1,
            "msg": "登陆成功时的提示信息"
            }
    return jsonify(reqs)


@app.route('/login', methods=['POST'])
def log():
    # 获取前端发来的 JSON 数据
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')
    token=str(username +"AAA"+ password)
    # 模拟验证过程
    if 1:
        # 成功登录，返回 token 和用户名
        reqs = {
            "name": username,
            "token": token
        }
    else:
        # 登录失败
        reqs = {
            "name": None,
            "token": None
        }
    return jsonify(reqs)

if __name__ == '__main__':
    app.run(debug=True,port=45612,host='0.0.0.0')
