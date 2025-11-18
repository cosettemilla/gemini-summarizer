## Gemini Text Summarizer — Case Study
### 1. Executive Summary
#### Problem
Students, researchers, and professionals frequently work with long academic texts, articles, and research documents. Manually summarizing these materials is slow, mentally exhausting, and inefficient—especially when dealing with multiple readings or dense technical content. Many people do not have access to advanced tools that can quickly distill large passages into clear, concise summaries, creating a need for a simple, accessible, and reliable text-summarization solution.

#### Solution
This project provides an easy-to-use, cloud-hosted text-summarization service built around the Google Gemini API. Users send any block of text to a lightweight Flask REST API, which returns a concise, AI-generated summary within seconds. The entire system is containerized with Docker for consistent execution and deployed on Azure Container Instances, allowing anyone to run or scale the service without managing servers. The solution is intentionally minimal, user-friendly, and designed to help anyone who needs fast, accurate summaries—especially students and academic users.

### 2. System Overview
Course Concepts Used: This project applies several core system concepts from the course, including containerization using Docker to ensure reproducible execution, cloud deployment through Azure Container Instances for serverless container hosting, and microservice architecture via a lightweight Flask REST API. It also incorporates secure secrets management using environment variables instead of hard-coded keys, applies DevOps principles through automated builds and consistent run commands, and demonstrates practical API integration by connecting a custom service to the Google Gemini large-language-model API. Together, these concepts form a complete end-to-end deployment pipeline from local development to cloud execution.

Architecture Diagram
<img width="1536" height="1024" alt="ChatGPT Image Nov 17, 2025, 08_46_43 PM" src="https://github.com/user-attachments/assets/95a94a1f-1d2f-45cd-adec-ec863f3eca77" />

Data/Models/Services: The system relies on the Google Gemini API (gemini-2.0-flash), a cloud-hosted text-generation model provided through the Google Generative AI service under Google’s AI Studio Terms of Service. All input data consists of user-provided text sent as a simple JSON string, and no data is stored or logged on disk—summaries are generated in real time and returned as lightweight JSON responses. The application itself is a Flask REST API running inside a Docker container, exposed through two endpoints (`/health` and `/summarize`) and deployed on Azure Container Instances, with the container image stored in Azure Container Registry. Secrets such as the Gemini API key are passed

### 3. How to Run (Local)
#### 1. Create Your .env File
Copy the example file:

cp .env.example .env

Open .env and insert your Gemini API key:

GEMINI_API_KEY=your_key_here

#### 2. Build the Docker Image
docker build -t gemini-api .

#### 3. Run the Container (loads env variables)
docker run -p 8080:8080 --env-file .env gemini-api

#### 4. Health Check
curl http://localhost:8080/health

Expected response:

{"status": "ok"}

#### 5. Test Summarization
curl -X POST http://localhost:8080/summarize \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello this is a test"}'


Expected output:

{"summary": "This is a test message."}

### 4. Design Decisions
Why this concept: This project uses Docker, Flask, and Azure Container Instances because they provide a simple, reliable, and portable way to package and deploy an AI-powered API without managing servers. Docker ensures the app runs consistently across machines, while ACI allows quick, on-demand cloud deployment with minimal configuration. I considered alternatives such as hosting on a full virtual machine, running the model locally, or deploying on AWS ECS or Lambda. However, these options were either more complex, required unnecessary infrastructure management, or were not suitable for running a lightweight containerized service as efficiently. Using Gemini instead of a local LLM was also intentional—local models require GPUs and significantly more resources, while Gemini delivers high-quality summaries through a straightforward API call.

Tradeoffs: In choosing this design, I accepted several tradeoffs. Running the app in a single Azure Container Instance keeps deployment simple and inexpensive, but limits horizontal scalability and can introduce cold-start delays. Using the Gemini API greatly reduces system complexity and avoids the need for local model hosting, but it introduces per-request latency and relies on an external paid service. The codebase is lightweight and maintainable, but the minimal architecture means there is no built-in long-term storage or advanced observability. Overall, the choices favor simplicity and reliability over high performance or enterprise-level scalability.

Security/Privacy: Security is handled primarily through environment-based secrets management. The Gemini API key is never committed to GitHub and is injected at runtime through environment variables. No user data is stored on disk, reducing risk related to data retention. Requests are validated to ensure only text input is passed to the summarizer, and the system performs no logging of submitted content, minimizing PII exposure. While this setup is adequate for a small academic tool, future improvements could include API authentication, encrypted secrets storage, and stricter request validation.

Operations: Operationally, the container logs to stdout, which can be viewed through `az container logs`, providing enough visibility for debugging and monitoring basic behavior. The ACI instance restarts automatically if it exits, but does not autoscale or load-balance, which is a known limitation. Metrics such as CPU/memory usage can be viewed in Azure, but no custom telemetry is included in the application. This setup works well for a lightweight demo or personal tool, but production use would require better monitoring, alerting, and a more scalable compute environment.

### 5. Results & Evaluation
Sample tests: 
Input:
Hello this is a test

Output:
{ "summary": "This is a test message." }

<img width="1069" height="357" alt="Screenshot 2025-11-17 at 8 39 58 PM" src="https://github.com/user-attachments/assets/2d123045-db06-4cc6-ac5c-34f34416d68b" />


<img width="1074" height="323" alt="Screenshot 2025-11-17 at 8 40 03 PM" src="https://github.com/user-attachments/assets/547cde39-3814-4855-b61b-14f5352bc4dd" />


Performance:  Latency: ~300–700ms (Gemini API dependent), Container: 1 CPU, 1 GB RAM

Testing: Local Docker testing, Cloud testing with Azure public IP, Verified error handling (missing key, empty text)

### 6. What’s Next
Right now, the system only summarizes plain text sent in JSON. A major next step would be enabling the API to accept full PDFs, Word documents, and academic papers for automatic extraction and summarization. This matters because most academic content is stored in PDF or DOCX, not raw text. A summarizer that requires copying and pasting text is useful, but a summarizer that accepts whole documents is far more powerful and realistic.

### 7. Links
GitHub Repository: https://github.com/cosettemilla/gemini-summarizer
Public Cloud API Endpoint: http://135.119.248.195:8080/summarize
