FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY feinstaub.py /app/feinstaub.py

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "feinstaub.py"]