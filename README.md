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
### 不正なメソッドによりエラーが返ってくる場合
**リクエスト例**
```
curl -X POST -H "Content-type: application/json" "https://mgd-mathematics-api.herokuapp.com/fib?n=1"
```
**レスポンス例**
```json
{
  "message": "The method is not allowed for the requested URL.",
  "status": 405
}
```
### パラメータについて
```bash
n
```
正常に処理されるパラメータの条件
- nに対してのみ値を渡している
- nに対して1以上の整数を渡している

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
```bash
# Docker内で行うこと
pytest -v --cov --cov-report=term-missing
```

## ステージング環境へのデプロイ
```bash
# mainブランチをデプロイする場合
git push staging main
```

## デプロイ
```bash
# mainブランチをデプロイする場合
git push heroku main
```

## ステージング環境
https://mgd-mathematics-api-staging.herokuapp.com

## 本番環境
https://mgd-mathematics-api.herokuapp.com
