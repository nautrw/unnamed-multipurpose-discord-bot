import hashlib
import random


def generate_data(seed):
    random.seed(seed)

    hash = hashlib.sha512()
    hash.update(str(seed).encode("utf-8"))
    int_number = int(hash.hexdigest(), 16) % (10**6)
    hex_code = f"{int_number:06x}"

    variants = {"winter": 25, "summer": 25, "autumn": 25, "spring": 25}
    variant = random.choices(list(variants.keys()), weights=list(variants.values()))[0]

    data = {"hex_code": hex_code, "variant": variant}

    return data