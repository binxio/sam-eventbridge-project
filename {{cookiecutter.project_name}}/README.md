# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Prerequisites

This project requires [Python v3.9](https://www.python.org/) or newer and [poetry](https://python-poetry.org/). The rest of the dependencies will be encapsulated in the virtual environment that poetry will maintain for you.

```bash
brew install python3 poetry
```

## Before you start

Install all dependencies by executing the following command:

```bash
make install
```

## Build

To only perform a build you can use the following command, the output will be stored under a `.aws-sam` folder.

```bash
make build
```

## Local invocation

When you have build your SAM Template you can perform local invokes against it, for example:

```bash
poetry run sam local invoke CloudFormationStacksFunction -e payloads/cloudformation_update.json
```

## Deploy

To deploy make sure you have selected an `AWS_PROFILE` or that you have loaded the access keys in your session.

```bash
make deploy
```

## Destroy

To remove the deployed resources execute the following:

```bash
make deploy
```

## Cleanup

To remove the virtual environment created by poetry execute:

```bash
make cleanup
```
