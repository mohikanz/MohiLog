# MohiLog - mohikanz.slack.comのアレをアレする
## GOAL
最近流れが早くすぐに見れなくなる、、、ので
- 日毎にログを収集
- HTML, JSON, GSpread形式で出力
- mohikanzでなくてもスラックワークスペースであれば普通に動くはず


## REQUIREMENTS
- SEE [requirements.txt](https://github.com/mohikanz/MohiLog/blob/master/requirements.txt)
- APIを叩くためのトークンを自分で取得してroot/settings.pyに置いておく


## USAGE
$ python main.py <options>...


### オプション
- -c 取得チャンネル

    デフォルト： #tsurai

- -t 出力タイプ

    json(デフォルト), html, gspread

- -o 出力ファイル名

    デフォルトではmohikanz.(type)となる

    "-o -" で標準出力に


## STATUS
Beta


### DONE

- データの取得
- テンプレートへのデータの流し込み


### TODO

- テンプレートのデザインが死滅しているので助け・・・
- google spreadsheetへの書き込み
- 自動投稿
- ラムダ対応


### CONTRIBUTER

@udgw, @a-yasui

Your contributions are always welcomed.

### LICENSE

MPL(Mohikan Public License) - Fully compatible with MIT
