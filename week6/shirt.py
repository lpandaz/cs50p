import sys
from PIL import Image, ImageOps

length = len(sys.argv)
valid_outputs = ['jpeg', 'jpg', 'png']

if length > 3:
    sys.exit("Too many command-line arguments")
elif length < 3:
    sys.exit("Too few command-line arguments")
else:
    try:
        with open(sys.argv[1]) as file:
            first_end = sys.argv[1]
            second_end = sys.argv[2]

            if first_end[-3:] not in valid_outputs:
                sys.exit("Invalid input")
            elif second_end[-3:] not in valid_outputs:
                sys.exit("Invalid output")
            elif first_end[-3:] != second_end[-3:]:
                sys.exit("Input and output have different extensions")

            else:
                shirt = Image.open('shirt.png')
                new_img = Image.open(sys.argv[1])
                img_crop = ImageOps.fit(new_img, shirt.size)
                img_crop.paste(shirt, mask=shirt)
                img_crop.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")
