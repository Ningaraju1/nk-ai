from qdrant_client import QdrantClient

from django.conf import settings


def check_qdrant():
    client = QdrantClient(
        host=settings.QDRANT["HOST"],
        port=settings.QDRANT["PORT"],
    )

    return client.get_collections()