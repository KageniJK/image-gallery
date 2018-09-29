from django.db import models


class Location(models.Model):
    """
    class that defines the locations to be tagged on the images
    """

    location=models.CharField(max_length=30)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()


class Category(models.Model):
    """
    class that defines the categories that the images will fit under
    """

    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

    @classmethod
    def search_category(cls, search_term):
        # returns a searched image by category
        return cls.objects.filter(category__icontains=search_term)


class Picture(models.Model):
    """
    class that defines the images
    """

    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, default=1)
    category = models.ManyToManyField(Category)

    class meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save_picture(self):
        # saves the picture
        self.save()

    @classmethod
    def delete_picture(cls,id):
        # deletes the picture from database
        pic = cls.objects.filter(id=id)
        pic.delete()

    @classmethod
    def get_pic_by_id(cls,id):
        # gets a specific picture
        return cls.objects.filter(id=id)

    @classmethod
    def filter_by_loc(cls,location):
        # returns all the pictures from a specific location
        return cls.objects.filter(location=location)

    @classmethod
    def filter_by_cat(cls, category):
        # returns all the pictures from a specific location
        return cls.objects.filter(category=category)

    @classmethod
    def all_pics(cls):
        # gets all the pictures
        return cls.objects.all().order_by('-id')