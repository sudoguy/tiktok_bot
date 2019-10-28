from hashlib import md5, sha1
from time import time


def generate_as(now: str) -> str:
    as_md5 = md5(now.encode()).hexdigest()

    return as_md5


def generate_cp(now: str) -> str:
    now += str(time())

    cp_md5 = md5(now.encode()).hexdigest()

    return cp_md5


def generate_mas(now: str) -> str:
    mas_sha = sha1(now.encode()).hexdigest()
    mas_md5 = md5(mas_sha.encode()).hexdigest()

    return mas_md5
