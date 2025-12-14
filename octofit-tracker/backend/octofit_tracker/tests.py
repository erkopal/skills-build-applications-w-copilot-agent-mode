from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')
    def test_user_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', name='Test User', team=team)
        self.assertEqual(str(user), 'test@example.com')
    def test_activity_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', name='Test User', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=30, date='2025-12-14')
        self.assertEqual(str(activity), 'test@example.com - run')
    def test_workout_create(self):
        workout = Workout.objects.create(name='Pushups')
        self.assertEqual(str(workout), 'Pushups')
    def test_leaderboard_create(self):
        team = Team.objects.create(name='Test Team')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(str(leaderboard), 'Test Team - 100 pts')
