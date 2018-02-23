# MohiLog - mohikanz.slack.comのアレをアレする
## GOAL
最近流れが早いのですぐに見れなくなるので
- 日毎にログを収集
- 絵文字も全て収集
- jinja2でHTML化
- zipで固めてGoogle Driveに投稿
- ↑を共有設定にして、どこかのチャンネルにリンクを自動投稿
- どこかのブログに転送も考えたが、無料で使わせてもらってるのでそれもなんだか
- というわけでバックアップ用ログと言う位置づけ

## REQUIREMENT
- python2.7 (3でも大体OKなはず)
- jinja2
- Slacker
- APIを叩くためのトークンを自分で取得してsettings.pyに置いておく

## STATUS
まだ実験段階なのでいろいろと汚い

- DONE:データの取得
- WORKING:テンプレートへのデータの流し込み
  - テンプレートのデザインが死滅しているので助け・・・
- NOT_YET: Gdriveへのアップロード
- NOT_YET: 自動投稿
