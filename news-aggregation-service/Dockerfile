FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Install Dapr CLI and Dapr runtime binaries
RUN apt-get update && apt-get install -y wget curl \
    && wget -q https://github.com/dapr/cli/releases/download/v1.13.0/dapr_linux_amd64.tar.gz \
    && tar -xzf dapr_linux_amd64.tar.gz -C /usr/local/bin \
    && wget -q https://github.com/dapr/dapr/releases/download/v1.13.5/daprd_linux_amd64.tar.gz \
    && tar -xzf daprd_linux_amd64.tar.gz -C /usr/local/bin \
    && rm *.tar.gz \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]