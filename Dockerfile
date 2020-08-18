FROM pytorch:arm7l

RUN python3 -m pip install alpaca-trade-api

RUN mkdir /workspace
WORKDIR /workspace

COPY src .

CMD ["python3", "main.py"]
