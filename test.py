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

draw = Drawing()

def residence_name(font_size, color, text):
    draw.font_size = font_size
    draw.fill_color = Color(color)
    draw.font = 'arial.ttf'
    text = text

    x1 = first_image.width * 14 // 100
    y1 = first_image.height * 85 // 100

    x, y = x1, y1

    font_size_ots = (first_image.width - (x1 * 2)) // 182  
    max_line_lenght = 15
    lines = textwrap.wrap(text, max_line_lenght)
    
    for line in lines:
        metrics = draw.get_font_metrics(first_image,line, False)
        text_width = metrics.text_width
        draw.text(round(x), round(y), line)
        x = text_width//2.5
        y += font_size

    draw(combined_image)


def beds_info(font_size, color, text):
    draw.font_size = font_size
    draw.fill_color = Color(color)
    draw.font = 'arial.ttf'
    text = text

    x1 = first_image.width + second_image.width * 15 // 100
    y1 = second_image.height * 80 // 100
    
    x, y = x1, y1
    
    max_line_lenght = 4
    lines = textwrap.wrap(text, max_line_lenght)
    for line in lines:
        metrics = draw.get_font_metrics(second_image,line, False)
        text_width = metrics.text_width
        x = x1 - text_width//2
        draw.text(round(x), round(y), line)
        y += font_size
    draw(combined_image)

def floor_info(font_size, color, text):
    draw.font_size = font_size
    draw.fill_color = Color(color)
    draw.font = 'arial.ttf'
    text = text

    x1 = first_image.width + second_image.width * 50 // 100
    y1 = second_image.height * 80 // 100
    x, y = x1, y1

    max_line_lenght = 5
    lines = textwrap.wrap(text, max_line_lenght)
    for line in lines:
        metrics = draw.get_font_metrics(second_image,line, False)
        text_width = metrics.text_width
        x = x1 - text_width//2
        draw.text(round(x), round(y), line)
        y += font_size
    draw(combined_image)


def sqft_info(font_size, color, text):
    draw.font_size = font_size
    draw.fill_color = Color(color)
    draw.font = 'arial.ttf'
    text = text

    x1 = first_image.width + second_image.width * 85 // 100
    y1 = second_image.height * 80 // 100
 
    x, y = x1, y1

    max_line_length = 5
    lines = textwrap.wrap(text, max_line_length)
    for line in lines:
        metrics = draw.get_font_metrics(second_image,line, False)
        text_width = metrics.text_width
        x = x1 - text_width//2
        draw.text(round(x), round(y), line)
        y += font_size
    draw(combined_image)



second_combined_images(images[:2])   
residence_name(300, 'white', 'NEW RESIDENCE IN DUBAI')
beds_info(300, 'black', 'BEDS10')
floor_info(300, 'black', 'FLOOR43')
sqft_info(300, 'black', 'SQ.FT4893')


combined_image.save(filename='generate.jpg')
for image in images:
    image.close()

first_image.close()
second_image.close()
combined_image.close()