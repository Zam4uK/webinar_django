from django.db import models
from django.urls import reverse


class Tags(models.Model):
    name = models.CharField(max_length=255)


class Category(models.Model):
    name = models.CharField('Название катеории', max_length=255)


class Blog(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category,
                                 null=True,
                                 blank=True,
                                 on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs) -> None:
        return super().save(*args, **kwargs)
