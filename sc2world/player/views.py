from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext

from forms import PlayerCreateForm, PlayerUpdateForm
from models import Player


def show(request, id, template_name='player/show.html'):
    """
    Show a player.
    """
    if request.method == 'GET':
        player = get_object_or_404(Player, pk=id)
        return redirect(player, permanent=True)
    else:
        return HttpResponseRedirect(request.path)

def title(request, slug, template_name='player/show.html'):
    """
    Show a player by it's slug.
    """
    if request.method == 'GET':
        player = get_object_or_404(Player, is_removed=False, slug=slug)
    else:
        return HttpResponseRedirect(request.path)

    context = RequestContext(request, {
        'player': player,
        'now': datetime.now(),
    })
    return render_to_response(template_name, context)

def create(request, form_class=PlayerCreateForm, template_name='player/create.html'):
    """
    Add a player.
    """
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.remote_address = request.META['REMOTE_ADDR']
            player.save()
            return redirect(player)
    elif request.method == 'GET':
        form = form_class()
    else:
        return HttpResponseRedirect(request.path)

    context = RequestContext(request, {
        'form': form,
    })
    return render_to_response(template_name, context)

def update(request, id, form_class=PlayerUpdateForm, template_name='player/update.html'):
    """
    Update an existing player.
    """
    player = get_object_or_404(Player, pk=id)

    if request.method == 'POST':
        form = form_class(request.POST, instance=player)
        if form.is_valid():
            player = form.save()
            return redirect(player)
    elif request.method == 'GET':
        player.password = ""
        form = form_class(instance=player)
    else:
        return HttpResponseRedirect(request.path)

    context = RequestContext(request, {
        'player': player,
        'form': form,
    })
    return render_to_response(template_name, context)

