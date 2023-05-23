from uuid import UUID
import base64
import re
from email_validator import validate_email, EmailNotValidError
from itertools import cycle

from app import core


def validate_uuid4(uuid_string):
    try:
        UUID(uuid_string, version=4)
    except ValueError:
        return False
    return True


# validar imagem em base 64
def validate_image(key: str):
    try:
        if key == None:
            return key
        if validate_uuid4(key):
            return key
        result = key.split(",")[-1]
        base64.b64encode(base64.b64decode(result))
    except:
        raise ValueError("Campo deve conter uma imagem em formato valido")
    return result


# validador de CPF
def cpf_validate(key: str):
    if len(key) != 11:
        raise ValueError("O campo deve conter exatamente 11 digitos numericos")

    if key in (c * 11 for c in "1234567890"):
        raise ValueError("CPF invalido")

    cpf_reverso = key[::-1]
    for i in range(2, 0, -1):
        cpf_enumerado = enumerate(cpf_reverso[i:], start=2)
        dv_calculado = sum(map(lambda x: int(x[1]) * x[0], cpf_enumerado)) * 10 % 11
        if cpf_reverso[i - 1 : i] != str(dv_calculado % 10):
            raise ValueError("CPF invalido")

    return key


# validador de CNPJ
def cnpj_validate(key: str):
    if len(key) != 14:
        raise ValueError("CNPJ invalido")

    if key in (c * 14 for c in "1234567890"):
        raise ValueError("CNPJ invalido")

    cnpj_r = key[::-1]
    for i in range(2, 0, -1):
        cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])
        dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
        if cnpj_r[i - 1 : i] != str(dv % 10):
            raise ValueError("CNPJ invalido")
    return key


# Valida um dado que pode ser CPF OU CNPJ
def cnpj_cpf(key: str):
    if len(key) == 11:
        cpf_validate(key)
    else:
        cnpj_validate(key) 

# Aplica Primeria letra maiuscula em uma string
def normalize_capitalize(key: str):
    key = key.lower()
    return " ".join((word.capitalize()) for word in key.split(" "))


def normalize_password(key: str):
    return core.get_password_hash(key)


def normalize_lower(key: str):
    return " ".join((word.lower()) for word in key.split(" "))


# retira caractes nao numericos de uma string
def normalize_numeric(key: str) -> str:
    key = re.sub("[^0-9]+", "", key)
    if not key.isnumeric():
        raise ValueError("O campo deve conter somente numeros")
    return key


def normalize_no_numeric(key: str) -> str:
    if key.isnumeric():
        raise ValueError("O campo nao deve conter numeros")
    return key.lower()


def normalize_telefone(key: str):
    key = re.sub("[^0-9]+", "", key)
    if len(key) < 10 or len(key) > 13:
        raise ValueError(
            "O campo deve conter no minimo 10 e no maximo 13 digitos numericos"
        )
    return key


def email_validate(key: str):
    try:
        valid = validate_email(key)
        key = valid.email
    except EmailNotValidError:
        raise ValueError("O campo deve conter um email valido")
    return key.lower()
