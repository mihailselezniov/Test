from django.db import models

import datetime
from django.utils import timezone

class Store_lists_of_discounts(models.Model):
    date_save = models.DateTimeField('date save')
    data = models.TextField()