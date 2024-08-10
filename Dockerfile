FROM python
LABEL authors="sergey.alekseev"

WORKDIR /app
RUN pip install --upgrade --no-cache pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
RUN chmod +x entrypoint.sh
CMD ["./entrypoint.sh"]