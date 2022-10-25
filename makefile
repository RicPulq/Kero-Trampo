# apt install -y curl python3 python3-distutils
COMPATIBLE_SHELLS = "bash fish zsh"
POETRY = $(HOME)/.poetry/bin/poetry

clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '*.db' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build

install:
	poetry install

test:
	pytest tests/ -vvv  --workers auto -x --cov={{cookiecutter.project_slug}} --cov-report=html

export:
	poetry export -f requirements.txt -o requirements.txt

cov:
	coverage html
	xdg-open htmlcov/index.html

install_poetry.bash:
ifeq ($(shell id -u),0)
	mkdir /etc/bash_completion.d
	$(POETRY) completions bash > /etc/bash_completion.d/poetry.bash-completion > /dev/null
else
	sudo mkdir /etc/bash_completion.d
	$(POETRY) completions bash | sudo tee /etc/bash_completion.d/poetry.bash-completion > /dev/null
endif

install_poetry.fish:
	$(POETRY) completions fish > ~/.config/fish/completions/poetry.fish

install_poetry.zsh:
	$(POETRY) completions zsh > ~/.zfunc/_poetry

install_poetry:

ifeq (,$(findstring $(MY_SHELL), $(COMPATIBLE_SHELLS)))
	echo "Informe a variavel MY_SHELL com um dos valores: $(COMPATIBLE_SHELLS)"
	exit 203
endif
ifeq (,$(shell which curl))
	echo "Comando \`curl\` não encontrado"
	exit 204
endif
ifeq (,$(shell which python3))
	echo "Comando \`python3\` não encontrado"
	exit 204
endif
ifneq (,$(shell bash -c "python3 -c 'import distutils.util' |& grep -o ModuleNotFoundError"))
	echo "Modulo python distutils.util não encontrado"
	exit 204
endif
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3
	$(MAKE) install_poetry.$(MY_SHELL)

run:
	uvicorn app:app --reload --host 0.0.0.0 --port 8000 --proxy-headers --forwarded-allow-ips '*'

config_git:
	pre-commit install ;  pre-commit install --hook-type commit-msg

all_test:
	python3 -m unittest discover test/

init_alembic:
	alembic init alembic;

alembic_revision:
	read -p "nome da revision: " nome; alembic revision --autogenerate -m "$$nome"

alembic_upgrade:
	alembic upgrade head

alembic_downgrade:
	alembic downgrade base

popula_db:
	cat database/dump_sos.sql | docker exec -i a65ddbce31fb psql -U postgres sos

db_init:
	alembic upgrade 4ac9 ; alembic upgrade ce92

drop_db:
	cd app/database/ ; python3 drop_database.py
requirements:
	poetry export --without-hashes --format requirements.txt --output requirements.txt


