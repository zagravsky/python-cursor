# Generated by Django 2.1.3 on 2018-12-06 11:56

from django.db import migrations


def add_done(apps, schema_editor):
    Post = apps.get_model('diary', 'Post')
    post = Post.objects.get(title='Title1')
    post.title = 'Done'
    post.save()


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_done),
    ]
