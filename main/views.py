from datetime import datetime

from django.contrib.comments.models import Comment
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from sc2world.player.models import Player


def index(request, template_name='main/index.html'):
    """
    Index page.
    """
    if request.method == 'GET':
        players = Player.objects.filter(is_removed=False).order_by('-created_at')[:500]
        last_players = Player.objects.filter(is_removed=False).order_by('-created_at')[:10]
    else:
        return HttpResponseRedirect(request.path)

    context = RequestContext(request, {
        'players': players,
        'last_players': last_players,
        'player_total': Player.objects.count(),
        'now': datetime.now(),
    })
    return render_to_response(template_name, context)

def recent_updated(request, template_name='main/recent_updated.html'):
    """
    Return players sorted by recently updated.
    """
    if request.method == 'GET':
        players = Player.objects.filter(is_removed=False).order_by('-updated_at')[:200]
    else:
        return HttpResponseRedirect(request.path)

    context = RequestContext(request, {
        'players': players,
        'player_total': Player.objects.count(),
        'now': datetime.now(),
    })
    return render_to_response(template_name, context)

def recent_commented(request, template_name='main/recent_commented.html'):
    """
    Return players sorted by recently commented.
    """
    if request.method == 'GET':
        # Hack to get recent commented. Getting all recent comments,
        # get the player object id, and remove duplicates. Then retrive player instances
        # using the ids.
        # Probably better approach is to capture comment stats thru Comments signals.

        ids = Comment.objects.all().values_list('object_pk', flat=True).order_by('-submit_date')[:500]
        ids = reduce(lambda l, x: int(x) not in l and l.append(int(x)) or l, ids, [])
        player_dict = Player.objects.in_bulk(ids[:200])
        players = [player_dict[id] for id in ids if not player_dict[id].is_removed]
    else:
        return HttpResponseRedirect(request.path)

    context = RequestContext(request, {
        'players': players,
        'player_total': Player.objects.count(),
        'now': datetime.now(),
    })
    return render_to_response(template_name, context)
