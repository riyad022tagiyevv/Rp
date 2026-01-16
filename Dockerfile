FROM python:3.10-slim

# Node.js, Git və FFmpeg quraşdırılması
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    git \
    curl \
    && curl -sL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean && rm -rf /var/lib/apt/lists/*


# İş faylları
WORKDIR /app
COPY . .

# Python paketləri
RUN pip install --no-cache-dir -r requirements.txt

# Start
CMD ["bash", "start"]

