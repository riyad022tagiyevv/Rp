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

# Git xətasını (silent) həll etmək üçün mühit dəyişəni
[span_3](start_span)[span_4](start_span)ENV GIT_PYTHON_REFRESH=quiet[span_3](end_span)[span_4](end_span)

# İş faylları
WORKDIR /app
COPY . .

# Python paketləri
RUN pip install --no-cache-dir -r requirements.txt

# Start
CMD ["bash", "start"]
