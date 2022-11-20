FROM python:3.10-slim
WORKDIR /app
RUN adduser --system --group app # && chown app /app
# USER app
RUN mkdir data
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]