FROM python:3

LABEL Author="Jay Shepherd"
LABEL E-mail="jaykshepherd92@gmail.com"
LABEL version="0.0.1"

ENV FLASK_APP "money_mover.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/
RUN make dummy_data
EXPOSE 5000

CMD flask run --host=0.0.0.0