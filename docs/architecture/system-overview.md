# FinSight AI - System Architecture

## 1. Application Architecture

FinSight AI follows a Modular Monolith architecture.

## 2. Core Components

- API Layer: Handles HTTP requests.
- Service Layer: Implements business logic.
- Repository Layer: Manages data access.
- Database Layer: Stores application data.
- AI Layer: Implements RAG and LLM workflows.
- ML Layer: Implements transaction anomaly detection.
- Frontend: Provides the user interface.

## 3. AI Capabilities

- Document ingestion
- Text extraction
- Text chunking
- Embedding generation
- Vector similarity search
- Retrieval-Augmented Generation
- Transaction anomaly detection
- AI-assisted investigation

## 4. Infrastructure

- Docker
- PostgreSQL
- pgvector
- Redis
- Celery
- Ollama
- AWS