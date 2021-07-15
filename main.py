from flask import Flask,request,Response
import json
import helper


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/tasks/new',methods=['POST'])
def add_new_item():
    req_data = request.get_json()
    item = req_data['item']
    res_data = helper.add_to_list(item)

    if res_data is None:
        response = Response("{'error': 'Item not added - " + item + "'}", status=400 , mimetype='application/json')
        return response
    response = Response(json.dumps(res_data),mimetype='application/json')
    return response

@app.route('/tasks/get')
def get_items():
    req_data = helper.get_all_items()
    response = Response(json.dumps(req_data),mimetype='application/json')
    return response

@app.route('/tasks/status',methods=['GET'])
def item_status():
    item_name = request.args.get('name')
    print(item_name)
    item_status = helper.get_item_status(item_name)
    print(item_status)
    if item_status is None:
        response = Response("{'error': 'Status not found - " + item_name + "'}", status=400, mimetype='application/json')
        return response
    res_data = {"status":item_status}
    response = Response(json.dumps(res_data),status=200,mimetype='application/json')
    return response

@app.route('/tasks/update',methods=['PUT'])
def update_status():
    req_data = request.get_json()
    item = req_data['item']
    status = req_data['status']
    res_data = helper.update_item(item,status)
    if status is None:
        response = Response("{'error': 'Status not found - " + item + "'}", status=400, mimetype='application/json')
        return response
    response = Response(json.dumps(res_data),status=200,mimetype='application/json')
    return response


@app.route('/tasks/delete',methods=['DELETE'])
def delete_item():
    req_data = request.get_json()
    item = req_data['item']
    res_data = helper.delete_item(item)
    if res_data is None:
        response = Response("{'error': 'Data not found - " + item + "'}", status=400, mimetype='application/json')
        return response
    response = Response(json.dumps(res_data),status=200,mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(debug=True)

