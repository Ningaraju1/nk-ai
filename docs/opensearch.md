# OpenSearch Development Guide

## Overview

OpenSearch provides distributed search and analytics capabilities for NK AI.

## Services

- OpenSearch
- OpenSearch Dashboards

## Local URLs

- OpenSearch: http://localhost:9200
- Dashboards: http://localhost:5601

## Docker Commands

Start:

```bash
docker compose up -d
```

Stop:

```bash
docker compose down
```

Logs:

```bash
docker compose logs opensearch
```

## Health Check

```bash
python manage.py shell
```

```python
from apps.core.services.search_health import check_opensearch

print(check_opensearch())
```