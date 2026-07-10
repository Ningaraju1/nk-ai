# NK AI Roadmap

> AI-powered Coding Assistant with Hybrid Search, Agentic Workflow, and RAG

---

# Project Overview

## Project Name

NK AI

## Goal

Build an advanced AI Coding Assistant capable of:

- AI-powered code generation
- Code explanation
- Bug fixing
- Repository understanding
- Hybrid Search (Keyword + Vector)
- Conversational memory
- Multi-file context awareness
- Documentation search
- Agentic task execution

---

# Tech Stack

## Backend

- Python 3.13+
- Django
- Django REST Framework

## Frontend

- React
- TypeScript
- Tailwind CSS

## Database

- PostgreSQL

## Search

- OpenSearch

## Vector Database

- Qdrant

## Embedding Model

- Hugging Face Sentence Transformers

## Cache

- Redis

## Containerization

- Docker
- Docker Compose

## AI

- OpenAI Compatible APIs
- Hugging Face Models

## Version Control

- Git
- GitHub

---

# Development Workflow

Issue

↓

Feature Branch

↓

Development

↓

Commit

↓

Push

↓

Pull Request

↓

Self Review

↓

Merge into develop

↓

Delete Feature Branch

---

# Branch Strategy

main

- Production releases

develop

- Integration branch

feature/*

- New features

hotfix/*

- Production fixes

---

# Commit Convention

Examples

feat(search): add OpenSearch client

fix(auth): resolve JWT validation

docs: update README

refactor(api): simplify search service

build: organize Python dependencies

---

# Milestone 1 — Foundation

## Sprint 1

- [x] Repository Bootstrap
- [x] Repository Standards
- [x] Development Environment

## Sprint 2

### PR-005
- Backend Architecture Foundation

### PR-006
- Docker Infrastructure

### PR-007
- PostgreSQL

### PR-008
- Redis

### PR-009
- OpenSearch

### PR-010
- Qdrant

---

# Milestone 2 — Search

- [ ] OpenSearch
- [ ] Qdrant
- [ ] Hybrid Search
- [ ] Search API
- [ ] Search Ranking

---

# Milestone 3 — AI Engine

- [ ] Hugging Face Embeddings
- [ ] LLM Integration
- [ ] Prompt Templates
- [ ] Context Builder
- [ ] Response Generator

---

# Milestone 4 — Agentic Workflow

- [ ] Intent Detection
- [ ] Planner
- [ ] Tool Executor
- [ ] Memory
- [ ] Conversation Manager

---

# Milestone 5 — Frontend

- [ ] Authentication
- [ ] Chat UI
- [ ] Search UI
- [ ] Code Viewer
- [ ] History
- [ ] Settings

---

# Milestone 6 — Production

- [ ] Monitoring
- [ ] Logging
- [ ] CI/CD
- [ ] Deployment
- [ ] Documentation

---

# Current Progress

| PR | Feature | Status |
|----|---------|--------|
| PR-001 | Repository Bootstrap | ✅ |
| PR-002 | Repository Standards | ✅ |
| PR-003 | Development Environment | 🚧 |
| PR-004 | Django Configuration | ⏳ |
| PR-005 | Docker Infrastructure | ⏳ |
| PR-006 | PostgreSQL | ⏳ |
| PR-007 | Redis | ⏳ |
| PR-008 | OpenSearch | ⏳ |
| PR-009 | Qdrant | ⏳ |

---

# Future Features

- AI Code Review
- Repository Chat
- Documentation Search
- Semantic Search
- Multi-language Support
- Plugin System
- User Management
- Team Workspaces
- Analytics Dashboard

---

# Notes

This roadmap will evolve as the project grows.