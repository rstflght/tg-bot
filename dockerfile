FROM python:3.12.7-slim
ENV TOKEN="Your token here"
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt
COPY app.py /app/app.py
ENTRYPOINT [ "python", "app.py" ]
