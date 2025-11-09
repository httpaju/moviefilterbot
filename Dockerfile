
FROM python:3.10.8


RUN apt update && apt upgrade -y
RUN apt install git -y


WORKDIR /VJ-FILTER-BOT


COPY requirements.txt .
RUN pip3 install -U pip && pip3 install -U -r requirements.txt


COPY . .


RUN chmod +x /VJ-FILTER-BOT/start.sh


CMD [ "./start.sh" ]
