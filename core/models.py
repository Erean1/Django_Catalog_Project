from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Category(models.Model):
    title = models.CharField(max_length=155,blank=True,null=True)
    slug = models.SlugField(max_length=155,blank=True,null=True)
    image = models.ImageField(upload_to="categoriesmedia",blank=True,null=True)
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Film_Post(models.Model):
    title = models.CharField(max_length=155)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    director = models.CharField(max_length=155,blank=True,null=True)
    image = models.ImageField(upload_to="filmimgs",blank=True)
    description = models.CharField(max_length=255,blank=True,null=True)
    publication_date = models.DateField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=155,blank=True,null=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args,**kwargs)
    
    class Meta:
        verbose_name = "Film_Post"
        verbose_name_plural = "Film_Posts"

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Film_Post,on_delete=models.CASCADE,related_name="comments")
    content = models.CharField(max_length=155)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user} for {self.post}"
    
    