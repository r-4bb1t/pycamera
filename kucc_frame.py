from PIL import Image, ImageDraw, ImageOps, ImageFont
import random

scale = 1


def random_text():
    list = [
        "코딩이 잘 되는 날이다.",
        "버그가 잘 잡히는 날이다.",
        "새로운 아이디어가 떠오른다.",
        "친구들과 협력하면 길하다.",
        "새로운 프로젝트에 도전해보자.",
        "집중력이 높은 날이다.",
        "회장에 출마해야 한다.",
    ]
    return list[random.randint(0, len(list) - 1)]


def image_frame(file):
    img = Image.open(file)
    img = ImageOps.scale(img, scale)
    img = ImageOps.expand(img, border=(0, 160 * scale, 0, 200 * scale), fill="white")

    logo = Image.open("logo.png")
    logo = ImageOps.scale(logo, 60 / img.width * scale)
    img.paste(logo, (round((img.width - logo.width) / 2), 30 * scale))

    I1 = ImageDraw.Draw(img)

    title = ImageFont.truetype("Galmuri7.ttf", 32 * scale)
    content = ImageFont.truetype("Galmuri7.ttf", 40 * scale)

    I1.text(
        (img.width / 2, img.height - 160 * scale),
        "~오늘의 운세~",
        fill=(0, 0, 0),
        font=title,
        anchor="mm",
    )
    I1.text(
        (img.width / 2, img.height - 100 * scale),
        random_text(),
        fill=(0, 0, 0),
        font=content,
        anchor="mm",
    )

    img.save(file)
    img = img.convert("L")
    # img.show()
    img.save("print_" + file)
