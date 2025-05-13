from flask import Flask, send_from_directory, jsonify
from src.llm_helper import summarize_trends

app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'world_map.html')

@app.route('/summary')
def summary():
    text = summarize_trends()
    return jsonify(summary=text)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
