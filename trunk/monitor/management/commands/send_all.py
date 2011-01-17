import logging, smtplib
from datetime import datetime, timedelta

from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django.db.models import get_model
from django.template import Context
from django.template.loader import get_template

from sc2world.player.models import Player
from sc2world.monitor.models import Moniton


class Command(BaseCommand):
    """
    Called by cron job to iterate thru all monitons and send emails accordingly.
    Only check player reports for the last 24 hours.
    """
    def handle(self, *args, **options):
        # Get player reports in the last 24 hours.
        now = datetime(*args) if args else datetime.now()
        past = now - timedelta(1)
        latest_players = Player.objects.filter(is_removed=False, created_at__gt=past)

        # Iterate all monitons. Send emails on players that are of interest.
        for m in Moniton.objects.all():
            players = [x for x in latest_players if m.top >= x.lat and m.bottom <= m.right >= x.lng and m.left <= x.lng]
            if players:
                try:
                    send_mail('[SC2 GEOMAP] Notification of Players',
                        get_template('monitor/notification_email.txt').render(Context({'uuid': m.uuid, 'players': players})),
                        'noreply@sc2geomap.com', [m.email])
                except smtplib.SMTPException, e:
                    logging.error(e)
