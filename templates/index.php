{% extends 'base.html' %}
{% load render_table from django_tables2 %}
{% load table_tags %}

{% block title %}To-do Lists{% endblock %}
{% block header %}Logged in as {{uname}}{% endblock %}
{% if request.user.is_authenticated %}
    {% block content %}
    {% render_table table %}
    <div class="row">
        <div class="col-lg-12">                            
                <h1 class="page-header">
                    Add/Edit Activities<br>
                </h1>
                <ul>
                    <li>To add an activity, use a new and unique activity name
                    <li>To edit an existing activity, use the same activity name
                    <li>Deadline Format: YYYY-MM-DD or YYYY-MM-DD HH:MM
                </ul>                                               
        </div>
    </div class="row">
    <form method="post" class="form-horizontal"> {% csrf_token %}
        <div class="form-group col-sm-7">
            {{ form_edit.as_p }}
            <input type="submit" value = "Save" class="btn btn-info">
        </div>
    </form>
    {% endblock %}
{% endif %}