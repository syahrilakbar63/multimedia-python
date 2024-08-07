from PIL import Image
from PIL import ImageFilter

# Memuat gambar
image = Image.open('example.jpg')

filtered_image = image.filter(ImageFilter.BLUR)
filtered_image.save('filtered_result.jpg')