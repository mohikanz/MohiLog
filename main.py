# vim: fileencoding=utf-8

from __future__ import unicode_literals

from datetime import datetime
import json


class MohiLogger(object):
    template_name = 'template/log.tpl'
    template = None
    channel_dict = None
    user_dict = None
    emoji_dict = None

    def __init__(self, **kwargs):
        """
            settings.pyを作り、
            チャンネル一覧取得用のトークン(slack_token),
            会話履歴取得用のトークン(slack_token2)を設定すること
        """

        from settings import SLACK_TOKEN, SLACK_TOKEN2
        from slacker import Slacker
        from jinja2 import Environment, FileSystemLoader

        self.slack = Slacker(SLACK_TOKEN)
        self.slack2 = Slacker(SLACK_TOKEN2)
        self.channel_dict = self._get_channel_dict()
        self.user_dict = self._get_user_dict()
        self.user_reverse_dict = self._get_user_reverse_dict()
        self.emoji_dict = self._get_emoji_dict()
        # template
        env = Environment(loader=FileSystemLoader('.'))
        self.template = env.get_template(self.template_name)

    def _get_channel_dict(self):
        """
            {チャネル名:  ID}の辞書を返す。
        """
        res = self.slack.channels.list(exclude_archived=1)
        return {d['name']: d['id'] for d in res.body['channels']}

    def _get_user_dict(self):
        """
            {ユーザ名: (id, icon_url,)}の辞書を返す。
        """
        res = self.slack.users.list()
        return {
            m['name']: (m['id'], m['profile']['image_32'])
            for m in res.body['members']}

    def _get_user_reverse_dict(self):
        """
           {ユーザID: 名前} の辞書を返す。
        """
        d = {}
        for username in self.user_dict:
            id = self.user_dict[username][0]
            d[id] = username
        return d

    def _get_emoji_dict(self):
        """"
            {絵文字: url}の辞書を返す。
        """
        res = self.slack2.emoji.list()
        return res.body['emoji']

    def get_channel_history(self, id):
        """
            channelの書き込み履歴を返す。
            取得にはtoken2が必要。
        """
        res = self.slack2.channels.history(id)
        return res.body['messages']

    def display_ts(self, ts):
        """ unix epoch(float) からdatetimeへの変換 """
        return '{0:%Y-%m-%d %H:%M}'.format(datetime.fromtimestamp(ts))

    def get_channel_log(self, channel):
        """
            チャンネルのログを取得する
            その際にユーザの名前、emojiのURLを埋め込む。
        """
        channel_id = self.channel_dict[channel]
        messages = self.get_channel_history(channel_id)
        for message in messages:
            self.process_each_message(message)
        return {'messages': messages}

    def process_each_message(self, message):
        user_id = message.get('user')
        message['username'] = (
            self.user_reverse_dict.get(user_id) or
            message.get('username'))
        message['img_url'] = (
            self.user_dict.get(message['username'], ('', ''))[1])
        message['text'] = self._replace_text(message['text'])
        message['dt'] = self.display_ts(float(message['ts']))
        for reaction in message.get('reactions', []):
            emoji_name = reaction['name']
            reaction['url'] = self.emoji_dict.get(emoji_name, '')
            users_name = []
            for user_id in reaction['users']:
                users_name.append(self.user_reverse_dict.get(user_id))
            reaction['users_name'] = users_name

    def _replace_text(self, text):
        # TODO: リンクをanchorタグに変換
        # TODO: 絵文字をimgタグに変換
        return text

    def render_to_template(self, context):
        return self.template.render(context)


ml = MohiLogger()
context = ml.get_channel_log(u'tsurai')
html = ml.render_to_template(context)

# テンプレートファイルへの流し込み
fh = open("generate.html", 'w')
fh.write(html.encode('utf-8'))
fh.close()

# JSONデータの保存
history = json.dumps(context)
fh = open("history.json", 'w')
fh.write(history.encode('utf-8'))
fh.close()
