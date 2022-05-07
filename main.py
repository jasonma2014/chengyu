import json

from fastapi import FastAPI

app = FastAPI()


@app.get("/words")
async def get_words():
    with open('idiom.json', encoding='utf-8') as f:
        data = json.load(f)
        idiom_list = []
        for item in data:
            idiom_list.append(item["word"])
        print(len(idiom_list))
        return {"words": idiom_list}


@app.get("/words/next/{pre}")
async def get_next_words(pre: str):
    with open('idiom.json', encoding='utf-8') as f:
        data = json.load(f)
        words = [item["word"] for item in data if str(item["word"]).startswith(pre)]
        return words

