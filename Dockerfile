FROM python:3.10-slim

WORKDIR /app

# Install CPU-only torch first (avoids pulling ~2GB CUDA build)
RUN pip install --no-cache-dir \
    torch --index-url https://download.pytorch.org/whl/cpu

# Install remaining dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/
COPY app.py .

# Copy trained model artifacts
COPY models/ ./models/

CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
