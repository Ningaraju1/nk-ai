# Qdrant Development Guide

## What is Qdrant?
Qdrant is a highly performant vector similarity search engine and database. It provides a convenient API to store, search, and manage vectors (embeddings) along with their JSON payloads. In the NK AI project, Qdrant acts as the primary vector store for enabling AI-powered semantic search, Retrieval-Augmented Generation (RAG), and fast document retrieval.

## Docker Ports
Qdrant runs locally through Docker Compose and exposes two primary ports:
- **`6333`**: HTTP REST API (Used for general interactions, dashboards, and health checks)
- **`6334`**: gRPC API (High-performance binary protocol, typically used under the hood by the Python `qdrant-client`)

## Health Check
You can easily verify that the backend is communicating with Qdrant correctly using the provided utility service.

1. Open the Django shell inside your Docker container:
   ```cmd
   docker compose exec backend python manage.py shell
   ```
2. Run the health check function:
   ```python
   from apps.core.services.vector_health import check_qdrant
   check_qdrant()
   ```
   *This should successfully return a list of existing collections or an empty list if none have been created yet.*

## Collections
In Qdrant, a "Collection" is a named set of points (vectors) among which you can search. You can think of a collection as being equivalent to a "table" in PostgreSQL or an "index" in OpenSearch.
- **Default Collection:** The project defaults to the `nk-ai` collection. This is configurable via the `QDRANT_COLLECTION` environment variable in your `.env`.

## Development Commands
Here are a few useful commands for managing the Qdrant container during development:

- **View live logs:**
  ```cmd
  docker compose logs -f qdrant
  ```
- **Restart the Qdrant service:**
  ```cmd
  docker compose restart qdrant
  ```
- **Stop or start the service individually:**
  ```cmd
  docker compose stop qdrant
  docker compose start qdrant
  ```
