from flask import Flask, request, jsonify

app = Flask(__name__)

def printflush(*messages):
    print(*messages, flush=True)

@app.route('/echo', methods=['POST'])
def echo():
    try:
        printflush(f"REQUEST: ''' {request} '''")
        printflush(f"REQUEST BODY: ''' {request.get_data(as_text=True)} '''")
        printflush(f"REQUEST JSON: ''' {request.get_json()} '''")
        data = request.get_json()
        return jsonify({'message': data['message']}), 200

    except Exception as e:
        printflush(f"ERROR:  {e} ")
        return jsonify({'message': 'Error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
