from flask import Flask
import os
import sys

app = Flask(__name__)

def get_port():
    # 명령줄 인수에서 포트 번호 파싱
    args = sys.argv[1:]  # 첫 번째 인수는 파일 이름이므로 제외
    for arg in args:
        if arg.startswith('-port='):
            port = arg.split('=')[1]
            return int(port)
    return 8080  # 기본 포트

@app.route('/')
def hello_world():
    message = os.getenv('MESSAGE', 'Hello, World!')
    hostname = os.getenv('HOSTNAME', 'Unknown Hostname')
    response = f"{message}\nPod Name: {hostname}\n"
    return response

@app.route('/health')
def health():
    code = request.args.get('code')
    if code == '404':
        return "Failed Response\n", 404
    return "Health Checked\n"

if __name__ == '__main__':
    port = get_port()  # 포트 번호 얻기
    # print(port)
    app.run(host='0.0.0.0', port=port)
