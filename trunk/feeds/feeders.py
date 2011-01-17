from django.contrib.comments.models import Comment
from django.contrib.gis.feeds import Feed

from sc2world.player.models import Player


class LatestEntries(Feed):
    title = "StarCraft 2 Latest Players"
    link = "/"
    description = "Updates on latest entries in www.sc2geomap.com."

    def items(self):
        return Player.objects.filter(is_removed=False).order_by('-created_at')[:50]

    def item_geometry(self, item):
        return (item.lng, item.lat)

    def item_pubdate(self, item):
        return item.updated_at

    def item_author_name(self, item):
        return item.author

    def item_categories(self, item):
        return (item.icon,)

class CommentedEntries(Feed):
    title = "StarCraft 2 Recently Commented Players"
    link = "/recent/commented/"
    description = "Updates on recently commented entries in www.sc2geomap.com."

    def items(self):
        ids = Comment.objects.all().values_list('object_pk', flat=True).order_by('-submit_date')[:10]
        ids = reduce(lambda l, x: int(x) not in l and l.append(int(x)) or l, ids, [])
        player_dict = Player.objects.in_bulk(ids[:10])
        players = [player_dict[id] for id in ids if not player_dict[id].is_removed]
        return players

    def item_pubdate(self, item):
        return item.updated_at

    def item_author_name(self, item):
        return item.author

    def item_categories(self, item):
        return (item.icon,)

    def item_geometry(self, item):
        return (item.lng, item.lat)

class UpdatedEntries(Feed):
    title = "StarCraft 2 Recently Updated Players"
    link = "/recent/updated/"
    description = "Updates on recent updated entries in www.sc2geomap.com."

    def items(self):
        return Player.objects.filter(is_removed=False).order_by('-updated_at')[:10]

    def item_pubdate(self, item):
        return item.updated_at

    def item_author_name(self, item):
        return item.author

    def item_categories(self, item):
        return (item.icon,)

    def item_geometry(self, item):
        return (item.lng, item.lat)
