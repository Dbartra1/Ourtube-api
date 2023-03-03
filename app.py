from flask import Flask, request, jsonify, redirect, url_for

app = Flask(__name__)

##@app.route('/hello/', methods=['GET', 'POST'])
##def welcome():
    ##return "Hello World!"

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == "GET":
        return jsonify({"response": "Get Request Called!"})
    elif request.method == "POST": 
        req_Json = request.json
        name = req_Json ['name']
        return jsonify({"response": "Hi" + name})

if __name__ == '__main__': 
    app.run(debug=True, port=9090)

##if __name__ == '__main__':
    ##app.run(host='0.0.0.0', port=105)
