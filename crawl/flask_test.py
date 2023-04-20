from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    answer = request.form.get('answer')
    user_id = request.form.get('id')
    # answer와 user_id를 이용하여 처리할 코드 작성
    return 'Success'

if __name__ == '__main__':
    app.run()