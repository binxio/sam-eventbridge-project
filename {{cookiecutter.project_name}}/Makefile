SHELL = /bin/bash -c
VIRTUAL_ENV = $(shell poetry env info -p)
export BASH_ENV=$(VIRTUAL_ENV)/bin/activate

.DEFAULT_GOAL:=help
.PHONY: help
help:  ## Display this help
	$(info {{cookiecutter.description}})
	awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

pyproject.toml:
	$(info Create pyproject.toml file...)
	poetry init \
		--no-interaction --quiet \
		--name "{{cookiecutter.project_name}}" \
		--description "{{cookiecutter.description}}" \
		--license=MIT \
		--python ^3.9 \
		--dependency aws-sam-cli \
		--dependency aws-lambda-powertools[pydantic] \
		--dev-dependency pytest \
		--dev-dependency pytest-cov \
		--dev-dependency mypy \
		--dev-dependency xenon \
		--dev-dependency radon
	sed -i '' 's/$(shell echo "{{cookiecutter.project_name}}" | tr "-" _)/src/g' pyproject.toml

.git:
	git init
	pre-commit install

.PHONY: install
install: pyproject.toml .git ## Install all dependencies
	poetry install

.aws-sam/build/template.yaml: build

.PHONY: test
test: _complexity-baseline ## Run the tests defined in the project
	pytest --cov

.PHONY: lint
lint: _black _mypy ## Lint all code

.PHONY: _complexity-baseline
_complexity-baseline:
	$(info Maintenability index)
	radon mi --min A --max A --show --sort src
	$(info Cyclomatic complexity index)
	xenon --max-absolute A --max-modules A --max-average A src

.PHONY: _black
_black:
	black .

.PHONY: _mypy
_mypy:
	$(info [*] Python static type checker...)
	mypy src tests

.PHONY: build
build: test ## Build the artifacts needed for the deployment
	sam build

.PHONY: deploy
deploy: .aws-sam/build/template.yaml ## Deploy the template to AWS
	sam deploy --resolve-s3 --no-fail-on-empty-changeset

.PHONY: destroy
destroy: ## Destroy the deployed resources from your AWS account
	sam delete

.PHONY: clean
clean: ## Cleanup, removes the virtual environment
	$(info Remove virtual environment $(VIRTUAL_ENV))
	[[ -d "$(VIRTUAL_ENV)" ]] && rm -rf "$(VIRTUAL_ENV)" || True
	[[ -d "reports" ]] && rm -rf "reports" || True
	[[ -d ".aws-sam" ]] && rm -rf ".aws-sam" || True

$(VERBOSE).SILENT:
