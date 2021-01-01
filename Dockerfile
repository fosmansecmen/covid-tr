FROM python:3.7
WORKDIR /opt/covid-tr
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY guess.py .
CMD python guess.py
EXPOSE 5000/tcp