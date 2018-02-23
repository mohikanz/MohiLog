!DOCTYPE html>
<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>{{ title }}</title>
<meta charset="utf-8">
<meta name="description" content="">
<meta name="author" content="">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="">
<link rel="shortcut icon" href="">
</head>
<body>
{% for message in messages %}
<div>
    <div>
        {#
        {{ message.userimg }} {{ message.username }}
        {% endcomment %}
        #}
    </div>
    <div>
        {{ message.ts }} {{ message.text }}
    </div>
    <hr>
        {% for reaction in message.reactions %}
        <img src="{{ reaction.url }}" title="{% for user in reaction.users_name %}{{user}},{% endfor %}">
        {% endfor %}
    </div>
</div>
{% endfor %}
</body>
</html>
