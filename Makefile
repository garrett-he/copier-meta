.DEFAULT_GOAL := help

.PHONY: help
help: ## Show help information
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

.PHONY: init
init: ## Initialize project
	poetry install --no-root
	poetry run pre-commit install

.PHONY: lint
lint: ## Code analyse and lint
	poetry run pylint --recursive=yes copier/ tests/

.PHONY: test
test: ## Run tests
	poetry run pytest

.PHONY: clean
clean: ## Clean up cache files
	find . -name '__pycache__' -type d | xargs rm -rf
	rm -rf .pytest_cache/
	rm -f .python-version
