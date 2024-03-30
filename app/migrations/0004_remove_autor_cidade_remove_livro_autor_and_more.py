# Generated by Django 5.0.3 on 2024-03-30 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_emprestimolivro_alter_livro_editora_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='editora',
            name='cidade',
        ),
        migrations.DeleteModel(
            name='EmprestimoLivro',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='genero',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.DeleteModel(
            name='Autor',
        ),
        migrations.DeleteModel(
            name='Cidade',
        ),
        migrations.DeleteModel(
            name='Editora',
        ),
        migrations.DeleteModel(
            name='Genero',
        ),
        migrations.DeleteModel(
            name='Livro',
        ),
    ]
