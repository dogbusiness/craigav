# Generated by Django 4.2.4 on 2023-09-24 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aggregator", "0004_alter_media_name_alter_media_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="city",
            field=models.CharField(max_length=200, verbose_name="City"),
        ),
        migrations.AlterField(
            model_name="post",
            name="description",
            field=models.CharField(max_length=1500, verbose_name="Description"),
        ),
        migrations.AlterField(
            model_name="post",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=12, verbose_name="Price"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=50, verbose_name="Title"),
        ),
        migrations.AlterField(
            model_name="subcategory",
            name="name",
            field=models.CharField(
                choices=[
                    ("Cars", "Cars"),
                    ("Motorcycles", "Motorcycles"),
                    ("Trucks", "Trucks and Special Equipment"),
                    ("Water", "Water"),
                    ("Parts and Accessories", "Parts and Accessories"),
                    ("Overseas Properties", "Overseas Estate"),
                    ("Apartments", "Apartments"),
                    ("Rooms", "Rooms"),
                    ("Houses", "Houses"),
                    ("Parking", "Parking"),
                    ("Commercial Properties", "Commercial Properties"),
                    ("Vacancies", "Vacancies"),
                    ("IT/Telecom", "IT/Telecom"),
                    ("Business Services", "Business Services"),
                    ("Tutoring", "Tutoring"),
                    ("Building", "Building"),
                    ("Other", "Other"),
                    ("Clothes and Footwear", "Clothes and Footwear"),
                    ("Clothes and Footwear for Kids", "Clothes and Footwear for Kids"),
                    ("Baby Products and Toys", "Baby Products and Toys"),
                    ("Accessories", "Accessories"),
                    ("Health and Beauty", "Health and Beauty"),
                    ("Household Equipment", "Household Equipment"),
                    ("Furniture and Interior", "Furniture and Interior"),
                    ("Dishes and Kitchen Equipment", "Dishes and Kitchen Equipment"),
                    ("Groceries", "Groceries"),
                    ("Maintenance and Building", "Maintenance and Building"),
                    ("Plants", "Plants"),
                    ("Audio and Video", "Audio and Video"),
                    ("Videogaming", "Videogaming"),
                    ("Personal Computers", "Personal Computers"),
                    ("Laptops", "Laptops"),
                    ("Phones", "Phones"),
                    ("Other", "Other"),
                    ("Tickets", "Tickets"),
                    ("Bikes", "Bikes"),
                    ("Books and Magazines", "Books and Magazines"),
                    ("Collecting", "Collecting"),
                    ("Hunting and Fishing", "Hunting and Fishing"),
                    ("Sports and Leisure", "Sports and Leisure"),
                    ("Dogs", "Dogs"),
                    ("Cats", "Cats"),
                    ("Birds", "Birds"),
                    ("Fish", "Fish"),
                    ("Other Pets", "Other Pets"),
                    ("Pest Products", "Pest Products"),
                    ("Business for Sale", "Business for Sale"),
                    ("Business equipment", "Business equipment"),
                ],
                max_length=30,
                verbose_name="Name",
            ),
        ),
        migrations.AlterModelTable(
            name="category",
            table='content"."category',
        ),
        migrations.AlterModelTable(
            name="media",
            table="content.media",
        ),
        migrations.AlterModelTable(
            name="post",
            table="content.post",
        ),
        migrations.AlterModelTable(
            name="subcategory",
            table='content"."subcategory',
        ),
    ]