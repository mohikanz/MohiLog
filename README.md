# MohiLog - mohikanz.slack.comのアレをアレする
## GOAL
最近流れが早くすぐに見れなくなる、、、ので
- 日毎にログを収集
- 絵文字も全て収集
- jinja2でHTML化
- zipで固めてGoogle Driveに投稿
- ↑を共有設定にして、どこかのチャンネルにリンクを自動投稿
- どこかのブログに転送も考えたが、無料で使わせてもらってるのでそれもなんだか
- というわけでバックアップ用ログと言う位置づけ

## REQUIREMENTS
- SEE [requirements.txt](https://github.com/mohikanz/MohiLog/blob/master/requirements.txt)
- APIを叩くためのトークンを自分で取得してroot/settings.pyに置いておく

## STATUS
まだ実験段階なのでいろいろと汚い

- DONE:データの取得

- WORKING:テンプレートへのデータの流し込み
- ソート順が逆になっているので要修正
- テンプレートのデザインが死滅しているので助け・・・
- jsonの生データも残しておきたい
- NOT_YET: Gdriveへのアップロード
- NOT_YET: 自動投稿
- NOT_YET: 例外関連
