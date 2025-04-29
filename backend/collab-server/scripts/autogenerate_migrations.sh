#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <message>"
    exit 1
fi
docker compose exec collab-server alembic revision --autogenerate -m "$1"
