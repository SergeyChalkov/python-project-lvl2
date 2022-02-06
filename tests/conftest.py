import json
import pytest
import yaml
from pathlib import Path


fixtures_dir = Path('tests/fixtures')


@pytest.fixture(params=[
    ('j_first_flat.json', json.load), ('y_first_flat.yaml', yaml.safe_load)
])
def flat_one(request):
    with (fixtures_dir / request.param[0]).open() as file:
        return request.param[1](file)


@pytest.fixture(params=[
    ('j_second_flat.json', json.load), ('y_second_flat.yaml', yaml.safe_load)
])
def flat_two(request):
    with (fixtures_dir / request.param[0]).open() as file:
        return request.param[1](file)


@pytest.fixture(scope='session')
def output():
    with (fixtures_dir / 'result_flat').open() as file:
        return file.read().rstrip('\n')
