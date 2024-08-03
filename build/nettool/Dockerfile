# Base image from Alpine Linux
FROM alpine:latest

LABEL version="0.2" \
      architecture="multiarch" \
      description="This image contains network tools for debugging in Kubernetes."

# Install necessary network debugging tools
run apk add --no-cache \
    net-tools \
    iputils \
    bind-tools \
    curl \
    tcpdump \
    socat

# Default command
CMD ["sh"]
