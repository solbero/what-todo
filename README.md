# what-todo

## Development

### First time setup
Clone the repository:
```python
git clone git@github.com:solbero/what-todo.git
cd what-todo
```

Install Poetry on your machine for dependency management. The documentation for Poetry can be found [here](https://python-poetry.org/docs/).

macOS, Linux  or Windows Subsystem for Linux:
```sh
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

Windows:
```ps
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```

Install the project and activate the virtual environment:
```python
poetry install
```

Activate pre-commit hooks:
```python
pre-commit install
```
