from flask import Flask,jsonify
import json,os
app=Flask(__name__)
port=int(os.environ.get("PORT",8000))

#健康检测接口（赛前唤醒用）
@app.route("/health")
def health():
    return jsonify({"status":"ok","entries":165})

#openapi文档接口（蓝鹰敏学平台导入地址）
@app.route("/openapi.json")
def doc():
    with open("data.json","r",encoding="utf-8") as f:
        return json.load(f)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=port)
