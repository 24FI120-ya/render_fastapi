from typing import Optional

from fastapi import FastAPI

from fastapi.responses import HTMLResponse

import random  # randomライブラリを追加

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return omikuji_list[random.randrange(10)]

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>バドミントンの歴史</title>
        </head>
        <body>
            <h1>バドミントンの歴史</h1>
            <p>バドミントンは19世紀初頭のインドで行われていた「プーナ」という遊びに由来します。</p>
            <p>1873年、イギリスの侯爵がインドから持ち帰り、紹介したのが始まりとされている。</p>

            <h2>主な出来事</h2>
            <ul>
                <li>19世紀後半：イギリスで競技として発展</li>
                <li>1934年：国際バドミントン連盟設立</li>
                <li>1992年：オリンピック正式種目に採用</li>
            </ul>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
