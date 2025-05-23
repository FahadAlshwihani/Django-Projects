# Generated by Django 5.2 on 2025-04-09 15:48

from django.db import migrations

def create_sample_comments(apps, schema_editor):
    Comment = apps.get_model('blog', 'Comment')
    User = apps.get_model('auth', 'User')
    Post = apps.get_model('blog', 'Post')

    comments = [
        (1, 2, "Great introduction to Django!"),
        (1, 5, "Very informative article."),
        (2, 3, "These tips are really helpful."),
        (3, 7, "I love traveling and exploring nature!"),
        (4, 4, "Beautifully written article about photography."),
        (6, 8, "Healthy eating is so important for overall well-being."),
        (7, 9, "I enjoy reading different genres of books."),
        (8, 10, "Graphic design is such a creative field."),
        (9, 6, "Yoga and meditation have changed my life."),
        (10, 1, "Positive thinking can make a huge difference in one's life."),
    ]

    for post_id, user_id, content in comments:
        post = Post.objects.get(id=post_id)
        user = User.objects.get(id=user_id)
        Comment.objects.create(post=post, user=user, content=content)

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20250409_1839'),
    ]

    operations = [
    ]
