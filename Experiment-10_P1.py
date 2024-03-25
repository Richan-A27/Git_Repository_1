from PIL import Image, ImageOps, ImageFilter

image = Image.open('green.jpg')
# a) Display the image
image.show()


# b) Plot the image in the console window
image_data = image.load()
for y in range(image.height):
    for x in range(image.width):
       print(image_data[x, y], end=' ')
       break

# c) Display the image size (width and height)
print(f"Image size: {image.size[0]}x{image.size[1]}")


# d) Reduce the image size to half
half_size_image = image.resize((image.width // 2, image.height // 2))
half_size_image.show()


# e) Rotate the image 145 degrees
rotated_image = image.rotate(145)
rotated_image.show()

# f) Resize the image
resized_image = image.resize((image.width + 50, image.height + 70))
resized_image.show()

# g) Flip the image (Left to Right, Top to Bottom)
flipped_lr_image = ImageOps.mirror(image)
flipped_tb_image = ImageOps.flip(image)
flipped_lr_image.show()
flipped_tb_image.show()

# h) Crop the image
box = (100, 100, 400, 400)  # Define the region to crop (left, top, right, bottom)
cropped_image = image.crop(box)
cropped_image.show()

# i) Change the color image to GrayScale, Black and White
gray_image = image.convert('L')
bw_image = gray_image.point(lambda x: 0 if x < 128 else 255, '1')
gray_image.show()
bw_image.show()


# j) Apply blur effect on the image
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.show()
