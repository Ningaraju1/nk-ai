# OpenSearch Client
from opensearchpy import OpenSearch

from django.conf import settings


client = OpenSearch(
    hosts=[settings.OPENSEARCH_HOST],
    http_compress=True,
)