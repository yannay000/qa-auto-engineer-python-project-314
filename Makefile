init:
	uv init

install:
	uv sync

# run:
# 	uv run gendiff files/file1.json files/file2.json

test:
	uv run pytest -v -s

# test-coverage:
# 	uv run pytest --cov=gendiff --cov-report xml

# help:
# 	uv run gendiff -h

lint:
	uv run ruff check --fix pages tests

check: test lint

build:
	uv build

package-install:
	uv tool install --force dist/*.whl

start:
	docker run --rm -p 5173:5173 hexletprojects/qa_auto_python_testing_kanban_board_project_ru_app