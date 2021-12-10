FROM python:3

LABEL Author="Jay Shepherd"
LABEL E-mail="jaykshepherd92@gmail.com"
LABEL version="0.0.1"

ENV FLASK_APP "money_mover"
ENV FLASK_ENV "production"
ENV FLASK_DEBUG True

RUN mkdir /money_mover
WORKDIR /money_mover
ADD requirements.txt /money_mover/
RUN pip install -r requirements.txt
ADD . /money_mover/
RUN make dummy_data
EXPOSE 5000

CMD flask run --host=0.0.0.0