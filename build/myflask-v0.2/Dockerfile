# Python 3.10 Alpine 버전 사용
FROM python:3.10-alpine

# Set version label
LABEL version="0.2" \
      architecture="multiarch" \
      description="This alpine image contains python 3.10."

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치
RUN pip install flask

# 애플리케이션 파일 추가
COPY ./app.py /app/app.py

# 애플리케이션 실행
CMD ["python", "app.py"]