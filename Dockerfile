FROM python:3.11-slim

WORKDIR /app

# Force rebuild 2026-08-20-v2
COPY requirements.txt .

# 先装 requirements.txt 里的，再强制单独装一次 plotly 保底
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir plotly

COPY . .

EXPOSE 8080

CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]

