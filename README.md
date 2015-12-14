#learn-django-queryset

Lets consider the following model
```
class Book(models.Model):
	name =  models.CharField(max_length=255)
	isbn = models.CharField(max_length=20)

	def __unicode__(self):
		return unicode(self.name)

```

<a name='insert-query'/>
####Insert

	* b = Book(name='The Immortals of Meluha', isbn='978123456789')
	> No Sql query here

