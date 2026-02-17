# Enterprise AI – Reference Implementation

![Architecture](https://img.shields.io/badge/pattern-Enterprise%20AI%20Platform-blue)
![Version](https://img.shields.io/badge/python-3.10+-purple)


***Created by: [Suyog Hire - Solutions Architect](https://linkedin.com/in/suyoghire)***

---

**Minimal runnable** *Enterprise AI Platform* **reference implementation**.

## Key components

- Model routing
- Cost guardrails
- Governance enforcement
- Provider abstraction
- Extensible architecture

---

## Features

- FastAPI service
- Pluggable model providers
- Budget enforcement
- Basic PII check
- Routing based on complexity
- Typed schemas (Pydantic)
- Unit test example

---

### **In Scope**

It is a minimal runnable, self-contained platform implementation - for reference purposes only.

### **Exclusion**

The following are excluded to keep the example simple and focused:

-   **Production-grade error handling** (e.g., retries, rate limiting, API downtime recovery).
-   **Authentication** (e.g. OAuth, service accounts, or multi-key rotation).
-   **Actual LLM Response** (OpenAI API calls)
-   **Logging, monitoring, or observability** integrations.
-   **Web UI, CLI interface, or input validation** for user prompts.
-   **Containerization** (Docker) or deployment configurations (CI/CD, cloud providers).
-   **Multi-model support** or dynamic model selection.


### Run Locally
[![ai-reference-implementation](https://img.shields.io/badge/GitHub-ai--reference--implementation-purple?style=flat&logo=github)](https://github.com/intarchs111/ai-gateway)

```bash
git clone https://github.com/intarchs111/ai-reference-implementation.git
cd ai-reference-implementation
```

**1. Create Virtual Environment (Optional)**
```bash
python -m venv venv
venv\Scripts\activate
```
**2. Install Dependencies**
```bash
pip install -e .
uvicorn app.main:app --reload
```

**3. Start the server:**
```bash
uvicorn app.main:app --reload
```

**4. Open in browser:**   http://localhost:8000/docs

**5. Test the Endpoint** 

`POST /generate`

**Sample Request Body:**
```json
{
  "prompt": "Explain routing logic",
  "complexity": "low",
  "estimated_cost": 0.01
}
```

**Expected response:**

```json
{
  "output": "[Mock response] Explain routing logic",
  "model": "mock-model"
}
```

**6. Test High Complexity Routing**

**Request:**
```json
{
  "prompt": "Design distributed systems architecture",
  "complexity": "high",
  "estimated_cost": 0.02
}
```
**Expected response:**
```json
{
  "output": "[OpenAI simulated response] Design distributed systems architecture",
  "model": "openai-model"
}
```

**7. Test Budget Guardrail**

The configured daily budget is:
```bash
DAILY_BUDGET = 100.0
```

To simulate failure, repeatedly send requests with large `estimated_cost`.

Once exceeded, expected response:
```bash
Exception: Daily budget exceeded
```
##
<div align="center">

### **Suyog Hire** | **AI Solutions Architect**
[![github-profile](https://img.shields.io/badge/GitHub-grey?style=flat&logo=github)](https://github.com/intarchs111) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/suyoghire)

</div>
