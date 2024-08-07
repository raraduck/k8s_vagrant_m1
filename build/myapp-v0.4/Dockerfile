FROM nginx:alpine

# Set version label
LABEL version="0.4" \
      architecture="multiarch" \
      description="This image contains nginx with port 8080 for debugging in Kubernetes."

# Nginx 설정 파일 복사
COPY default.conf /etc/nginx/conf.d/default.conf

# 포트 8080 열기
EXPOSE 8080
