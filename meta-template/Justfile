default:
    @just --list

init:
    uv sync
    uv run pre-commit install

test:
    uv run pytest

lint:
    uv run pylint --recursive=yes copier/ tests/
