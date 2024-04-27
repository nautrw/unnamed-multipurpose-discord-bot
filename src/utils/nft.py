import hashlib
import random
from io import BytesIO

from PIL import Image


def generate_nft_data(seed):
    random.seed(seed)

    hash = hashlib.sha512()
    hash.update(str(seed).encode("utf-8"))
    int_number = int(hash.hexdigest(), 16) % (10**6)
    hex_code = f"{int_number:06x}"

    variants = {"winter": 25, "summer": 25, "autumn": 25, "spring": 25}
    variant = random.choices(list(variants.keys()), weights=list(variants.values()))[0]

    data = {"hex_code": hex_code, "variant": variant}

    return data


def make_nft(data: dict):
    hex_code = data["hex_code"]
    variant = data["variant"]

    rgb = tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
    
    img = Image.new("RGBA", (500, 500), rgb)
    
    variant_img = Image.open(f"src/assets/nft/{variant}.png").convert('RGBA')
    img.paste(variant_img, (0, 0), variant_img)
    
    bio = BytesIO()
    img.save(bio, "PNG")
    bio.seek(0)
    
    return bio