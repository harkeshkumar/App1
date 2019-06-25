From frolvlad/alpine-python3

LABEL maintainer="harkeshsaini21@gmail.com"

WORKDIR /src
COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]