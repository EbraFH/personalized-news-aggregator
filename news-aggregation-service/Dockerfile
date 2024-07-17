FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Install Dapr CLI and Dapr runtime binaries
RUN apt-get update && apt-get install -y wget curl \
    && wget -q https://github.com/dapr/cli/releases/download/v1.13.0/dapr_linux_amd64.tar.gz \
    && tar -xzf dapr_linux_amd64.tar.gz -C /usr/local/bin \
    && wget -q https://github.com/dapr/dapr/releases/download/v1.13.5/daprd_linux_amd64.tar.gz \
    && tar -xzf daprd_linux_amd64.tar.gz -C /usr/local/bin

# Copy the entrypoint script
COPY entrypoint.sh /app/entrypoint.sh

# Ensure the script is executable
RUN chmod +x /app/entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
