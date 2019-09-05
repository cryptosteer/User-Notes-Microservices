FROM python:3.7
ADD . /app
WORKDIR /app
EXPOSE 4002
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python","index.py"]
