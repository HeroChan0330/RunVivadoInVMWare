from flask import Flask, jsonify
from flask import request
import subprocess,os

app=Flask(__name__)

SHARE_FOLDER_WINDOWS = "D:/VMUbuntu/Share"
SHARE_FOLDER_LINUX = "/mnt/hgfs/Share"

@app.route("/vscode", methods=["POST"])
def vscode():
    if request.method == "POST":
        if request.content_type.startswith('application/json'):            
            addr = request.json.get('addr')
            line =  request.json.get('line')
        elif request.content_type.startswith('multipart/form-data'):
            addr = request.form.get('addr')
            line =  request.form.get('line')
        else:
            addr = request.values.get("addr")
            line =  request.values.get('line')
        addr = addr.replace(SHARE_FOLDER_LINUX,SHARE_FOLDER_WINDOWS)
        subprocess.Popen('Code.exe -g "%s":%s'%(addr,line))
        return "success"
    else:
        return "method error"

if __name__=="__main__":
    app.run(port=4567,host="192.168.65.1",debug=True)