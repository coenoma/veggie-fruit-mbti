# API仕様書

## エンドポイント一覧

### POST /quiz/submit_answer
回答を送信する

#### リクエスト
```json
{
    "answer": "A" or "B"
}
```

#### レスポンス
```json
{
    "success": true
}
```

### GET /result
診断結果を取得する

#### レスポンス
```json
{
    "mbti_type": "INTJ",
    "personality": {
        "fruit": "アボカド",
        "description": "説明文",
        "color": "#2E8B57"
    }
}
```
