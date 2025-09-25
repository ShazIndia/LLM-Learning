# LLM-Learning
This guide will help you create a simple but powerful API using FastAPI that leverages Large Language Models (LLMs) to help troubleshoot problems. The API will accept problem descriptions and return AI-generated solutions.

<img width="3840" height="2263" alt="Untitled diagram _ Mermaid Chart-2025-09-25-170419" src="https://github.com/user-attachments/assets/9a73d768-3e8f-4132-aa69-57a5f8c8528d" />


                                        
<img width="3840" height="2883" alt="Untitled diagram _ Mermaid Chart-2025-09-25-172201" src="https://github.com/user-attachments/assets/7898b446-a1c5-4851-ae9a-4dfbac02b94f" />

┌─────────────────────────────────────────────────────────────┐
│                        CLIENT LAYER                         │
│  (Browser, cURL, Python requests, Mobile App, etc.)        │
└────────────────────────────┬────────────────────────────────┘
                             │ HTTP/JSON
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                   FASTAPI APPLICATION                        │
│                        (main.py)                             │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   /health    │  │ /categories  │  │/troubleshoot │     │
│  │   Endpoint   │  │   Endpoint   │  │   Endpoint   │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└────────────────────────────┬────────────────────────────────┘
                             │
                    ┌────────┴────────┐
                    │                 │
                    ▼                 ▼
┌─────────────────────────┐  ┌──────────────────────────────┐
│     DATA MODELS         │  │      LLM SERVICE             │
│     (models.py)         │  │  (services/llm_service.py)   │
│                         │  │                              │
│ • TroubleshootRequest   │  │ • generate_response()        │
│ • TroubleshootResponse  │  │ • create_prompt()            │
│ • Solution              │  │ • parse_llm_response()       │
│ • ProblemCategory       │  │ • Fallback handlers          │
│ • HealthResponse        │  │                              │
└─────────────────────────┘  └────────────┬─────────────────┘
                                          │
                                          ▼
                             ┌─────────────────────────┐
                             │   EXTERNAL SERVICES     │
                             │                         │
                             │  • OpenAI GPT API       │
                             │  • Rate Limiting        │
                             │  • Token Management     │
                             └─────────────────────────┘
