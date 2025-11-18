## Gemini Text Summarizer — Case Study
### 1. Executive Summary
#### Problem
Students, researchers, and professionals often work with long academic texts, articles, and research documents. Manually summarizing this material is time-consuming and inefficient.

#### Solution
This project provides a lightweight, cloud-hosted text-summarization API powered by Google Gemini.
Users send the API a block of text and receive a concise summary.
The application runs inside a Docker container and is deployed on Azure Container Instances (ACI) for scalable, on-demand access.

### 2. System Overview
Course Concepts Used: Docker containers, Azure Container Instances (ACI), REST APIs & Microservices, Secrets management via environment variables

Architecture Diagram
(Add your architecture PNG to /assets and embed it here.)

### 3. How to Run (Local)
#### Set your environment variable
export GEMINI_API_KEY="your_key_here"

#### Build
docker build -t gemini-api .

#### Run
docker run -p 8080:8080 --env GEMINI_API_KEY=$GEMINI_API_KEY gemini-api

#### Health Check
curl http://localhost:8080/health

### 4. Design Decisions
#### Why These Tools?
Docker: Ensures reproducible, portable execution.
Azure Container Instances: Simple container hosting without managing servers.
Gemini API: High-quality summarization with minimal setup.

#### Alternatives Considered
AWS ECS / Lambda – more complex for this project
Local LLMs – require GPU, too heavy
VM hosting – less portable than containers

#### Tradeoffs
Cloud cost vs. local execution
Single-container simplicity vs. limited autoscaling
No database = low complexity but no persistent storage

#### Security / Privacy
API key stored in environment variables
No user text stored on disk
No PII retained

#### Operations
Logs accessible via az container logs
Automatic restarts via ACI
Cold starts when redeployed

### 5. Results & Evaluation
#### Sample Output
Input:
Hello this is a test

Output:
{ "summary": "This is a test message." }

#### Performance
Latency: ~300–700ms (Gemini API dependent)
Container: 1 CPU, 1 GB RAM

#### Testing
Local Docker testing
Cloud testing with Azure public IP
Verified error handling (missing key, empty text)

### 6. What’s Next
Add a frontend UI
Add PDF/DOCX upload summarization
Add API authentication tokens
Add structured multi-section summaries
Add usage analytics & rate limiting
Deploy to App Service or Kubernetes for scaling

### 7. Links
GitHub Repository: https://github.com/cosettemilla/gemini-summarizer
Public Cloud API Endpoint: http://135.119.248.195:8080/summarize
