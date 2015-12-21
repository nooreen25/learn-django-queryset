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

*   Book(name='The Immortals of Meluha', isbn='978123456789')

	```
	No Sql query here
	```

*   b = Book(name='The Immortals of Meluha', isbn='978123456789').save()<br/>__*or*__
	Book.objects.create(name='My Experiments with Truth', isbn='897456789123')
	
	```
    SET SQL_AUTO_IS_NULL = 0
    INSERT INTO `queries_book` (`name`, `isbn`) VALUES ('The Immortals of Meluha', '978123456789')
    ```

*   b = Book(name='Made in Japan', isbn='879123456789')<br/>
	b.save()<br/>
	b.isbn = '879123456780'<br/>
	b.save()<br/>

	```
	SET SQL_AUTO_IS_NULL = 0
	INSERT INTO `queries_book` (`name`, `isbn`) VALUES ('Made in Japan', '879123456789')
	UPDATE `queries_book` SET `name` = 'Made in Japan', `isbn` = '879123456780' WHERE `queries_book`.`id` = 7
	```

*   Book.objects <br/>__*or*__ Book.objects.all()<br/>__*or*__ books = Book.objects.all()<br/>__*or*__
	Book.objects.filter()<br/>__*or*__ books = Book.objects.filter()

	```
	No Sql query here 			#querysets are lazily evaluated
	```

*   print Book.objects.all()<br/>__*or*__ print Book.objects.filter()

	```
	SELECT ••• FROM `queries_book` LIMIT 21
	```

*   print Book.objects.filter(id=1)<br/>__*or*__ print Book.objects.all().filter(id=1)<br/>__*or*__ print
	Book.objects.filter(pk=1)<br/>__*or*__ print Book.objects.filter(id__exact=1)

	```
	SELECT ••• FROM `queries_book` WHERE `queries_book`.`id` = 1 LIMIT 21
	```

*	Book.objects.get(id=1)<br/>__*or*__ print Book.objects.get(id=1)<br/>__*or*__ Book.objects.get(pk=1)<br/>
	__*or*__ print Book.objects.get(pk=1)<br/>__*or*__ print Book.objects.get(id__exact=1)

	```
	SELECT ••• FROM `queries_book` WHERE `queries_book`.`id` = 3
	```

	Note: `get` internally calls `filter` with an additional check of whether the length of queryset is one or not

*   Book.objects.all()[:3]<br/>__*or*__ Book.objects.all()[3:5]

	```
	No Sql query here
	```

*	print Book.objects.all()[:3]

	```
	SELECT ••• FROM `queries_book` LIMIT 3
	```

*	print Book.objects.all()[3:5]

	```
	SELECT ••• FROM `queries_book` LIMIT 2 OFFSET 3
	```

*	Book.objects.all()[:6:2]<br/>__*or*__ print Book.objects.all()[:6:2]

	```
	SELECT ••• FROM `queries_book` LIMIT 6
	```

	Note: The query fetches __n<sup>th</sup>__(here n=6) objects from the database but while printing it will only print every __i<sup>th</sup>__(here i=2) object.

*   print Book.objects.filter(id__in=[1])

	```
	SELECT ••• FROM `queries_book` WHERE `queries_book`.`id` IN (1) LIMIT 21
	```

<a name='field-lookups'/>
####Field Lookups

Field lookups specify the `WHERE` clause. They remain the same for `filter`, `get` and `exclude` with the only difference in their base query structure.

#####exact

*	print Book.objects.filter(id__exact=1)

	```
	SELECT `queries_book`.`id`, `queries_book`.`name`, `queries_book`.`isbn` FROM `queries_book` WHERE `queries_book`.`id` = 1 LIMIT 21
	```

*	print Book.objects.filter(id__exact=None)
	
	```
	SELECT `queries_book`.`id`, `queries_book`.`name`, `queries_book`.`isbn` FROM `queries_book` WHERE `queries_book`.`id` IS NULL LIMIT 21
	```

*	print Book.objects.filter(name__exact='tHE iMMORTALS OF mELUHA')

	```
	SELECT ••• FROM `queries_book` WHERE `queries_book`.`name` = 'tHE iMMORTALS OF mELUHA' LIMIT 21
	```

*	print Book.objects.filter(name__iexact='tHE iMMORTALS OF mELUHA')

	```
	SELECT ••• FROM `queries_book` WHERE `queries_book`.`name` LIKE 'tHE iMMORTALS OF mELUHA' LIMIT 21
	```

