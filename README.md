Gemini Text Summarizer — Case Study
1. Executive Summary
Problem

Students, researchers, and professionals often work with long academic texts, articles, and research documents. Manually summarizing this material is time-consuming and inefficient.

Solution

This project provides a lightweight, cloud-hosted text-summarization API powered by Google Gemini. Users send the API a block of text and receive a concise summary.
The application runs inside a Docker container and is deployed on Azure Container Instances (ACI) for scalable, on-demand access.

2. System Overview
Course Concepts Used

Docker containers

Azure Container Instances (ACI)

REST APIs & Microservices

Secrets management using environment variables

Architecture Diagram

(Add your architecture PNG to /assets and embed it here.)

3. How to Run (Local)
Set your environment variable
export GEMINI_API_KEY="your_key_here"

Build
docker build -t gemini-api .

Run
docker run -p 8080:8080 --env GEMINI_API_KEY=$GEMINI_API_KEY gemini-api

Health Check
curl http://localhost:8080/health

4. Design Decisions
Why These Tools?

Docker: Ensures consistent, reproducible execution across environments.

Azure Container Instances: Simplifies cloud deployment without managing VMs.

Google Gemini API: Provides fast, high-quality summarization.

Alternatives Considered

AWS ECS or Lambda (more complex for the course project)

Local LLMs (heavy compute requirements)

VM deployment (less portable, harder to manage)

Tradeoffs

Cloud hosting costs vs. convenience

Simpler architecture but limited long-term storage

Single container = low complexity but no autoscaling

Security & Privacy

API key stored via environment variables

No user text is saved to disk

Only temporary request data is processed

Operations

Logs accessed via az container logs

ACI restarts automatically

Known limitation: cold start after redeployment

5. Results & Evaluation
Sample Output

Input:

Hello this is a test


Output:

{
  "summary": "This is a test message."
}

Performance

Response latency: ~300–700 ms

Resource usage: 1 CPU, 1 GB memory container

Testing

Fully tested locally using Docker

Cloud API verified using Azure public IP

Verified error handling for missing/invalid keys

6. What’s Next

Add a frontend UI

Add PDF / DOCX uploading

Add user authentication

Add structured multi-section summaries

Add rate limiting and analytics

Deploy using Azure App Service or Kubernetes

7. Links

GitHub Repository:
https://github.com/cosettemilla/gemini-summarizer

Public Cloud Endpoint:
http://<YOUR_CONTAINER_IP>:8080/summarize
