# AI チャット for Website(API)

API にリクエストを送ることで自社ウェブサイトの情報を学習させ、その情報をもとに ChatGPT が回答をしてくれます。

自社の住所や、EC サイトの商品情報まで、ウェブサイト上のものはすべて ChatGPT に学習させることが出来ます。

自由にソースを変更して利用ください。

## 使い方

env に`OPENAI_API_KEY`を設定し、uvicorn で main.py の app を実行してください。

```bash
uvicorn main:app
```

### 学習させる

/crawl/ここにページ URL を入力

ページ URL には、`https://`を書かないでください。

```
/crawl/{url:path}
```

### 回答させる

/question/ここにドメイン/質問内容

```
/question/{domain:str}/{question:str}
```
