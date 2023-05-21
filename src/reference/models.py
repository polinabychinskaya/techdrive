from django.db import models

# Create your models here.

class Title(models.Model):
    author = models.ForeignKey(
        'reference.Author',
        on_delete=models.PROTECT,
        verbose_name='Author',
        default=1
    )
    edition = models.ForeignKey(
        'reference.Edition',
        on_delete=models.PROTECT,
        verbose_name='Edition',
        default=1
    )
    genre = models.ForeignKey(
        'reference.Genre',
        on_delete=models.PROTECT,
        verbose_name='Genre',
        default=24
    )
    publishing_house = models.ForeignKey(
        'reference.PublishingHouse',
        on_delete=models.PROTECT,
        verbose_name='Publishing house',
        default=3
    )
    book_title = models.CharField(
        verbose_name='Book title',
        max_length=256
    )
    description = models.TextField(
        verbose_name='Book desciption',
        max_length=2048
    )

    def __str__(self):
        return self.book_title

class Author(models.Model):
    name = models.CharField(
        verbose_name='Author name',
        max_length=256
    )
    language = models.CharField(
        verbose_name='Original language',
        max_length=256
    )

    def __str__(self):
        return self.name

class Edition(models.Model):
    number = models.IntegerField(
        verbose_name='Edition number',
        null=True,
        blank=True
    )

    def __str__(self):
        return 'Edition ' + str(self.number)

class Genre(models.Model):
    name = models.CharField(
        verbose_name='Genre',
        max_length=256
    )
    description = models.TextField(
        verbose_name='Genre desciption',
        max_length=2048
    )

    def __str__(self):
        return self.name

class PublishingHouse(models.Model):
    name = models.CharField(
        verbose_name='Publishing house',
        max_length=256
    )
    country = models.CharField(
        verbose_name='Country',
        max_length=256
    )

    def __str__(self):
        return self.name