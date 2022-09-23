import os
from os.path import isfile, join
from fastapi import APIRouter

router = APIRouter(tags=["parser"])


def test_template(nome):
    imports = f"""from fastapi.testclient import TestClient
from app import core

from main import app
client = TestClient(app)

"""
    return imports


@router.get("/parser")
def generate_test():
    """Retorna Hora do Servidor"""

    test_dir = os.path.join(os.getcwd(), "tests")
    print(test_dir)
    endpoints_dir = os.path.join(os.getcwd(), "app/api/endpoints")
    list_test = os.listdir(test_dir)
    list_endpoints = os.listdir(endpoints_dir)

    for d in list_endpoints:
        print(d)
        if d not in list_test:
            file = open(test_dir + f"/test_{d}", "w")
            file.write(test_template(d.split(".")[0]))
            print(f"test_{d}")
        else:
            print("ja exites")

    return "ok"
