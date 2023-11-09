from PIL import Image, ImageDraw, ImageOps, ImageFont
import random

scale = 1


def random_text():
    # 오늘의 운세 목록
    list = [
        "행복한 하루가 될 예정이에요!",
        "좋은 일이 생길 거예요!",
        "오늘은 행운의 날이에요!",
        "재미있는 하루가 될 거예요!",
        "배우는 게 많은 하루가 될 거예요!",
        "공부가 잘 되는 날이에요!",
        "맛있는 걸 먹을 수 있는 날이에요!",
        "지식이 머리에 쏙쏙 들어오는 날이에요!",
        "친구들과 재미있는 시간을 보낼 거예요!",
        "하루 종일 웃을 수 있는 날이에요!",
        "지치지 않고 에너지가 넘치는 날이에요!",
        "인기쟁이가 되는 날이에요!",
        "즐거운 일이 생길 거예요!",
        "성취감을 느낄 수 있는 날이에요!",
        "좋은 소식이 들려오는 날이에요!",
    ]
    return list[random.randint(0, len(list) - 1)]


def image_frame(file):
    img = Image.open(file)
    img = ImageOps.scale(img, scale)
    img = ImageOps.expand(img, border=(0, 0, 0, 200 * scale), fill="white")

    I1 = ImageDraw.Draw(img)

    title = ImageFont.truetype("Binggrae.ttf", 24 * scale)
    content = ImageFont.truetype("Binggrae.ttf", 30 * scale)
    sub = ImageFont.truetype("Binggrae.ttf", 18 * scale)

    I1.text(
        (img.width / 2, img.height - 160 * scale),
        "♥ 오늘의 운세 ♥",
        fill=(0, 0, 0),
        font=title,
        anchor="mm",
    )
    I1.text(
        (img.width / 2, img.height - 105 * scale),
        random_text(),
        fill=(0, 0, 0),
        font=content,
        anchor="mm",
    )

    img.save(file)
    img = img.convert("L")
    # img.show()
    img.save("print_" + file)
