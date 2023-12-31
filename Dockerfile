FROM python:3.12.1

WORKDIR /app

EXPOSE 8080

COPY . .

#RUN pip install --upgrade pip
#RUN pip install -r requirements.txt
RUN pip install flask

CMD ["python", "main.py"]