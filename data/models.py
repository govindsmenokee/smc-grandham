from django.db import models

class Book(models.Model):
	
	Language = models.TextField(unique=False)
	DDC = models.TextField(unique=False)
	Title = models.TextField(unique=False)
	Author = models.TextField(unique=False)
	Titleorg = models.TextField(unique=False)
	Vol = models.TextField(unique=False)
	Edition = models.TextField(unique=False)
	Series = models.TextField(unique=False)
	Year = models.TextField(unique=False)
	publisher = models.TextField(unique=False)
	Preface = models.TextField(unique=False)
	Illustrator = models.TextField(unique=False)
	Pages = models.TextField(unique=False)
	Length = models.TextField(unique=False)
	Price = models.TextField(unique=False)
	Note = models.TextField(unique=False)
	Location = models.TextField(unique=False)
	def __unicode__(self):
		return self.Title


class DDC(models.Model):
	
	DDC = models.TextField(unique=False)
	subject= models.TextField(unique=False)
	def __unicode__(self):
		return self.DDC


class Author(models.Model):

	Author = models.TextField(unique=False)
	def __unicode__(self):
		return self.Author

class Title_word(models.Model):

	word = models.TextField(unique=False)
	def __unicode__(self):
		return self.word

