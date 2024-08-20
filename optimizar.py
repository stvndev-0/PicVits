# optimiza la subida de imagenes
# from PIL import Image
# import io

# image_file = request.FILES['image']
# with Image.open(image_file) as img:
#     image_io = io.BytesIO()
#     img.save(image_io, format=img.format, optimize=True, quality=85)
#     request.FILES['image'] = image_io

def sum(x, y):
    return x + y

def is_greater_than(number_1, number_2):
    return number_1 > number_2