# Generated by Django 5.0.6 on 2024-08-09 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wwq', '0005_quizquestion_quizresult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
        migrations.AlterField(
            model_name='blog',
            name='week',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='quizquestion',
            name='option1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='quizquestion',
            name='option2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='quizquestion',
            name='option3',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='quizquestion',
            name='option4',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='quizquestion',
            name='question_text',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='quizresult',
            name='date_taken',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
