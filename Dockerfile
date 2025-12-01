FROM python:3.10-slim

# FFmpeg quraşdırılması
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# İş faylları
WORKDIR /app
COPY . .

# Python paketləri
RUN pip install --no-cache-dir -r requirements.txt

# Start
CMD ["bash", "start"]
