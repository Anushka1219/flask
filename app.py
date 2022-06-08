from flask import Flask,jsonify,request
app=Flask(__name__)

tasks=[{'id':12192007,'title':"Flask",'Description':"Requesting web browsers for information",'done':False},
{'id':1921,'title':"Coding",'Description':"Whitehat Jr",'done':False}]

@app.route("/")
def Hello_World():
    return "Contact Informations"

@app.route("/adddata",methods=["POST"])

def addtask():
    if not request.json:
        return jsonify({'status':"error",'message':"give data"},400)
        task={'id':tasks[-1]["id"]+1,'title':request.json["title"],'description':request.json.get("description",""),'done':False}
        tasks.append(task)

        return jsonify({'status':"success",'message':"task added successfully"})

@app.route("/getdata")

def gettask():
    return jsonify({'data':tasks})

if(__name__=="__main__"):
    app.run(debug=True)
