# Generated by Django 3.1.1 on 2020-10-11 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Facebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Instagram_Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram_user_id', models.CharField(max_length=64)),
                ('Photos', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gps', models.FloatField(max_length=32)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_id', models.CharField(max_length=64)),
                ('location_id', models.CharField(max_length=64)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReportUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cause_id', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='UnMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cause_id', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Tinder_Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('age', models.PositiveSmallIntegerField()),
                ('interests', models.CharField(max_length=512)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('about', models.TextField(blank=True)),
                ('work', models.CharField(blank=True, max_length=32, null=True)),
                ('max_distance', models.IntegerField()),
                ('age_range', models.PositiveSmallIntegerField()),
                ('privacy', models.BooleanField(default=True)),
                ('facebook_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.facebook')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.location')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Super_Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(choices=[('L', 'Like'), ('NI', 'Not Interested')], max_length=2)),
                ('liked_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SuperLikeGivenTo', to='core.tinder_account')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.match')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SuperLikeGivenBy', to='core.tinder_account')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.CharField(max_length=64)),
                ('message_content', models.TextField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('match_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.unmatch')),
                ('report_user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.reportuser')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.message'),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(choices=[('L', 'Like'), ('SL', 'Super Like'), ('NI', 'Not Interested')], max_length=2)),
                ('liked_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LikeGivenTo', to='core.tinder_account')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.match')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LikeGivenBy', to='core.tinder_account')),
            ],
        ),
    ]