# Mathematics API

##  仕様
フィボナッチ数列を返すAPI

### n番目のフィボナッチ数が返ってくる場合
**リクエスト例**
```
curl -X GET -H "Content-type: application/json" "https://mgd-mathematics-api.herokuapp.com/fib?n=99"
```
**レスポンス例**
```json
{
  "result": 218922995834555169026
}
```

### 不正なパラメータによりエラーが返ってくる場合
**リクエスト例**
```
curl -X GET -H "Content-type: application/json" "https://mgd-mathematics-api.herokuapp.com/fib?n="
```
**レスポンス例**
```json
{
  "message": {
    "n": [
      "field 'n' cannot be coerced: invalid literal for int() with base 10: ''",
      "must be of integer type"
    ]
  },
  "status": 400
}
```

## 環境構築
```bash
docker-compose up
```

## Docker内に移動
```bash
docker container exec -it app bash
# 上のコマンドで動作しない場合
docker container exec -it app /bin/sh
```

## テストの実行


## デプロイ
```bash
# Docker内、mainブランチ
git push heroku main
```

## 本番環境
https://mgd-mathematics-api.herokuapp.com
