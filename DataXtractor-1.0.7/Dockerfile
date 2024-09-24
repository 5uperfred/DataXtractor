FROM python:3.11

RUN apt-get update && apt-get install -y \
    libpoppler-cpp-dev \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn --bind 0.0.0.0:$PORT app:app
