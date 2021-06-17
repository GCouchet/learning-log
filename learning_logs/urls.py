"""Defines URL patterns for learning_logs."""
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics,
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),  # /<int:topic_id>/ busca un integer, lo guarda en la variable
    # Page for adding a new Topic                                topic_id y lo va a utilizar la funcion topic() en views
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),  # <int:topic_id> captures a numerical value and assigns it to the variable topic_id
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # Page for deleting an entry
    path('delete_entry/<int:entry_id>', views.delete_entry, name='delete_entry'),
    ]
