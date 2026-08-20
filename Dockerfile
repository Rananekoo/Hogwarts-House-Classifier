FROM python:3.11-slim

WORKDIR /app
# Force rebuild to install plotly - 2026-08-20
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
fix: force rebuild for plotly
