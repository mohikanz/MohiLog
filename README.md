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
- mohikanzでなくてもスラックワークスペースであれば普通に動くはず

## REQUIREMENTS
- SEE [requirements.txt](https://github.com/mohikanz/MohiLog/blob/master/requirements.txt)
- APIを叩くためのトークンを自分で取得してroot/settings.pyに置いておく

## STATUS
まだ実験段階なのでいろいろと汚い

### DONE

- データの取得
- テンプレートへのデータの流し込み

### TODO

- ソート順が逆になっているので要修正
- テンプレートのデザインが死滅しているので助け・・・
- jsonの生データも残しておきたい
- Gdriveへのアップロード
- 自動投稿
- 例外関連
- モジュールとして独立させる
- 出来ればラムダかなんかで動かしたい
- google spreadsheetへの書き込み

### LICENSE

MPL(Mohikan Public License) - Fully compatible with MIT
