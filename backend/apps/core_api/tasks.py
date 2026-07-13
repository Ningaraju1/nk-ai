import time
from celery import shared_task


@shared_task
def process_repository(repo_name):

    print("=" * 60)
    print(f"Processing repository: {repo_name}")
    print("=" * 60)

    time.sleep(5)

    print("Repository indexed.")

    return {
        "repository": repo_name,
        "status": "completed",
    }