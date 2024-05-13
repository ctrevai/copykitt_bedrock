FROM python:3.12

COPY requirements.txt /app/
COPY *.py /app/

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["streamlit", "run", "app.py"]