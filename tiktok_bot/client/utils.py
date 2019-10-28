from hashlib import md5, sha1


def generate_mas(now: str) -> str:
    mas_sha = sha1(now.encode()).hexdigest()
    mas_md5 = md5(mas_sha.encode()).hexdigest()

    return mas_md5
