# Makefile for NitroStack

# Variables
PYTHON=python3
PIP=pip
SRC_DIR=src
TEST_DIR=tests
DOCKER_IMAGE=nitrostack:latest

# Define phony targets
.PHONY: test clean-cache lint format docker-build docker-run install

# Run tests with cache cleared
test:
	PYTHONPATH=$(pwd) pytest --cache-clear $(TEST_DIR) -v

# Clear all cache files (pytest, __pycache__, coverage)
clean-cache:
	find . -type d -name '__pycache__' -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf .mypy_cache

# Lint code with flake8
lint:
	flake8 $(SRC_DIR) $(TEST_DIR) --max-line-length=88 --exclude=.venv,__pycache__,.pytest_cache

# Format code with black
format:
	black $(SRC_DIR) $(TEST_DIR)

# Install Python dependencies
install:
	$(PIP) install -r requirements.txt

# Build Docker image
docker-build:
	docker build -t $(DOCKER_IMAGE) .

# Run Docker container
docker-run:
	docker run -p 8000:8000 $(DOCKER_IMAGE)

# Run all steps (install, lint, format, test)
all: install lint format test
