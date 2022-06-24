# Generated by Django 3.2.13 on 2022-06-24 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingridients',
            field=models.ManyToManyField(help_text='ингридиенты, необходимые для приготовления блюда', through='recipes.IngridientInRecipe', to='recipes.Ingridient'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(help_text='тэги рецепта', through='recipes.TagInRecipe', to='recipes.Tag'),
        ),
        migrations.AlterField(
            model_name='ingridientinrecipe',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingridients_in_recipe', to='recipes.recipe'),
        ),
        migrations.AlterField(
            model_name='taginrecipe',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags_in_recipe', to='recipes.recipe'),
        ),
    ]
