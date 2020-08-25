FROM joeyschentrup/pytorch:arm7l

RUN apt-get update && apt-get install -y cron

RUN python3 -m pip install alpaca-trade-api

RUN mkdir /workspace
WORKDIR /workspace

#Cron set up
COPY config/auto-trader-crontab /etc/cron.d/auto-trader-crontab
RUN chmod 0644 /etc/cron.d/auto-trader-crontab
RUN crontab /etc/cron.d/auto-trader-crontab
RUN touch /var/log/cron.log
CMD cron && tail -f /var/log/cron.log

COPY src .
