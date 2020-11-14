from django.db import models
from ckeditor.fields import RichTextField


class Offer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=100)
    primary_category = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=100)
    preview_text = models.CharField(max_length=300)
    product_detail = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    offer = models.ForeignKey(
        Offer, on_delete=models.CASCADE, blank=True, null=True)
    main_image = models.ImageField(upload_to='pics')
    sub_image_1 = models.ImageField(upload_to='pics', blank=True, null=True)
    sub_image_2 = models.ImageField(upload_to='pics', blank=True, null=True)
    sub_image_3 = models.ImageField(upload_to='pics', blank=True, null=True)
    price = models.FloatField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    """@property
    def imageURL(self):
        try:
            url = (self.sub_image_1.url,
                   self.sub_image_2.url, self.sub_image_3.url)
        except:
            url = ''
        return url"""
