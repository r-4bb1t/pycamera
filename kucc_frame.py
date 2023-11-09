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
        "에러 메시지도 친절하게 나오는 날이다.",
        "뭐든지 스택 오버플로우에서 해결책을 찾을 수 있다.",
        "코드 리뷰에서 칭찬을 받는다.",
        "디버깅 전 커피 한 잔이 효율적이다.",
        "갑작스런 깨달음이 찾아올 것이다.",
        "희귀한 버그를 발견할 수 있는 날이다.",
        "함수 이름 짓기가 쉬운 날이다.",
        "모든 것이 예상보다 순조롭게 진행될 것이다.",
        "머리가 가볍고 창의성이 넘쳐날 것이다.",
        "자료구조와 알고리즘 공부가 잘 된다.",
        "오타가 적은 날이다.",
        "블로그를 쓰면 좋은 일이 생길 것이다.",
        "코드 리팩토링이 잘 된다.",
        "프로젝트를 완성할 수 있는 날이다.",
        "과감한 리팩토링이 필요한 날이다.",
        "새로운 기술을 도입하면 길하다.",
        "재미있는 아이디어가 떠오른다.",
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
    content = ImageFont.truetype("Galmuri7.ttf", 28 * scale)

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
