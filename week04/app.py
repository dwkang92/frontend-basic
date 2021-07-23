from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    # render_template라는 내장함수를 사용하여, html파일을 불러와준다.
    # 유저가 / 라는 라우터로 접속을 하면, 함수 home이 실행되어지고,
    # 함수 home()의 실행 내용인 index.html의 내용물을 불러와준다.
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


@app.route('/test', methods=['GET'])
def test_get():
    # title_give로 저장된 값을 가져와바. 그걸 title_receive에 넣어줘.
    title_receive = request.args.get('title_give')
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})


@app.route('/test', methods=['POST'])
def test_post():
    title_receive = request.form['title_give']
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})
