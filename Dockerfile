FROM python:3.10-slim

# Sistem paketləri və asılılıqlar
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    git \
    curl \
    python3-pip \
    && curl -sL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean && rm -rf /var/lib/apt/lists/*


WORKDIR /app
COPY . .

# yt-dlp-ni məcburi ən son versiyaya yeniləyirik
RUN pip install --no-cache-dir -U pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -U yt-dlp

CMD ["bash", "start"]
