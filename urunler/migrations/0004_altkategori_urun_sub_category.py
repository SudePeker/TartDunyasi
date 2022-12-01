# Generated by Django 4.1.2 on 2022-11-12 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0003_urun_kategori'),
    ]

    operations = [
        migrations.CreateModel(
            name='AltKategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='urun',
            name='sub_category',
            field=models.ManyToManyField(to='urunler.altkategori'),
        ),
    ]