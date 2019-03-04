# Generated by Django 2.1.4 on 2019-02-20 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doubt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发表时间')),
                ('star', models.IntegerField()),
                ('comments', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '帖子',
                'verbose_name_plural': '帖子',
                'db_table': 'doubt',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='DoubtComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='正文')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('is_enable', models.BooleanField(default=True, verbose_name='是否显示')),
                ('star', models.IntegerField(default=0, verbose_name='点赞')),
                ('is_doubt_comments', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doubt_comment_set', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('doubt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discuss.Doubt', verbose_name='问题')),
                ('parent_comment', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='discuss.DoubtComment', verbose_name='上级评论')),
                ('reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doubt_commented_set', to=settings.AUTH_USER_MODEL, verbose_name='回复')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'db_table': 'doubt_comment',
                'ordering': ['-created_time'],
                'get_latest_by': 'created_time',
            },
        ),
    ]