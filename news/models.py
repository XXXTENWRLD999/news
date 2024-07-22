from django.db import models

# Create your models here.
CHOISE = (
  ('one','Kursatilsin'),
  ('two','kursatilmasin')
)

class Category(models.Model):
  name = models.CharField(max_length=100)
  def __str__(self):
    return self.name



class News(models.Model):
  title = models.CharField(max_length=200)
  image = models.ImageField(upload_to='static/img')
  description = models.TextField()
  category = models.ForeignKey(Category,on_delete=models.CASCADE)
  status = models.CharField(max_length=14,
                            choices=CHOISE,
                            default='one')
  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
  

class Commentary(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  message = models.TextField()
  news_id = models.ForeignKey(News,on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now=True)
  update_at = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.name