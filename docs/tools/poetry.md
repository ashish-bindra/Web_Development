# Poetry

## Basic of poetry

- Since PEP 518  the pyprojec5.toml diles has been introduced.

## Install poetry

It not worked in my case.

```sh
pip install poetry
```

Windows (Powershell)

```sh
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

Add Poetry to your PATH

The installer creates a poetry wrapper in a well-known, platform-specific directory:

```sh
$HOME/.local/bin on Unix.
%APPDATA%\Python\Scripts on Windows.
$POETRY_HOME/bin if $POETRY_HOME is set.
If this directory is not present in your $PATH, you can add it in order to invoke Poetry as poetry.

Alternatively, the full path to the poetry binary can always be used:

~/Library/Application Support/pypoetry/venv/bin/poetry on macOS.
~/.local/share/pypoetry/venv/bin/poetry on Linux/Unix.
%APPDATA%\pypoetry\venv\Scripts\poetry on Windows.
$POETRY_HOME/venv/bin/poetry if $POETRY_HOME is set.
```

check the version

```sh
poetry --version
```

## To insilize the py.toml file

```sh
poetry init
```

This command will guide you through creating your pyproject.toml config.

Package name [new folder]:  dir
Version [0.1.0]:
Description []:  a perfect project
Author [ashish <ashishbindra2@gmail.com>, n to skip]:  ashish
License []:  MIT
Compatible Python versions [>=3.13]:  3.11

## example of pyproject.toml file

```sh
[project]
name = "project name"
version = "0.1.0"
description = "a perfect project"
authors = [
    {name = "ashish"}
]
license = {text = "MIT"}
readme = "README.md"
requires-python = "3.11"
dependencies = [
]

[tool.poetry]

[tool.poetry.group.dev.dependencies]
requests = "^2.32.4"

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```

## Creating a New Project

If you prefer, you can create a new project with a basic folder structure and a pyproject.toml file using the poetry new command.

Example:

```sh
poetry new myproject
```

## Adding Dependencies After Initialization

Once you have the pyproject.toml file, you can add dependencies to your project.

- it will create virtual evviroment.
- it also create poetry.lock file.
- It is a internal dile for poetry to keep the trake of the dependecy
- We can also remove the dependecy and update them

Example:

```sh
poetry add requests
```

## To display poetry install packages

```sh
poetry show
```

## Install the specific versions

```sh
poetry add requests@2.12.1
```

## To remove pkg

```sh
poetry remove requests
```

To install the up until the major version, it wont install a request version 3
> poetry add requests^2.12.1

it is aalso the default installation style in poetry

It wont install request version

> poetry add requests~2.12.1

It install the package up to the latest minor version

## To install the dependency

```sh
poetry install

poetry install -no-root
```

> `poetry shell` to cmd to go that virtal env or activate virtual env

## Handle version

`poetry version minor` to convert 0.2.0 to 0.3.0 sementic version

Distributable formats such as awheel or a source distribution to gzip file

```sh
poetry publish
```
