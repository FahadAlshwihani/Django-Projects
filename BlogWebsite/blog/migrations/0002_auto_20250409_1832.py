from django.db import migrations


def create_sample_data(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Category = apps.get_model('blog', 'Category')

    # Create categories
    categories = [
        'Programming',
        'Productivity',
        'Travel',
        'Art',
        'Technology',
        'Health',
        'Books',
        'Design',
        'Wellness',
        'Self-Improvement'
    ]
    for cat in categories:
        Category.objects.create(name=cat)

    # Create users
    users = [
        ('johnsmith', 'johnsmith@example.com'),
        ('emilyjones', 'emilyjones@example.com'),
        ('davidwilson', 'davidwilson@example.com'),
        ('sarahbrown', 'sarahbrown@example.com'),
        ('michaelscott', 'michaelscott@example.com'),
        ('lisajohnson', 'lisajohnson@example.com'),
        ('alexturner', 'alexturner@example.com'),
        ('jessicabaker', 'jessicabaker@example.com'),
        ('matthewwright', 'matthewwright@example.com'),
        ('oliviawalker', 'oliviawalker@example.com'),
    ]

    for username, email in users:
        User.objects.create_user(username=username, email=email, password='password123')


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0001_initial'),  # Replace with your last migration file
    ]

    operations = [
        migrations.RunPython(create_sample_data),
    ]