import json
import pytest
import yaml
from pathlib import Path


fixtures_dir = Path('tests/fixtures')


@pytest.fixture(params=[json.load, yaml.safe_load])
def flat_one(request):
    with (fixtures_dir / 'first_flat.json').open() as file:
        return request.param(file)


@pytest.fixture(params=[json.load, yaml.safe_load])
def flat_two(request):
    with (fixtures_dir / 'second_flat.json').open() as file:
        return request.param(file)


@pytest.fixture(scope='session')
def output():
    with (fixtures_dir / 'result_flat').open() as file:
        return file.read().rstrip('\n')
