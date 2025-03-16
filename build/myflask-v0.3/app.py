from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    # 환경변수 MESSAGE 읽기
    message = os.getenv('MESSAGE', '')
    # 환경변수 HOSTNAME (Pod의 이름) 읽기
    hostname = os.getenv('HOSTNAME', 'Unknown Hostname')

    # 응답 문자열 구성
    response = "Hello, World!\n"
    if message:
        response += f"Message: {message}\n"
    response += f"Pod Name: {hostname}\n"

    return response

@app.route('/health')
def health():
    # URL 파라미터 'code' 확인
    code = request.args.get('code')
    
    if code == '404':
        return "Failed Response\n", 404
    
    return "Health Checked\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
