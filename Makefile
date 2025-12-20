.PHONY: run-server
run-server:
	uv run python src/manage.py runserver 0.0.0.0:8000

.PHONY: install
install:
	uv install --no-root

.PHONY: migrate
migrate:
	uv run python src/manage.py migrate

.PHONY: migrations
migrations:
	uv run python src/manage.py makemigrations

.PHONY: superuser
superuser:
	uv run python src/manage.py createsuperuser

.PHONY: install-pre-commit
install-pre-commit:
	uv run pre-commit install

.PHONY: lint
lint:
	uv run pre-commit run --all-files

.PHONY: update
update: install install-pre-commit migrate
