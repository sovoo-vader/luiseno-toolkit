
# Luiseño Toolkit Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install OS dependencies for audio support
RUN apt-get update && apt-get install -y     ffmpeg     portaudio19-dev     && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app/main.py", "--server.port=8501", "--server.enableCORS=false"]
