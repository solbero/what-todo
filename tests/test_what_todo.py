import toml


def test_project_version():
    path = "pyproject.toml"
    config = toml.load(path)
    version = config["tool"]["poetry"]["version"]
    assert version == "0.1.0"
