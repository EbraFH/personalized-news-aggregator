#!/bin/bash
set -e

# Ensure the Dapr binaries are in place
mkdir -p /root/.dapr/bin
cp /usr/local/bin/dapr /root/.dapr/bin/dapr
cp /usr/local/bin/daprd /root/.dapr/bin/daprd

# Start the service with Dapr
exec dapr run --app-id user-service --app-port 5000 --components-path /dapr/components -- python app/__init__.py