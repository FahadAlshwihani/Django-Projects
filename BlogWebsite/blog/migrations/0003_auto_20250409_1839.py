from django.db import migrations

def create_sample_posts(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Category = apps.get_model('blog', 'Category')

    categories = {
        'Programming': 'Programming',
        'Productivity': 'Productivity',
        'Travel': 'Travel',
        'Art': 'Art',
        'Technology': 'Technology',
        'Health': 'Health',
        'Books': 'Books',
        'Design': 'Design',
        'Wellness': 'Wellness',
        'Self-Improvement': 'Self-Improvement',
    }

    posts = [
        ("Introduction to Django", "Lorem ipsum dolor sit amet.", "Programming", "2023-01-01"),
        ("Tips for Effective Time Management", "Lorem ipsum dolor sit amet.", "Productivity", "2023-01-05"),
        ("Exploring the Wonders of Nature", "Lorem ipsum dolor sit amet.", "Travel", "2023-01-10"),
        ("The Art of Photography", "Lorem ipsum dolor sit amet.", "Art", "2023-01-15"),
        ("Understanding Machine Learning Algorithms", "Lorem ipsum dolor sit amet.", "Technology", "2023-01-20"),
        ("Healthy Eating Habits for a Balanced Lifestyle", "Lorem ipsum dolor sit amet.", "Health", "2023-01-25"),
        ("Exploring the World of Literature", "Lorem ipsum dolor sit amet.", "Books", "2023-02-01"),
        ("Mastering the Basics of Graphic Design", "Lorem ipsum dolor sit amet.", "Design", "2023-02-05"),
        ("The Benefits of Yoga and Meditation", "Lorem ipsum dolor sit amet.", "Wellness", "2023-02-10"),
        ("The Power of Positive Thinking", "Lorem ipsum dolor sit amet.", "Self-Improvement", "2023-02-15"),
    ]

    for title, content, category_name, pub_date in posts:
        category = Category.objects.get(name=category_name)
        Post.objects.create(title=title, content=content, category=category, date_published=pub_date)

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20250409_1832'),  # Replace with your actual last migration
    ]

    operations = [
        migrations.RunPython(create_sample_posts),
    ]