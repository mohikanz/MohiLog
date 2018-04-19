# vim: fileencoding=utf-8

from __future__ import unicode_literals

import requests
import json
from datetime import datetime, timedelta
from jinja2 import Template, Environment, FileSystemLoader
from slacker import Slacker


class MohiLogger(object):
    template_name = 'template/log.tpl'
    template = None
    channel_dict = None
    user_dict = None

    def __init__(self, **kwargs):
        from settings import slack_token, slack_token2
        self.slack = Slacker(slack_token)
        self.slack2 = Slacker(slack_token2)
        self.channel_dict = self.get_channel_dict()
        self.user_dict = self.get_user_dict()
        self.user_reverse_dict = self.get_user_reverse_dict()

        # template
        env = Environment(loader=FileSystemLoader('.'))
        self.template = env.get_template(self.template_name)

    def get_channel_dict(self):
        """
            {チャネル名:  ID}の辞書を返す。
        """
        res = self.slack.channels.list(exclude_archived=1)
        return {d['name']: d['id'] for d in res.body['channels']}

    def get_user_dict(self):
        """
            {ユーザ名: (id, icon_url,)}の辞書を返す。
        """
        res = self.slack.users.list()
        return {m['name']: (m['id'], m['profile']['image_32']) for m in res.body['members']}

    def get_user_reverse_dict(self):
        """
           {ユーザID: 名前} の辞書を返す。
        """
        d = {}
        for username in self.user_dict:
            id = self.user_dict[username][0]
            d[id] = username
        return d

    def get_emoji_dict(self):
        """"
            {絵文字: url}の辞書を返す。
        """
        res = self.slack2.emoji.list()
        return res.body['emoji']

    def get_channel_history(self, id):
        res = self.slack2.channels.history(id)
        return res.body['messages']

    def restore_ts(self, ts):
        """ unix epoch(float) からdatetimeへの変換 """
        return datetime.fromtimestamp(ts)

    def get_channel_log(self, channel):
        """
            チャンネルのログを取得する
        """
        channel_id = self.channel_dict[channel]
        emoji_dict = self.get_emoji_dict()
        messages = self.get_channel_history(channel_id)
        for message in messages:
            user_id = message.get('user')
            username = self.user_reverse_dict.get(user_id) or message.get('username')
            for reaction in message.get('reactions', []):
                emoji_name = reaction['name']
                reaction['url'] = emoji_dict.get(emoji_name)
                users_name = []
                for user_id in reaction['users']:
                    users_name.append(self.user_reverse_dict.get(user_id))
                reaction['users_name'] = users_name
        return messages

    def render_to_template(context):
        self.output_text = template.render(context)


ml = MohiLogger()
log = ml.get_channel_log(u'lang_ジャバ')
print(log)
