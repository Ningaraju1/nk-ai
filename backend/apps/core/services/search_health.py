from .opensearch_client import client


def check_opensearch():

    info = client.info()

    return {
        "status": "healthy",
        "cluster": info["cluster_name"],
        "version": info["version"]["number"],
    }