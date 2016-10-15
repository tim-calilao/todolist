{% extends 'base.html' %}
{% block title %}Settings{% endblock %}
{% block header %}Email Notification <small>{{message}}</small>{% endblock %}
{% block content %}
	<div class="row">
		<div class="col-lg-12"><h4>
		{{message2}}
		</h4></div>
	</div>
	<br>

    <form method="post" class="form-inline"> {% csrf_token %}
        <div class="form-group col-sm-7">
            {{ form.as_p }}
            {% if user.is_authenticated %}
            <input type="submit" value = "Save" class="btn btn-default">
            {% endif %}
        </div>
    </form>

{% endblock %}