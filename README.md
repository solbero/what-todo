# what-todo

## Development

### Get the repository
Clone the repository:
```python
git clone git@github.com:solbero/what-todo.git
cd what-todo
```

### Poetry for dependency management
Install Poetry on your machine. The documentation for Poetry can be found [here](https://python-poetry.org/docs/).

#### macOS, Linux and Windows Subsystem for Linux
```sh
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

#### Windows
```ps
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```

#### Install the virtual enviroment
Make sure you are in the root folder of the project, then install the virtual environment and dependencies:
```python
poetry install
```

### Install pre-commit hooks
Make sure you are in the root folder of the project, then install the pre-commit hooks:
```python
pre-commit install
```

### Create a dotenv file
You need to create a `.env` file in the root directory to hold some environment variables for the project.

1. Create an empty file in the root directory named `.env`
2. Paste in the following content:
```
FLASK_ENV="development"
FLASK_APP="main.py"
FLASK_SECRET_KEY="<generated-secret-key>"
```
4. Replace `<generated-secret-key>` with a secret key you generate yourself. Can get some good instructions on how to generate a secret key in [this StackOverflow answer](https://stackoverflow.com/a/54433731).

## Running
You need to run the app through Poetry and its virtual environment:
```sh
poetry run flask run
```
It is also possible to debug the app while running using VSCode's debugging capabilities. To do so open the "Run and debug" pane on the left had side of VSCode. Make sure the `Python: Flask` configuration is selected.
