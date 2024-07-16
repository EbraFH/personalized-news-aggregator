FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Install Dapr CLI
RUN apt-get update && apt-get install -y wget
RUN wget -q https://raw.githubusercontent.com/dapr/cli/master/install/install.sh -O install.sh && chmod +x install.sh && ./install.sh

CMD ["dapr", "run", "--app-id", "news-aggregation-service", "--app-port", "5002", "--resources-path", "/dapr/components", "--", "python", "app/__init__.py"]
