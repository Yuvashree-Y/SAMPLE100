from flask import Flask,request,jsonify
app=Flask(__name__)
orders=[]
@app.route('/addOrders',methods=['POST'])
def addOrders():
    name=request.form['name']
    product=request.form['product']
    quantity=request.form['quantity']
    orders.append({"name":name,"product":product,"quantity":quantity})
    return "Orders added successfully"
@app.route('/showOrders')
def showOrders():
    return jsonify(orders)
app.run(debug=True)