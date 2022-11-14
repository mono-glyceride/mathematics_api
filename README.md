# Mathematics API

##  仕様
フィボナッチ数列を返すAPI

**リクエスト例**
```
curl -X GET -H "Content-type: application/json" "https://mgd-mathematics-api.herokuapp.com/fib?n=99"
```
**レスポンス例**
正常に値が返ってきた場合
```json
{
  "result": 218922995834555169026
}
```

エラーの場合


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
