from python:3.8

WORKDIR /var/app

COPY requirements.txt /var/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /var/app
CMD ./run.sh
