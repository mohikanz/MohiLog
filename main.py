# vim: fileencoding=utf-8

from __future__ import unicode_literals

from datetime import datetime
import json
import argparse
from mohilog import MohiLogger, MohiLogWriter


def main():
    """
        settings.pyを作り、
        チャンネル一覧取得用のトークン(slack_token),
        会話履歴取得用のトークン(slack_token2)を設定すること
    """
    # load settings
    from settings import SLACK_TOKEN, SLACK_TOKEN2
    ml = MohiLogger(SLACK_TOKEN, SLACK_TOKEN2)

    # load args
    parser = argparse.ArgumentParser(description='Mohikanz Log Fetcher')
    parser.add_argument('-c', '--channel', type=str, default='tsurai',
                        help='Fetching channel name')
    parser.add_argument('-t', '--type', type=str, default='json',
                        help='Data type')
    parser.add_argument('-o', '--output', type=str, default='',
                        help='Output file name')
    args = parser.parse_args()

    # get context
    context = ml.get_channel_log( unicode(args.channel, 'utf_8') )

    # output
    mlw = MohiLogWriter(context, unicode(args.type), unicode(args.output))
    mlw.write()


if __name__ == '__main__':
    main()
