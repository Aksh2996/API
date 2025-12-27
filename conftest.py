import pytest
import yaml
from classess.auth import Auth
from classess.crud import Crud
from classess.edge import Edge
from classess.error import Error
from classess.perf import Perf
from classess.valid import Valid


def conf():
    with open(r"C:\Backend_Automation\pytest_2Final_project22\testss\config.yaml") as j:
        co=yaml.safe_load(j)
    env=co.get("env","dev")
    return co[env]

cop=conf()

@pytest.fixture()
def req_res_helper():
    return Auth(cop["REQRES_BASE"])

@pytest.fixture()
def json_placeholder():
    return Crud(cop["JSONPLACEHOLDER_BASE"])

@pytest.fixture()
def json_placeholder_edge():
    return Edge(cop["JSONPLACEHOLDER_BASE"])

@pytest.fixture()
def json_placeholder_error():
    return Error(cop["JSONPLACEHOLDER_BASE"])


@pytest.fixture()
def http_bin():
    return Error(cop["HTTPBIN_BASE"])

@pytest.fixture()
def go_resbase():
    return Crud(cop["GOREST_BASE"])

def go_rest():
    return Valid(cop["GOREST_BASE"])

@pytest.fixture()
def json_placeholder_perf():
    return Perf(cop["JSONPLACEHOLDER_BASE"])
@pytest.fixture()
def http_bin_perf():
    return Edge(cop["HTTPBIN_BASE"])





