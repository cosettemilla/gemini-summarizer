# Gemini Text Summarizer — Systems Final Project

## 1. Executive Summary

### Problem  
Students, researchers, and professionals frequently work with long academic papers, articles, and dense research documents. Manually summarizing these materials is slow, tiring, and inefficient—especially when dealing with multiple readings. There is a clear need for a simple, reliable tool that quickly converts long text into clear, concise summaries.

### Solution  
This project provides a lightweight, cloud-hosted text-summarization service powered by the Google Gemini API. Users send text to a Flask REST API, which returns an AI-generated summary within seconds.  
The entire system is containerized with Docker for reproducibility and deployed on Azure Container Instances for simple cloud hosting without managing servers.

---

## 2. System Overview

### Course Concepts Used  
This project integrates several core concepts from the course:

- **Docker Containerization** — ensuring reproducible execution across environments  
- **Microservices / REST APIs** — clean separation of concerns through a Flask API  
- **Cloud Deployment (Azure Container Instances)** — serverless container hosting  
- **Secrets Management** — environment variables instead of hard-coded keys  
- **DevOps Practices** — consistent build/run commands and container workflows  
- **External API Integration** — connecting to the Google Gemini LLM API  

These combine into a full pipeline: local dev → containerization → cloud deployment.

---

### Architecture Diagram  
*(Image stored in /assets — example shown below)*  

<img width="700" alt="Architecture Diagram" src="https://github.com/user-attachments/assets/95a94a1f-1d2f-45cd-adec-ec863f3eca77">

---

### Data / Models / Services  
The system relies entirely on **real-time API calls** rather than local datasets.

- **Model:** Google Gemini (gemini-2.0-flash)  
- **Format:** JSON request (`{"text": "..."}`) and JSON response  
- **License:** Google Generative AI terms via AI Studio  
- **Service:** Flask microservice inside a Docker container  
- **Cloud:** Azure Container Registry + Azure Container Instances  
- **Storage:** No user text or data is saved — everything is processed in memory  
- **Secrets:** API key stored in `.env` and injected at runtime  

---

## 3. How to Run (Local)

### 1. Create your `.env` file  
Copy the example:

```bash
cp .env.example .env
Then edit .env:

ini
Copy code
GEMINI_API_KEY=your_key_here
2. Build the Docker image
bash
Copy code
docker build -t gemini-api .
3. Run the container
bash
Copy code
docker run -p 8080:8080 --env-file .env gemini-api
4. Health Check
bash
Copy code
curl http://localhost:8080/health
Expected:

json
Copy code
{"status": "ok"}
5. Summarize Text
bash
Copy code
curl -X POST http://localhost:8080/summarize \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello this is a test"}'
Expected:

json
Copy code
{"summary": "This is a test message."}
4. Design Decisions
Why This Approach
Docker ensures reproducibility, Flask keeps the API lightweight, and Azure Container Instances make cloud deployment simple without provisioning VMs. Gemini provides high-quality summarization while avoiding the heavy compute required for hosting local LLMs.
Alternatives like AWS ECS/Lambda or self-hosting models were rejected due to complexity, cost, or hardware requirements.

Tradeoffs
Performance: Reliant on Gemini API latency (300–700ms).

Cost: API usage cost + Azure compute.

Simplicity vs. Scalability: Single container, no autoscaling.

Maintainability: Very small codebase, easy to extend, but minimal logging/observability.

Security & Privacy
Secrets stored in .env, not in GitHub

No text stored on disk

Only minimal request data is processed

No PII retention

Operations
Logs visible with docker logs or az container logs

ACI auto-restarts on failure

No autoscaling or deep metrics (a known limitation)

5. Results & Evaluation
Example Summary Test
Input:

kotlin
Copy code
Hello this is a test
Output:

json
Copy code
{ "summary": "This is a test message." }
Screenshots
<img width="886" alt="Screenshot 1" src="https://github.com/user-attachments/assets/34145b97-45b0-4d4b-a457-6e3642ee9fca" /> <img width="759" alt="Screenshot 2" src="https://github.com/user-attachments/assets/d7a319a9-1610-4ca6-bad3-182ded8f0dcc" />
Performance
Latency: 300–700ms (Gemini dependent)

Container resources: 1 CPU, 1 GB RAM

Testing
Local Docker tests

Cloud deployment tests

Validation for missing key, empty text, etc.

6. What’s Next
The biggest improvement would be adding document ingestion: PDFs, DOCX, academic papers, and multi-page uploads.
This would transform the tool from a text-only summarizer into a real academic assistant capable of summarizing full research articles automatically — the most common real-world use case.

Future enhancements:

Web UI for drag-and-drop uploads

User accounts + rate limiting

Multi-section structured summaries

Deployment on Azure App Service or Kubernetes for autoscaling

7. Links
GitHub Repository:
https://github.com/cosettemilla/gemini-summarizer

Public Cloud API Endpoint:
http://135.119.248.195:8080/summarize

yaml
Copy code
