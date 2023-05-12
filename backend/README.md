# WELCOME TO BACKEND

## 必要ファイルを用意する

- `.env.dev`
- `firebase_account_key.json`
  - 上記 2 点のファイルを `/backend/` 配下に用意してください
  - 中身はバックエンド管理者から共有してもらってください
  - `firebase_account_key.json` は秘密鍵なので口外禁止です！扱いに気をつけてください！

## 初めてコンテンを起動する

1. 古いバージョンのボリュームがある場合は削除

```bash
docker volume rm 古いバックエンドのボリューム

# docker volume ls でボリューム一覧が見れます
# ボリュームがが消せない場合はコンテナが起動してる可能性があります。 docker stop コンテナ名 で停止してから削除しましょう
```

2. イメージをビルド

```bash
docker-compose build --no-cache
```

3. コンテナを起動

```bash
make up
```

4. Python コンテナへ入る

```bash
docker-compose exec python bash
```

5. Python コンテナで DB のマイグレーションを実行(エラーが出ているが無視して OK)

```bash
flask db upgrade

# 完了したらexitで抜ける
```

6. ようこそバックエンドへ 😇

## コンテナの起動の仕方

自動で Python と MySQL のコンテンが立ち上がります

```bash
make up
```

コンテナのログが出力されます

```bash
make log

# Pythonコンテナのログがたまに止まるので、止まっていたら ctl + c (cmd + c) で抜けてもう一度log出力し直してください
```

## コンテナへの入り方

### Python

```bash
docker-compose exec python bash
```

### MySQL

```bash
docker-compose exec mysql bash
```

```bash
mysql -u homete -p

# password : hometepass
```

```bash
use homete;

# 各種SQLが実行できます
```
