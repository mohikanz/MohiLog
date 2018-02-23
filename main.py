# vim: fileencoding=utf-8

from __future__ import unicode_literals

import requests
import json
from datetime import datetime
from slacker import Slacker
from jinja2 import Template, Environment, FileSystemLoader


class MohiLogger(object):
    slack_token = 'xoxb-318958510932-ddT3Lu8OBJoQuUiwRDUMtp8A'
    slack_token2 = 'xoxp-170644065895-208280779190-320032068631-0329d46605be5879ced1b36b741be877'
    template_name = 'template/log.tpl'
    template = None
    channel_dict = None
    user_dict = None

    def __init__(self, **kwargs):
        self.slack = Slacker(self.slack_token)
        self.slack2 = Slacker(self.slack_token2)
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
        pass

    def get_channel_history(self, id):
        res = self.slack2.channels.history(id)
        return res.body['messages']

    def resotre_ts(self, ts):
        """ ts: unix epoch(float) """
        # tsを日時に復元する
        return datetime.fromtimestamp(ts)

    def get_channel_log(self, channel):
        channel_id = self.channel_dict[channel]
        messages = self.get_channel_history(channel_id)
        print self.user_reverse_dict
        for message in messages:
            user_id = message.get('user')
            username = self.user_reverse_dict.get(user_id) or message.get('username')
            print username, ':  ', message['text'], message.get('reactions')

    def render_to_template(context):
        self.output_text = template.render(context)


ml = MohiLogger()
log = ml.get_channel_log(u'lang_ジャバ')

## user情報のdict埋め込み
#for m in messages:
#    username = m['username']
#    print username
#    m['userimg'] = users[username]
#
#
#print messages[0].keys()
#context = {
#    'messages': messages,
#}
#
#
#print(disp_text)
#
#
# userlist: [{}]
#   u'profile', u'updated', u'tz', u'name', u'deleted', u'is_app_user', u'is_bot',
#   u'tz_label', u'real_name', u'color', u'team_id', u'is_admin', u'is_ultra_restricted',
#   u'is_restricted', u'is_owner', u'tz_offset', u'id', u'is_primary_owner'
#
#       profile: {}
#       u'status_text', u'display_name', u'status_emoji', u'title', u'team', u'real_name', u'image_24',
#       u'phone', u'real_name_normalized', u'image_512', u'image_72',
#       u'image_32', u'image_48', u'skype', u'avatar_hash', u'display_name_normalized', u'email', u'image_192']
#
#    historyの中身: {}
#    [u'has_more', u'messages', u'ok', u'is_limited']
#       messages: {}
#       messages [[u'username', u'attachments', u'icons', u'text', u'ts', u'subtype', u'type', u'bot_id']]
