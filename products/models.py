from django.db import models

class Product(models.Model):
    # CATEGORY_CHOICES = (
    #     ('Mobile', 'Mobiles'),
    #     ('Computer', 'Computers'),
    #     ('Electronic', 'Electronics'),
    #     ('Gaming', 'Gaming'),
    #     ('Software', 'Software'),
    # )

    category = models.CharField(max_length=50, null=True, blank=True)
    # category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='product_images', null=True, blank=True)    
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name