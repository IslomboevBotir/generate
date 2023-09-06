from typing import List
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
import textwrap

first_image = Image(filename='Salar.jpg')
first_image.modulate(brightness=40)
second_image = Image(width=4960, height=4677, background=Color('white')) # белый фон 
combined_image = Image(width=first_image.width + second_image.width, height=max(first_image.height, second_image.height))
combined_image.composite(first_image, left=0, top=0)
combined_image.composite(second_image, left=first_image.width, top=0) #соединение фона

images = (
    Image(filename='1.png'),
    Image(filename='2.png'),
    Image(filename='3.png'),
    Image(filename='4.png'),
)


def second_combined_images(images):
    num_images = len(images)
    assert 1 <= num_images <= 3, "Функция принимает от 1 до 3 изображений."
    image1_width = second_image.width // num_images
    x_positions = [first_image.width + i * image1_width for i in range(num_images)]
    for i in range(num_images):
        image = images[i]
        image_kf = image.height / image.width * image1_width
        image.scale(image1_width, int(image_kf))

        if num_images == 3:
            combined_image.composite(image, left=x_positions[i], top=round(second_image.height /5)) 
        elif num_images == 2:
            combined_image.composite(image, left=x_positions[i], top=round(second_image.height /4))
        else:
            combined_image.composite(image, left=x_positions[i], top=round(second_image.height / 8))


def draw_text(draw, font_size, color, text, x, y, max_line_length=None):
    draw.font_size = font_size
    draw.fill_color = Color(color)
    draw.font = 'arial.ttf'
    text = text

    if max_line_length:
        lines = textwrap.wrap(text, max_line_length)
    else:
        lines = [text]
            
    for line in lines:
        metrics = draw.get_font_metrics(combined_image, line, False)
        text_width = metrics.text_width
        draw.text(abs(round(x - text_width //2)), round(y), line)
        y += font_size


draw = Drawing()
second_combined_images(images[:1])

draw_text(draw, 300, 'white', 'NEW RESIDENCE IN DUBAI', first_image.width * 50 // 100, first_image.height * 85 // 100, max_line_length=15)
draw_text(draw, 300, 'black', 'BEDS 10', first_image.width + second_image.width * 15 // 100, second_image.height * 80 // 100, max_line_length=4)
draw_text(draw, 300, 'black', 'FLOOR 43', first_image.width + second_image.width * 50 // 100, second_image.height * 80 // 100, max_line_length=5)
draw_text(draw, 300, 'black', 'SQ.FT 4893', first_image.width + second_image.width * 85 // 100, second_image.height * 80 // 100, max_line_length=5)

draw(combined_image)



combined_image.save(filename='generate.jpg')
for image in images:
    image.close()

first_image.close()
second_image.close()
combined_image.close()