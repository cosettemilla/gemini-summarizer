Gemini Text Summarizer — Case Study
1. Executive Summary
Problem
Students, researchers, and professionals frequently work with long academic texts, articles, and documents. Manually summarizing these materials is time-consuming and inefficient.

Solution
This project provides a lightweight, cloud-hosted text-summarization API powered by Google Gemini. A user sends the API a block of text, and it returns a concise summary. The API runs inside a Docker container and is deployed on Azure Container Instances for scalable, on-demand access.

2. System Overview
Course Concepts Used

Docker Containers – for consistent packaging and reproducible execution

Cloud Deployment (Azure Container Instances) – running containers in the cloud

APIs & Microservices – serving functionality through HTTP endpoints

Secrets Management – environment variables for API keys

Architecture Diagram

(Place your architecture PNG in /assets and add it here, e.g.)

![Architecture Diagram](assets/architecture.png)

Data / Models / Services

Google Gemini API

Provides: text summarization

Model called via: google-generativeai Python package

Data format: JSON input containing arbitrary text

Service Output

JSON response with the generated summary

No local datasets are stored; all summarization is done dynamically.

3. How to Run (Local)
Environment Variable
export GEMINI_API_KEY="your_key_here"

Build
docker build -t gemini-api .

Run
docker run -p 8080:8080 --env GEMINI_API_KEY=$GEMINI_API_KEY gemini-api

Health Check
curl http://localhost:8080/health

4. Design Decisions
Why These Tools?

Docker: Ensures identical behavior across laptops, VMs, and cloud services.

Azure Container Instances (ACI): Offers simple container hosting without managing servers.

Gemini API: Provides high-quality text summarization via a simple API.

Alternatives Considered

AWS ECS / Lambda – more complex setup for this project scope

Local LLMs – too heavy, require GPUs

Running directly on VM – less portable than containers

Tradeoffs

Cloud cost vs. local execution

Simplicity of single-container deployment vs. scalability limits

No database allows minimal complexity but limits long-term storage features

Security / Privacy

API key stored in environment variables (not committed to GitHub)

No user data stored on disk

Only text in request is processed and returned

Operations

Logging handled in container stdout (viewed via az container logs)

Container restarts automatically via ACI policy

Known limitation: cold-start time when redeployed

5. Results & Evaluation
Sample Output

Input:

"Hello this is a test"


Output:

{
  "summary": "This is a test message."
}

Performance

Response latency: ~300–700ms (depends on Gemini API)

Resource usage: 1 CPU, 1 GB memory container

Testing

Verified working locally via Docker

Verified working in cloud via Azure public IP

Confirmed expected error handling when key missing or text empty

6. What’s Next

Add a frontend UI (React or simple HTML)

Add PDF / DOCX uploading for summarization

Add authentication tokens for users

Add multi-paragraph or multi-section structured summaries

Add rate limiting and usage analytics

Deploy using Azure App Service or Kubernetes for autoscaling

7. Links
GitHub Repository

https://github.com/cosettemilla/gemini-summarizer

Public Cloud Endpoint (Live API)
http://<YOUR_CONTAINER_IP>:8080/summarize