# MohiLog - mohikanz.slack.comのアレをアレする
## GOAL
最近流れが早くすぐに見れなくなる、、、ので
- 日毎にログを収集
- 絵文字も全て収集
- jinja2でHTML化
- zipで固めてGoogle Driveに投稿
- と思ったけどスプレッドシートのが簡単そうなのでそうする
- ↑を共有設定にして、どこかのチャンネルにリンクを自動投稿
- どこかのブログに転送も考えたが、無料で使わせてもらってるのでそれもなんだか
- というわけでバックアップ用ログと言う位置づけ
- mohikanzでなくてもスラックワークスペースであれば普通に動くはず


## REQUIREMENTS
- SEE [requirements.txt](https://github.com/mohikanz/MohiLog/blob/master/requirements.txt)
- APIを叩くためのトークンを自分で取得してroot/settings.pyに置いておく


## USAGE
$ python main.py


### オプション
- -c 取得チャンネル

    デフォルト： #tsurai

- -t 出力タイプ

    json(デフォルト), html, gspread

- -o 出力ファイル名

    デフォルトではmohikanz.(type)となる

    -o - で標準出力に


## STATUS
まだ実験段階なのでいろいろと汚い


### DONE

- データの取得
- テンプレートへのデータの流し込み


### TODO

- テンプレートのデザインが死滅しているので助け・・・
- google spreadsheetへの書き込み
- 自動投稿
- 例外関連
- 出来ればラムダかなんかで動かしたい


### CONTRIBUTER
@udgw, @a-yasui
Your contributions are always welcomed.

### LICENSE

MPL(Mohikan Public License) - Fully compatible with MIT
