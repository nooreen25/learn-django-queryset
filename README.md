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
    QUERY = u'BEGIN' - PARAMS = ()
    INSERT INTO "queries_book" ("name", "isbn") VALUES (%s, %s)' - PARAMS = (u"'The Immortals of Meluha'", u"'978123456789'")
    ```

*   b = Book(name='Made in Japan', isbn='879123456789')<br/>
	b.save()<br/>
	b.isbn = '879123456780'<br/>
	b.save()<br/>

	```
	QUERY = u'BEGIN' - PARAMS = ()
	QUERY = u'INSERT INTO "queries_book" ("name", "isbn") VALUES (%s, %s)' - PARAMS = (u"'Made in Japan'", u"'879123456789'")
	QUERY = u'BEGIN' - PARAMS = ()
	QUERY = u'UPDATE "queries_book" SET "name" = %s, "isbn" = %s WHERE "queries_book"."id" = %s' - PARAMS = (u"'Made in Japan'", u"'879123456780'", u'7')
	```

*   Book.objects <br/>__*or*__ Book.objects.all()<br/>__*or*__ books = Book.objects.all()

	```
	No Sql query here
	```

*   print Book.objects.all()<br/>__*or*__ Book.objects.filter()

	```
	QUERY = u'SELECT "queries_book"."id", "queries_book"."name", "queries_book"."isbn" FROM "queries_book" LIMIT 21' - PARAMS = ()
	```

*   print Book.objects.filter(id=1)<br/>__*or*__  print Book.objects.all().filter(id=1)

	```
	QUERY = u'SELECT "queries_book"."id", "queries_book"."name", "queries_book"."isbn" FROM "queries_book" WHERE "queries_book"."id" = %s LIMIT 21' - PARAMS = (u'1',)
	```

*   Book.objects.all[:3]<br/>__*or*__ Book.objects.all()[3:5]

	```
	No Sql query here
	```

*	print Book.objects.all()[:3]

	```
	QUERY = u'SELECT "queries_book"."id", "queries_book"."name", "queries_book"."isbn" FROM "queries_book" LIMIT 3' - PARAMS = ()
	```

*	print Book.objects.all()[3:5]

	```
	QUERY = u'SELECT "queries_book"."id", "queries_book"."name", "queries_book"."isbn" FROM "queries_book" LIMIT 2 OFFSET 3' - PARAMS = ()
	```

*	Book.objects.all()[:6:2]<br/>__*or*__ print Book.objects.all()[:6:2]

	```
	QUERY = u'SELECT "queries_book"."id", "queries_book"."name", "queries_book"."isbn" FROM "queries_book" LIMIT 6' - PARAMS = ()
	```

	Note: The query fetches __n<sup>th</sup>__(here n=6) objects from the database but while printing it will only print every __i<sup>th</sup>__(here i=2) object.


*   print Book.objects.filter(id__in=[1])

	```
	QUERY = u'SELECT "queries_book"."id", "queries_book"."name", "queries_book"."isbn" FROM "queries_book" WHERE "queries_book"."id" IN (%s) LIMIT 21' - PARAMS = (u'1',)
	```

