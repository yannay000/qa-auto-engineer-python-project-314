init:
	uv init

install:
	uv sync

test:
	uv run pytest -v -s

lint:
	uv run ruff check --fix pages tests steps utils

check: test lint

start:
	docker run --rm -p 5173:5173 hexletprojects/qa_auto_python_testing_kanban_board_project_ru_app