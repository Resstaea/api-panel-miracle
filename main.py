from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/crapi/had/viewstats', methods=['GET'])
def viewstats():
    token = request.args.get('token')
    sEcho = request.args.get('sEcho', 1)
    
    # Token ambil dari Railway Variables biar aman
    API_TOKEN = os.environ.get('API_TOKEN', 'Qk5YQUVBUzRkeJVjR4CId0GDlFVBc2Bia4CFU0qAWHRbZZaGXmGHUw==')
    
    if token != API_TOKEN:
        return jsonify({"error": "Invalid token"}), 401

    result = {
        "sEcho": int(sEcho),
        "iTotalRecords": 0,
        "iTotalDisplayRecords": 0,
        "aaData": []
    }
    
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
