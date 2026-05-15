init:
	uv init

install:
	uv sync

test:
	uv run pytest -v -s

test-coverage:
	uv run pytest --cov=steps --cov-report xml

lint:
	uv run ruff check --fix pages tests steps utils config.py

check: test lint

start:
	docker run --rm -p 5173:5173 hexletprojects/qa_auto_python_testing_kanban_board_project_ru_app