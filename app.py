from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to another Flask example"

@app.route('/cal',methods=["GET"])
def math_operation():
    # here we will take inputs from POSTMAN and so we have written request.json
    operation = request.json["operation"]
    num1 = request.json["num1"]
    num2 = request.json["num2"]
    # above inputs we will get from HTML or Postman and then we will process the data

    if operation == "add":
        result = int(num1) + int(num2)

    elif operation == "multiply":
        result = int(num1) * int(num2)

    elif operation == "division":
        result = int(num1) / int(num2)
    
    else:
        result = int(num1) - int(num2)

    return jsonify(result)

print(__name__)

if __name__ == '__main__':
    app.run(debug=True,port='5001')