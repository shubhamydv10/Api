from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/abc',methods=['GET', 'POST'])
def test1():
    if(request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a+ b
        return jsonify((str(result)))

@app.route('/abc1/shub',methods=['GET', 'POST'])
def test2():
    if(request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a*b
        return jsonify((str(result)))

@app.route('/abc1/shub/test3',methods=['GET', 'POST'])
def test3():
    if(request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a**b
        return jsonify((str(result)))

@app.route('/abc1/shub/test4',methods=['GET', 'POST'])
def test4():
    if(request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a-b
        return jsonify((str(result)))

@app.route('/abc1/shub/test5',methods=['GET', 'POST'])
def test5():
    if(request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a/b
        return jsonify((str(result)))


if __name__ =='__main__' :
    app.run()




