<!-- # FinSight AI

Intelligent Financial Operations & Risk Intelligence Platform.

## Overview

FinSight AI is an AI-powered financial intelligence platform combining:

- Retrieval-Augmented Generation (RAG)
- Machine Learning
- Transaction Anomaly Detection
- AI-powered Financial Assistant
- Intelligent Investigation Workflows

## Project Status

Under active development.

## Architecture

Documentation will be added as the system architecture evolves.

## Technology Stack

- Python
- FastAPI
- PostgreSQL
- pgvector
- Redis
- Celery
- Ollama
- React
- Docker
- AWS
 -->


# FinSight AI
## Intelligent Financial Operations & Risk Intelligence Platform

![Status](https://img.shields.io/badge/Project-Active%20Development-blue)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688)
![Database](https://img.shields.io/badge/Database-PostgreSQL-336791)
![AI](https://img.shields.io/badge/AI-LLM%20%7C%20RAG%20%7C%20ML-purple)
![Tests](https://img.shields.io/badge/Tests-16%20Passing-success)

> **FinSight AI** is an AI-powered financial intelligence platform designed to combine document intelligence, transaction risk analysis, and evidence-grounded AI assistance into one unified application.

**Project Type:** Enterprise-style AI Engineering Proof of Concept  
**Development Status:** Active Development  
**Architecture:** Modular Monolith  
**Primary Goal:** Build a practical, explainable, and extensible AI platform for financial operations and risk intelligence.

---

# 1. Executive Summary

Financial organizations work with large volumes of financial documents, transaction records, policies, invoices, and operational information.

Extracting meaningful information from these sources, identifying unusual transaction patterns, and preparing investigation summaries can involve significant manual effort.

FinSight AI aims to address these challenges through a unified AI-powered platform.

The platform combines:

- Financial document processing and intelligence.
- Retrieval-Augmented Generation (RAG).
- Semantic search and vector retrieval.
- Machine-learning-based anomaly detection.
- Transaction risk scoring and explainability.
- LLM-powered financial assistance.
- Controlled AI tool execution.
- Investigation workflows and auditability.

The project is being developed incrementally, beginning with backend engineering and database foundations before implementing the AI capabilities.

**The objective is not simply to integrate an LLM into an API. It is to engineer a complete AI-enabled application with reliable data pipelines, controlled AI behaviour, explainability, testing, and operational considerations.**

---

# 2. Business Problem

Financial operations and risk teams often work with information distributed across multiple systems and documents.

This creates several challenges:

1. **Fragmented information:** Financial information is distributed across invoices, policies, transaction records, and operational documents.
2. **Manual information retrieval:** Finding relevant evidence across multiple documents takes time.
3. **Risk identification:** Unusual transaction patterns can be difficult to identify consistently.
4. **Limited explainability:** Risk scores and AI-generated responses need supporting evidence.
5. **Investigation overhead:** Preparing investigation summaries and maintaining evidence trails can be time-consuming.
6. **Information reliability:** AI-generated answers must be grounded in reliable information rather than unsupported assumptions.

FinSight AI explores how AI and conventional software engineering can work together to improve these workflows.

---

# 3. Product Vision and Core Modules

The platform is divided into five major functional areas.

## 3.1 Financial Document Intelligence

**Objective:** Convert unstructured financial documents into searchable, usable information.

Planned capabilities:

- Upload financial PDF documents.
- Validate file type, size, and integrity.
- Store original documents securely.
- Extract text page by page.
- Clean and preprocess extracted content.
- Split text into overlapping chunks.
- Generate vector embeddings.
- Store embeddings for semantic retrieval.
- Retrieve relevant document passages.
- Generate context-aware responses using RAG.
- Provide document and page-level citations.

**Expected outcome:** Users can ask questions about financial documents and receive answers supported by traceable source information.

## 3.2 Transaction Intelligence and Risk Analysis

**Objective:** Identify potentially unusual financial transaction patterns.

Planned capabilities:

- Generate and process synthetic transaction datasets.
- Perform data preprocessing and feature engineering.
- Implement rule-based anomaly detection.
- Explore machine-learning anomaly detection.
- Generate transaction risk scores.
- Identify unusual transaction behaviour.
- Explain the signals contributing to risk scores.
- Evaluate model performance using appropriate metrics.

**Expected outcome:** Potentially suspicious transactions can be prioritized for human investigation with understandable risk indicators.

## 3.3 AI Financial Assistant

**Objective:** Provide an AI interface for interacting with financial information.

Planned capabilities:

- Natural-language questions about uploaded documents.
- Retrieval-based financial knowledge assistance.
- Controlled transaction analytics.
- Approved application-tool execution.
- Evidence-based investigation summaries.
- Structured AI responses.
- Source references and response validation.
- Handling of unsupported questions.

The assistant will use controlled tools and approved application interfaces rather than unrestricted database access.

## 3.4 Investigation and Case Management

**Objective:** Support structured financial investigations.

Planned capabilities:

- Create investigation cases.
- Associate transactions and documents with cases.
- Record risk indicators.
- Maintain supporting evidence.
- Generate investigation summaries.
- Support human review and approval.
- Maintain investigation history and audit trails.

## 3.5 Enterprise Engineering and Infrastructure

**Objective:** Build the platform using reliable software engineering practices.

Planned capabilities:

- REST API architecture.
- Authentication and authorization.
- Role-based access control.
- Database migrations.
- Background processing.
- Logging and monitoring.
- Error handling.
- Automated testing.
- Docker-based development.
- CI/CD pipelines.
- Cloud deployment.

---

# 4. High-Level System Architecture

The initial implementation follows a **Modular Monolith Architecture**.

This approach keeps development and deployment manageable while separating business responsibilities into independent modules.

```text
                       USER / CLIENT
                             |
                             v
                      REACT FRONTEND
                             |
                             v
                      FASTAPI BACKEND
                             |
          +------------------+------------------+
          |                  |                  |
          v                  v                  v
   DOCUMENT MODULE     TRANSACTION MODULE   INVESTIGATION
          |                  |                  |
          v                  v                  v
   PDF PROCESSING       FEATURE ENGINEERING  CASE MANAGEMENT
   TEXT EXTRACTION      ANOMALY DETECTION     EVIDENCE TRACKING
   TEXT CHUNKING        RISK SCORING          AUDIT HISTORY
          |                  |                  |
          +------------------+------------------+
                             |
                             v
                    AI ORCHESTRATION LAYER
                             |
                +------------+------------+
                |                         |
                v                         v
           RETRIEVAL / RAG           CONTROLLED TOOLS
                |                         |
                v                         v
          VECTOR SEARCH             ANALYTICS TOOLS
                |                         |
                +------------+------------+
                             |
                             v
                       LOCAL LLM
                          OLLAMA

---------------------------------------------------------
                    DATA INFRASTRUCTURE
---------------------------------------------------------

 PostgreSQL       : Relational database
 pgvector         : Vector storage and similarity search
 Redis            : Cache and task infrastructure
 Local Storage    : Original financial documents
 Docker           : Containerized environment
 GitHub Actions   : CI/CD (planned)
 AWS              : Cloud deployment (planned)
---------------------------------------------------------
```

### Architecture Decisions

| Decision | Rationale |
|---|---|
| Modular monolith | Avoid premature microservice complexity |
| FastAPI | Modern Python API framework |
| PostgreSQL | Reliable relational data storage |
| pgvector | Vector similarity search within PostgreSQL |
| Ollama | Local-first LLM execution |
| Sentence Transformers | Local embedding generation |
| Redis | Caching and asynchronous task infrastructure |
| Local storage abstraction | Future migration to S3 or object storage |
| Pydantic | Request validation and structured data |
| SQLAlchemy | Database abstraction and ORM |

The architecture diagram represents the target system. Not every component has been implemented yet.

---

# 5. Technology Stack

| Category | Technology | Current Status |
|---|---|---|
| Programming Language | Python 3.12 | In use |
| Backend Framework | FastAPI | Implemented |
| Data Validation | Pydantic | In use |
| ORM | SQLAlchemy 2.x | Implemented |
| Database | PostgreSQL 17 | Running locally |
| Database Migrations | Alembic | Initial migration applied |
| PDF Processing | PyMuPDF | Installed |
| File Upload | python-multipart | Installed |
| Testing | PyTest | In use |
| API Testing | HTTPX | In use |
| LLM Runtime | Ollama | Selected |
| LLM Model | Llama 3.2 3B | Selected |
| Embeddings | Sentence Transformers | Planned |
| Vector Database | pgvector | Planned |
| Cache | Redis | Planned |
| Background Jobs | Celery | Planned |
| Frontend | React | Planned |
| Containerization | Docker | In use |
| Version Control | Git/GitHub | In use |
| CI/CD | GitHub Actions | Planned |
| Cloud | AWS | Planned |

---

# 6. Development Progress Tracker

This section reflects the actual implementation status, not just the intended architecture.

**Status definitions**

- **Completed:** Implemented and verified.
- **In Progress:** Development has started but the milestone is not complete.
- **Not Started:** Planned but implementation has not started.

## Phase 1 — Engineering and Backend Foundation

| # | Module | Deliverables | Status |
|---|---|---|---|
| 1 | Project Setup | Repository, Python environment, project structure | Completed |
| 2 | Version Control | Git workflow, feature branches, GitHub integration | Completed |
| 3 | Backend Foundation | FastAPI application and API routing | Completed |
| 4 | Configuration | Centralized application configuration | Completed |
| 5 | Database Foundation | PostgreSQL and SQLAlchemy integration | Completed |
| 6 | Database Migrations | Alembic initialization and initial migration | Completed |
| 7 | Document Registry | Register, retrieve, and list document metadata | Completed |
| 8 | Automated Testing | Backend tests and database test fixtures | Completed |

## Phase 2 — Document Ingestion

| # | Module | Deliverables | Status |
|---|---|---|---|
| 9 | Ingestion Data Models | Document, page, and chunk models | In Progress |
| 10 | Database Migration | Migration for page/chunk tables and storage path | In Progress |
| 11 | PDF Upload API | Secure document upload endpoint | Not Started |
| 12 | File Validation | Type, size, signature, and integrity validation | Not Started |
| 13 | File Storage | Secure local storage abstraction | Not Started |
| 14 | PDF Extraction | Page-wise text extraction | Not Started |
| 15 | Text Processing | Text cleaning and normalization | Not Started |
| 16 | Text Chunking | Chunk generation, overlap, and page references | Not Started |

## Phase 3 — Embeddings and Retrieval

| # | Module | Deliverables | Status |
|---|---|---|---|
| 17 | Embedding Model | Local embedding model integration | Not Started |
| 18 | Vector Storage | pgvector integration | Not Started |
| 19 | Semantic Search | Similarity-based document retrieval | Not Started |
| 20 | Retrieval Optimization | Retrieval quality and relevance improvements | Not Started |

## Phase 4 — RAG and AI Assistant

| # | Module | Deliverables | Status |
|---|---|---|---|
| 21 | RAG Pipeline | Retrieval and context construction | Not Started |
| 22 | LLM Integration | Local LLM integration | Not Started |
| 23 | Grounded Responses | Evidence-based response generation | Not Started |
| 24 | Source Citations | Document and page references | Not Started |
| 25 | Evaluation | Retrieval and answer-quality evaluation | Not Started |
| 26 | AI Assistant | Natural-language financial Q&A | Not Started |
| 27 | Tool Calling | Controlled application tool execution | Not Started |

## Phase 5 — Transaction Intelligence

| # | Module | Deliverables | Status |
|---|---|---|---|
| 28 | Transaction Dataset | Synthetic financial transaction data | Not Started |
| 29 | Feature Engineering | Transaction feature extraction | Not Started |
| 30 | Anomaly Detection | Rule-based and ML-based detection | Not Started |
| 31 | Risk Scoring | Transaction risk prioritization | Not Started |
| 32 | Explainability | Risk signal explanations | Not Started |
| 33 | Model Evaluation | Metrics and evaluation framework | Not Started |

## Phase 6 — Investigation Workflows

| # | Module | Deliverables | Status |
|---|---|---|---|
| 34 | Case Management | Investigation creation and tracking | Not Started |
| 35 | Evidence Management | Document and transaction associations | Not Started |
| 36 | Investigation Summary | AI-assisted evidence summaries | Not Started |
| 37 | Human Review | Review and approval workflow | Not Started |
| 38 | Audit Trail | Investigation activity history | Not Started |

## Phase 7 — Frontend and Enterprise Features

| # | Module | Deliverables | Status |
|---|---|---|---|
| 39 | Frontend Foundation | React application | Not Started |
| 40 | User Authentication | Authentication and session management | Not Started |
| 41 | Authorization | Role-based access control | Not Started |
| 42 | Dashboard | Financial intelligence dashboard | Not Started |
| 43 | Document Interface | Upload and document Q&A interface | Not Started |
| 44 | Investigation Interface | Risk and case management UI | Not Started |

## Phase 8 — Production Engineering and Deployment

| # | Module | Deliverables | Status |
|---|---|---|---|
| 45 | Background Processing | Async task execution | Not Started |
| 46 | Logging and Monitoring | Observability and error tracking | Not Started |
| 47 | Security Hardening | Input security and access controls | Not Started |
| 48 | Performance | API and retrieval optimization | Not Started |
| 49 | Dockerization | Full application containerization | Not Started |
| 50 | CI/CD | Automated build and test pipeline | Not Started |
| 51 | Cloud Deployment | AWS deployment | Not Started |
| 52 | Documentation | Architecture and operational documentation | In Progress |
| 53 | Final Demonstration | End-to-end product demonstration | Not Started |

---

# 7. Current Engineering Checkpoint

**Latest verified position**

| Area | Current State |
|---|---|
| Python environment | Python 3.12 configured |
| FastAPI | Application foundation implemented |
| PostgreSQL | Local PostgreSQL 17 container running |
| SQLAlchemy | ORM configured |
| Alembic | Initial documents migration applied |
| Document API | Register, retrieve, and list operations implemented |
| Document models | Three models registered in SQLAlchemy metadata |
| Automated tests | 16 tests passing |
| PDF processing | PyMuPDF installed |
| File storage | Local storage directory created and Git-ignored |
| RAG | Not implemented |
| Embeddings | Not implemented |
| Transaction ML | Not implemented |
| Frontend | Not implemented |

### Current implementation details

The following database models are currently registered:

```text
documents
document_pages
document_chunks
```

The document model contains metadata and a storage-path field.

The page model is designed to store extracted text for each PDF page.

The chunk model is designed to store chunked text and source page ranges.

The next database migration has not yet been generated or applied.

**Current blocker:** The latest Alembic verification attempt encountered PostgreSQL password-authentication failure for the application database user. Local database configuration is being investigated.

**Existing test result:** 16 tests passed. The latest test run also reported one non-blocking Starlette deprecation warning related to HTTPX.

---

# 8. Repository Structure

```text
finsight-ai/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   ├── core/
│   │   ├── database/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── repositories/
│   │   ├── services/
│   │   │
│   │   ├── ai/
│   │   │   ├── ingestion/
│   │   │   ├── embeddings/
│   │   │   ├── retrieval/
│   │   │   ├── rag/
│   │   │   ├── agents/
│   │   │   └── evaluation/
│   │   │
│   │   └── ml/
│   │       ├── models/
│   │       ├── features/
│   │       └── evaluation/
│   │
│   ├── alembic/
│   ├── tests/
│   └── requirements.txt
│
├── frontend/
│
├── infrastructure/
│   └── docker/
│
├── data/
│   ├── sample/
│   └── processed/
│
├── storage/
│
├── docs/
│   ├── architecture/
│   ├── decisions/
│   └── interview-preparation/
│
├── scripts/
│
├── .env.example
├── .gitignore
└── README.md
```

Some directories are scaffolding for planned functionality and do not necessarily contain implemented features yet.

---

# 9. Local Development Setup

## Prerequisites

- Windows 11
- Python 3.12
- Git
- Docker Desktop
- Docker Compose
- Ollama (for local LLM capabilities)

## Clone the repository

```powershell
git clone https://github.com/Ganginenis/finsight-ai.git
cd finsight-ai
```

## Create the virtual environment

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r backend\requirements.txt
```

## Configure environment variables

Create a local `.env` file using `.env.example` as a reference.

Never commit `.env` or real credentials.

## Start PostgreSQL

```powershell
docker compose --env-file .env -f infrastructure\docker\compose.yaml up -d db
```

Verify the container:

```powershell
docker ps --filter "name=finsight-postgres"
```

## Run tests

```powershell
python -m pytest -v
```

## Start the API

```powershell
uvicorn backend.app.main:app --reload
```

FastAPI Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 10. Engineering Principles

The project follows these principles:

### 1. Evidence Before Answers
AI responses should be grounded in retrieved information wherever applicable.

### 2. Explainability
Risk scores and AI outputs should provide supporting evidence and understandable signals.

### 3. Human-in-the-Loop
AI should support financial investigation decisions, not silently replace human accountability.

### 4. Security by Design
Validate inputs, protect uploaded files, secure credentials, and apply least-privilege access.

### 5. Modular Architecture
Keep API, business logic, persistence, and AI responsibilities separated.

### 6. Test-Driven Quality
Cover successful scenarios, invalid inputs, edge cases, and failure conditions.

### 7. Reproducibility
Track configurations, migrations, model choices, and evaluation results.

### 8. Resource Awareness
Prefer local and lightweight models during development.

### 9. Incremental Delivery
Implement, test, review, and validate each milestone before moving forward.

---

# 11. Security and Data Privacy

The proof of concept is designed to use synthetic or authorized sample data.

Security considerations include:

- Original documents stored outside publicly served frontend directories.
- Generated storage identifiers instead of trusting uploaded filenames.
- File extension, MIME type, size, and content validation.
- Secrets stored outside source control.
- Dedicated database application credentials.
- Controlled AI tool access.
- Human review for risk-related workflows.
- Auditability of important operations.

Before any real-data or production deployment, additional controls must be implemented and reviewed, including encryption, access control, retention, deletion, monitoring, and applicable compliance requirements.

**The current project does not claim GDPR compliance, regulatory approval, or production security certification.**

---

# 12. Delivery Roadmap

| Milestone | Expected Deliverable | Status |
|---|---|---|
| M1 | Backend and database foundation | Completed |
| M2 | Document ingestion pipeline | In Progress |
| M3 | Embeddings and semantic retrieval | Not Started |
| M4 | RAG and grounded AI Q&A | Not Started |
| M5 | Transaction intelligence and risk analysis | Not Started |
| M6 | AI tools and investigation workflows | Not Started |
| M7 | Frontend and user experience | Not Started |
| M8 | Security, CI/CD, deployment, and final demo | Not Started |

Milestone dates will be established as implementation progresses.

---

# 13. Success Criteria

FinSight AI will be considered a meaningful end-to-end proof of concept when it demonstrates:

- Successful upload and validation of financial PDFs.
- Secure storage of original documents.
- Page-wise text extraction.
- Text chunking with source-page traceability.
- Local embedding generation.
- Semantic retrieval of relevant document passages.
- RAG responses supported by document citations.
- Transparent handling of unsupported questions.
- Synthetic transaction anomaly detection.
- Explainable transaction risk scoring.
- AI-assisted investigation summaries.
- Human review and auditability.
- Automated tests and reproducible local setup.

---

# 14. Current Scope Limitations

The following are intentionally outside the current implementation:

- Live banking integrations.
- Real customer financial data.
- OCR for scanned PDFs.
- Production-grade fraud detection.
- Autonomous transaction blocking or financial decisions.
- Production deployment and operational SLAs.
- Compliance certification.

The immediate priority is to build a reliable, demonstrable end-to-end application before expanding into production integrations.

---

# 15. Project Positioning

FinSight AI demonstrates practical AI engineering across the complete application lifecycle.

It brings together:

- Python backend engineering.
- API and database architecture.
- Document ingestion and processing.
- Embeddings and vector search.
- Retrieval-Augmented Generation.
- LLM integration and controlled tool execution.
- Machine-learning-based anomaly detection.
- Model evaluation and explainability.
- Security, testing, and deployment engineering.

**The vision:** Build an intelligent financial operations platform where AI does more than generate text — it retrieves evidence, analyzes data, explains findings, and supports accountable business workflows.

---

## Project Maintenance

Update this README whenever a milestone changes.

In particular, maintain:

1. Development Progress Tracker.
2. Current Engineering Checkpoint.
3. Technology Stack.
4. Delivery Roadmap.
5. Known limitations and blockers.

Only mark a capability as completed after implementation and verification.
