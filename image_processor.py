from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import os

def create_image_with_title(image_url, title):
    try:
        # download the image using requests library
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))

        # create a white extension on top of the image
        width, height = img.size
        extension_height = 50
        top_extension = Image.new('RGB', (width, extension_height), (255, 255, 255))
        img_with_extension = Image.new('RGB', (width, height+extension_height), (255, 255, 255))
        img_with_extension.paste(top_extension, (0, 0))
        img_with_extension.paste(img, (0, extension_height))

        # create a white extension on bottom of the image
        width, height = img_with_extension.size
        bottom_extension_height = 50
        bottom_extension = Image.new('RGB', (width, bottom_extension_height), (255, 255, 255))
        img_with_extension_with_bottom = Image.new('RGB', (width, height+bottom_extension_height), (255, 255, 255))
        img_with_extension_with_bottom.paste(img_with_extension, (0, 0))
        img_with_extension_with_bottom.paste(bottom_extension, (0, height))

        # split the title in two
        middle_index = len(title) // 2
        first_half = title[:middle_index].rsplit(' ', 1)[0]
        second_half = title[len(first_half):]

        # write the news title on the white strap
        draw = ImageDraw.Draw(img_with_extension_with_bottom)
        font = ImageFont.truetype("arial.ttf", 20)

        # write the first half of the news title on the top white strap
        first_half_width, first_half_height = draw.textsize(first_half, font=font)
        first_half_x = (width - first_half_width) // 2
        first_half_y = (extension_height - first_half_height) // 2
        draw.text((first_half_x, first_half_y), first_half, font=font, fill=(0, 0, 0))

        # write the second half of the news title on the bottom white strap
        second_half_width, second_half_height = draw.textsize(second_half, font=font)
        second_half_x = (width - second_half_width) // 2
        second_half_y = height + ((extension_height - second_half_height) // 2)
        draw.text((second_half_x, second_half_y), second_half, font=font, fill=(0, 0, 0))

        # save the final image in the "final_images" folder
        if not os.path.exists("final_images"):
            os.mkdir("final_images")
        
        filtered_title = purify(title)
        file_name = f"{filtered_title}.jpg"
        file_path = os.path.join("final_images", file_name)
        img_with_extension_with_bottom.save(file_path)

        # return the path for the final image
        return [file_path , file_name]
    except Exception as e:
        print(f"ERROR while 'create_image_with_title': {e}")
        return [None , None]

def purify(sentence):
    filtered_sentence = ""
    chars = [" ", "." , "<" , ">" , ":" , '"' , "/" , "\\" ,"|" , "?" , "*" , "%" , "#" , "@" , "!" , "}" , "{" , "+" , "-" , "=" , ")" , "(" , "&" , "$" , "_" , "'" , "`" , "~" , ";" , "," , "[" , "]" , ]
    for char in sentence:
        if char not in chars:
            filtered_sentence += char
    return filtered_sentence
