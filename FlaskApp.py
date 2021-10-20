from flask import Flask,jsonify,request

app = Flask(__name__)

contacts = [
    {
        'Id':1,
        'Name':u'James Hall',
        'Contact':u'9925476481',
        'done':False
    },
    {
        'Id':2,
        'Name':u'Kelly Clarkson',
        'Contact':u'9374659234',
        'done':False
    },
    {
        'Id':3,
        'Name':u'Emma Kaven',
        'Contact':u'8354667543',
        'done':False
    }
]

@app.route('/')
def HelloWorld():
    return "Hello World"

@app.route('/add-data',methods = ['POST'])
def add_task():
    if not request.json:
        return jsonify({
            "status":'error',
            'message':'Please provide the data.'
        },400)

    contact = {
        'Id':contacts[-1]['Id']+1,
        'Name':request.json['Name'],
        'Contact':request.json.get('Contact'),
        'done':False
    }
    contacts.append(contact)
    return jsonify({
        'status':'success',
        'message':'Task added successfully.'
    })

@app.route('/get-data')
def get_task():
    return jsonify({
        "data":contacts
    })

if (__name__ == "__main__"):
    app.run(debug = True)