from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User.objects.create(email='tony@marvel.com', name='Tony Stark', team=marvel, is_superhero=True),
            User.objects.create(email='steve@marvel.com', name='Steve Rogers', team=marvel, is_superhero=True),
            User.objects.create(email='bruce@marvel.com', name='Bruce Banner', team=marvel, is_superhero=True),
            User.objects.create(email='clark@dc.com', name='Clark Kent', team=dc, is_superhero=True),
            User.objects.create(email='bruce@dc.com', name='Bruce Wayne', team=dc, is_superhero=True),
            User.objects.create(email='diana@dc.com', name='Diana Prince', team=dc, is_superhero=True),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Iron Man Suit Training', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Shield Throwing', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='Hulk Smash', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Flying', duration=50, date=timezone.now().date())
        Activity.objects.create(user=users[4], type='Detective Work', duration=40, date=timezone.now().date())
        Activity.objects.create(user=users[5], type='Amazon Training', duration=70, date=timezone.now().date())

        # Create workouts
        w1 = Workout.objects.create(name='Super Strength', description='Strength workout for superheroes')
        w2 = Workout.objects.create(name='Flight Training', description='Flight workout for superheroes')
        w1.suggested_for.set(users)
        w2.suggested_for.set([users[0], users[3], users[5]])

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, points=300)
        Leaderboard.objects.create(team=dc, points=350)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
