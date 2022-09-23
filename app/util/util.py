import base64
import uuid
from app import core
from .validators import validate_image, validate_uuid4
import random
import os, csv


def password_hash(key):
    if len(key) <= 5:
        raise ValueError("o campo senha deve conter no minimo 6 caracteres")
    return core.get_password_hash(key)


def save_image(key):
    if validate_uuid4(key):
        return key
    name = str(uuid.uuid4())
    filename = f"{core.settings.UPLOAD_FOLDER}{name}.jpeg"
    with open(filename, "wb") as f:
        f.write(base64.b64decode(key))
    return name


def save_file(key, ext):
    name = str(uuid.uuid4())
    filename = f"{core.settings.UPLOAD_FOLDER}{name}.{ext}"
    with open(filename, "w") as f:
        f.write(key)
    return name


def save_csv_file(header, data):
    name = str(uuid.uuid4())
    filename = f"{core.settings.UPLOAD_FOLDER}{name}.csv"
    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)
    return name


def delete_file(path, key):
    if os.path.exists(f"{path}{key}"):
        os.remove(f"{path}{key}")
    else:
        return False
    return True


def delete_image(key):
    if os.path.exists(f"{core.settings.UPLOAD_FOLDER}{key}.jpeg"):
        os.remove(f"{core.settings.UPLOAD_FOLDER}{key}.jpeg")
    else:
        return False
    return True


def list_files(path):
    onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return onlyfiles


def create_key(usuario):
    if usuario.is_gestor:
        return ["1", "2", "3", "4", "5"]
    if usuario.is_fiscal:
        return ["1", "2", "3", "4"]
    if usuario.is_fornecedor:
        return ["1", "2", "3"]
    if usuario.is_entregador:
        return ["1", "2"]
    if usuario.is_consumidor:
        return ["1"]


def generate_cnpj():
    def calculate_special_digit(l):
        digit = 0

        for i, v in enumerate(l):
            digit += v * (i % 8 + 2)

        digit = 11 - digit % 11

        return digit if digit < 10 else 0

    cnpj = [1, 0, 0, 0] + [random.randint(0, 9) for x in range(8)]

    for _ in range(2):
        cnpj = [calculate_special_digit(cnpj)] + cnpj

    return "%s%s%s%s%s%s%s%s%s%s%s%s%s%s" % tuple(cnpj[::-1])


def generate_cpf():
    cpf = [random.randint(0, 9) for x in range(9)]

    for _ in range(2):
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11

        cpf.append(11 - val if val > 1 else 0)

    return "%s%s%s%s%s%s%s%s%s%s%s" % tuple(cpf)
