from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    title       = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(max_digits=9, decimal_places=2)
    summary     = models.TextField()
    featured    = models.BooleanField(default=False) # null=True OR default=True
    
    # 
    #  product_dynamic_view
    # product/<int:id>/
    def get_obsolute_url(self):
        return reverse("products:product_dynamic_view", kwargs={'id': self.id})
    
    # intial_update_datas
    # product/update/<int:id>/
    def get_obsolute_url_update(self):
        return reverse("products:intial_update_datas", kwargs={'id': self.id})
    
    # del_product
    # 'product/<int:id>/delete/'
    def get_obsolute_url_del(self):
        return reverse("products:delete_product", kwargs={'id': self.id})

    # product_create_db
    # product/create/
    def get_absolute_url_create(self):
        return reverse("products:product_create_view")
    
    # product_list_view
    def get_obsolute_url_home(self):
        return reverse("products:product_list_view")
        
        
    def __str__(self):
        return self.title

