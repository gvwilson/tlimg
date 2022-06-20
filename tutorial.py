from PIL import Image

picture = Image.open("sample_00.png")
print("format", picture.format)
print("size", picture.size)
print("mode", picture.mode)

position = (10, 10)
color = picture.getpixel(position)
print(f"color at {position}: {color}")
