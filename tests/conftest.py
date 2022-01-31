import json
import pytest
from pathlib import Path


fixtures_dir = Path('tests/fixtures').resolve()


@pytest.fixture(scope='session')
def flat_one():
    with (fixtures_dir / 'first_flat.json').open() as file:
        return json.load(file)


@pytest.fixture(scope='session')
def flat_two():
    with (fixtures_dir / 'second_flat.json').open() as file:
        return json.load(file)


@pytest.fixture(scope='session')
def output():
    with (fixtures_dir / 'result_flat').open() as file:
        return file.read().rstrip('\n')
