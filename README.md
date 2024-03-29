# HOMETE
近年話題になっている、SNSでの誹謗中傷を解決すべくHOMETEは誕生しました。  
HOMETEの最大の特徴は、一方向SNSです。  
投稿に対して返信はできません。できるのは心のこもったリアクションです。  

## 使い方
* **投稿**  
メニューバーから投稿するを押します。  
投稿内容が入力できたら、投稿する から投稿を完了させます。

* **リアクション**  
画面中央にある投稿のリアクションボタンを押します。  
気に入った投稿や応援したい投稿にリアクションをすることが可能です。

## テストアカウント
**URL**  
https://www.homete.tk  
※PCでの閲覧を推奨します。
- ユーザーID : HometeGuest
- パスワード : guestpass

## 機能
* ユーザ登録
	* メールアドレス認証
* ログイン / ログアウト
	* パスワード再設定
* 投稿機能
* リアクション追加 / 削除

## 使用技術
**バックエンド**
* Python 3.10.0
	* Flask
	* SQLAlchemy
	* Gunicorn
* MySQL 8.0.27
* Redis 6.2.6

**フロントエンド**
* JavaScript
	* Vue 2.6.11
	* Vuetify 2.4.0

**インフラ**
* Git / GitHub
* Docker / Docker-Compose
* AWS
	* ACM
	* S3
	* EC2 / ALB
	* Route53
	* CloudFront

## 開発エピソード
**チーム開発**  
私たちは、開発を進めるにあたり、ワークングアグリーメントを定めました。  
相手を思いやるコミュニケーションの取り方や、タスクの分配方法などを定めて、開発に取り組んできました。  
その結果、心理的安全性が確保され、チーム作業の効率化を図れたと感じています。

**開発方法**  
GitHubのissueを活用した、チケット駆動開発で開発を行ってきました。  
issueごとにブランチを切り、完了したらプルリクエストを出し、レビューを行い、マージする。  
このサイクルを繰り返すことで、タスク管理を明確化し、ミスを減らすことに成功しました。 

**WEB開発**  
SPAで作成することにより、モダンなページ設計やREST APIの設計など、現代のWEB開発に必要な技術を網羅的に習得することができました

**セキュリティ**  
新規登録時のメール認証はJWTを使用することで、DBを必要としないセキュアでミニマムな環境を整えました。  
ログイン後はJWTを使用せず、HttpOnly属性のcookieを使用しセッション管理をしています。  
また、バックエンドでのセッションの保存には、NoSQLのRedisを使用しています。インメモリDBを使用することで、RDBMSと比較してオーバヘッドを小さくすることができました。

## 開発者
* 齋藤 悠大 - Yudai Saito
	* GitHub : https://github.com/Yudai-Saito
* 白鳥 練 - Ren Shiratori
	* GitHub : https://github.com/shiratoriren
