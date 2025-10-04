FROM python:3.11-slim
WORKDIR /app
COPY helloworld.py .
CMD ["python", "helloworld.py"]
