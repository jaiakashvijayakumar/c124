from flask import Flask,jsonify,request
from asyncio import tasks

app = Flask(__name__)

contacts = [
    {
        "Contact" : "9987644456",
            "Name" : "Raju",
            "done" : False,
            "id" : 1
    },

      {
        "Contact" : "9876543222",
            "Name" : "Rahul",
            "done" : False,
            "id" : 2
    },
]

@app.route("/add-data",methods = ["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status" : "error",
            "message" : "pls provide the data"
        },400)

    contact = {
        "id" : tasks[-1]["id"]+1,
        "title" : request.json["title"],
        "description" :request.json.get("description",""),
        "done" : False
    }
    tasks.append(contact)    
    return jsonify({
        "status" : "success",
        "message" : "task added successfully"
    })

@app.route("/get-data")

def get_task():
    return jsonify({

        "data":tasks
    })

if(__name__ == "__main__"):
    app.run(debug=True)    


