# LLM-Learning
This guide will help you create a simple but powerful API using FastAPI that leverages Large Language Models (LLMs) to help troubleshoot problems. 

The API will accept problem descriptions and return AI-generated solutions.

┌─────────────────┐    HTTP Request    ┌─────────────────┐
│                 │ ──────────────────► │                 │
│   Client/User   │                     │   FastAPI App   │
│                 │ ◄────────────────── │                 │
└─────────────────┘    JSON Response   └─────────────────┘
                                                │
                                                │ API Call
                                                ▼
                                        ┌─────────────────┐
                                        │                 │
                                        │   LLM Service   │
                                        │  (OpenAI/etc)   │
                                        │                 │
                                        └─────────────────┘
