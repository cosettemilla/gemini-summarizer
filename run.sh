#!/bin/bash
docker build -t gemini-summarizer .
docker run --rm \
  -v "$(pwd)/data:/data" \
  --env-file .env \
  gemini-summarizer
