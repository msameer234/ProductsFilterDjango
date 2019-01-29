from django.db import models
from datetime import datetime
# Create your models here.
class Products(models.Model):
	pTitle = models.CharField(max_length=200, default='')
	pBrand = models.CharField(max_length=200, default='')
	pModel = models.CharField(max_length=200, default='')
	pOS = models.CharField(max_length=200, default='')
	pProcessor = models.CharField(max_length=200, default='')
	pPrice = models.IntegerField(default=0)
	pCreated_at = models.DateTimeField(default=datetime.now, blank=True)
	def __str__(self):
		return self.pTitle
	class Meta:
		verbose_name_plural = "Products"
		