# #"Hello World!"と表示されるWebアプリケーション
# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'Hello World!'

# if __name__ == '__main__':
#     app.run()
#ここまでテストコード

# コードの説明
# Flaskのインポート: Flaskをインポートしてアプリケーションを作成します。
# エンドポイントの定義: /chatというエンドポイントを定義し、POSTリクエストを受け取ります。
# 簡単な応答ロジック: ユーザーからのメッセージを受け取り、それに対する応答を返します。
# アプリケーションの実行: app.run()でアプリケーションを実行します。

from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'response': 'メッセージを入力してください。'}), 400

    if 'こんにちは' in user_input:
        response = 'こんにちは！今日はどうされましたか？'
    else:
        response = 'すみません、よくわかりません。'

    return jsonify({'response': response})

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)