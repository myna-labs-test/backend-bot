include .env
export

shell:
	poetry shell

prepare:
	poetry install || true

run:
	poetry run python -m bot

build:
	docker build -t myna-labs-bot-worker --no-cache .

down:
	docker kill myna-labs-bot-worker

run-docker:
	docker container rm myna-labs-bot-worker || true
	docker run --name myna-labs-bot-worker --network many-labs-network myna-labs-bot-worker