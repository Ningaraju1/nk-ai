# Redis Development Guide

## Start

```bash
docker compose up -d
```

## Check Redis

```bash
docker compose logs redis
```

## Redis URL

```
redis://redis:6379/1
```

## Purpose

- Django Cache
- Celery Broker
- Celery Result Backend
- Rate Limiting
- Session Storage
- AI Queue