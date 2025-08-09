from flask import Flask, request, jsonify
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agent.support_agent import query_agent
from agent.tools import load_json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    question = data.get("question", "")
    course_info = load_json("data/course_info.json")
    response = query_agent(question, course_info)
    return jsonify({"answer": response})

if __name__ == '__main__':
    app.run(port=5001)
