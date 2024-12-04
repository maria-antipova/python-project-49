install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	@echo "Установка в виртуальном окружении"
	python3 -m venv .venv
	source .venv/bin/activate
	python3 -m pipx install dist/*.whl
	deactivate

lint:
	poetry run flake8 brain_games
