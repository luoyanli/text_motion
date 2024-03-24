from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# 用于提供前端页面的路由
@app.route('/')
def home():
    return send_from_directory('static', 'gui.html')

# 用于处理API请求的路由
@app.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.json
    text = data['text']
    print("Received text:", text)  # 打印接收到的文本，以便调试
    # 假设情感分析的结果
    result = "positive"  # 这里可以替换成你的情感分析逻辑
    print("Returning:", result)  # 打印返回的结果，以便调试
    return jsonify({'sentiment': result})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
