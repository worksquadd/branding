FROM python:3.14-alpine

WORKDIR /app
COPY serve_assets.py ./
COPY assets ./assets

EXPOSE 6700

CMD ["python3", "serve_assets.py"]
