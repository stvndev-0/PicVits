# optimiza la subida de imagenes
from PIL import Image
import io

image_file = request.FILES['image']
with Image.open(image_file) as img:
    image_io = io.BytesIO()
    img.save(image_io, format=img.format, optimize=True, quality=85)
    request.FILES['image'] = image_io