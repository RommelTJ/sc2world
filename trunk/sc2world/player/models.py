# Notes for later: change save method to self.author?

from django.db import models
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify

class Player(models.Model):
    """
    Represents a player location.
    """
    bnetnick       = models.CharField(max_length=100, unique=False)
    slug           = models.SlugField(max_length=100, unique=False, db_index=True)
    charactercode  = models.IntegerField(max_length=3)
    icon           = models.CharField(max_length=50)
    lat            = models.FloatField()
    lng            = models.FloatField()
    zoom           = models.IntegerField()
    details        = models.TextField()
    author         = models.CharField(max_length=50)
    remote_address = models.IPAddressField(null=True)
    password       = models.CharField(max_length=20)
    is_removed     = models.BooleanField(default=False)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.bnetnick)
        super(Player, self).save()

    def __unicode__(self):
        return self.bnetnick

    @models.permalink
    def get_absolute_url(self):
        return ('player-title', (), {'slug': self.slug})
