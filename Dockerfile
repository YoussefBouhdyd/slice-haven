FROM python:3.13
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
# RUN flask db init 
# RUN db migrate -m "initial migration"
# RUN flask db upgrade
# RUN python seeds.py
CMD ["python", "run.py"]