# Celery Development Guide

## What is Celery?
Celery is a highly scalable, production-ready asynchronous task queue/job queue based on distributed message passing. In the NK AI project, we use Celery to offload long-running or computationally expensive background tasks (such as indexing repositories or processing embeddings) so that our main Django API remains fast and responsive for users.

## Worker
The Celery **Worker** is the background process that actively monitors the message broker for new tasks and executes them. You can have multiple workers running concurrently to process tasks in parallel.
- We run the worker via the `celery` service in our Docker Compose stack.

## Beat
Celery **Beat** is a scheduler. It kicks off tasks at regular intervals, which are then picked up and executed by available worker nodes in the cluster. It's essentially a highly configurable cron job replacement for Python and Django.
- We run this via the `celery-beat` service in Docker Compose. 
- *Important Note:* You should only ever run exactly *one* instance of Celery Beat at a time to prevent duplicate tasks from being scheduled.

## Redis Broker
Celery requires a "message broker" to send and receive messages between the Django app and the Celery workers. We use **Redis** for this purpose. 
- Redis acts as the fast, in-memory middleman holding the task queue.
- We also use Redis as our "result backend" to store the state and return values of completed tasks.

## Running Workers
In our development environment, both the worker and beat scheduler are fully Dockerized and run automatically when you bring up the stack.

To start the workers alongside your backend:
```cmd
docker compose up -d
```

## Common Commands
When developing, you will frequently need to restart the worker to pick up Python code changes, or view logs to debug tasks.

- **Restart the worker (CRITICAL: required after modifying any `tasks.py` file):**
  ```cmd
  docker compose restart celery
  ```
- **Restart the beat scheduler:**
  ```cmd
  docker compose restart celery-beat
  ```
- **View live worker logs:**
  ```cmd
  docker compose logs -f celery
  ```
- **View live beat logs:**
  ```cmd
  docker compose logs -f celery-beat
  ```

## Troubleshooting

### Task Not Found / Unregistered Task Error
**Error Log:** `KeyError: 'apps.core_api.tasks.my_task'`
**Solution:** The Celery worker loaded its code *before* you created or renamed the task. Unlike the Django development server, Celery does not auto-reload on code changes. You must run `docker compose restart celery` to force the worker to discover your new tasks.

### Connection Refused (Redis)
**Error Log:** `Error 111 connecting to localhost:6379. Connection refused.` or `getaddrinfo failed.`
**Solution:** 
1. Ensure your `.env` file uses the Docker service name (`redis://redis:6379/0`) and NOT `localhost`. 
2. If you are running the Django shell locally on your host Windows machine (outside Docker), you cannot reach the internal Docker Redis container by its hostname. Always run your shell inside the backend Docker container via:
   `docker compose exec backend python manage.py shell`
