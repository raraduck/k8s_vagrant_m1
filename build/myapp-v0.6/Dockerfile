FROM nginx:alpine

# Set version label
LABEL version="0.6" \
      architecture="multiarch" \
      description="This image contains nginx with port 8080 and /health and /health?code=404 for liveness probe."

# Nginx 설정 파일 복사
COPY default.conf /etc/nginx/conf.d/default.conf

# 포트 8080 열기
EXPOSE 8080
