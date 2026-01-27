#!/usr/bin/env bash

echo "Starting NovaAI Nexus Honeypot API..."
uvicorn app:app --host 0.0.0.0 --port 10000