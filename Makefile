.PHONY: all
all: help

.PHONY: init ## Initialize dependencies
init:
	pip install pipenv
	pipenv install --dev

.PHONY: test ## Run test
test:
	pipenv run py.test tests

.PHONY: help ## View help
help:
	@grep -E '^.PHONY: [a-zA-Z_-]+.*?## .*$$' $(MAKEFILE_LIST) | sed 's/^.PHONY: //g' | awk 'BEGIN {FS = "## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
