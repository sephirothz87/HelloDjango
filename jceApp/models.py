from django.db import models
 
class Model(models.Model):
	# id = models.AutoField()
	qxwx_login_id = models.CharField(max_length=20)

	class Meta:
		db_table='jce_change_subscriber'
