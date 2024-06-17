from django.test import TestCase
from .models import *
# Create your tests here.

class UserProfileUpdateTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(name='Raingou', email='raingou@example.com', password='password124')

    def test_user_profile_update(self):
        updated_name = 'John Smith'
        self.user.name = updated_name
        self.user.save()
        updated_user = User.objects.get(email='raingou@example.com')
        self.assertEqual(updated_user.name, updated_name)

class ProjectCRUDTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(name='John Doe', email='john@example.com', password='password')
        self.project = RaingouProject.objects.create(title='My Project', description='Project description', techonolies_use='Django', user=self.user)

    def test_project_creation(self):
        project_count = RaingouProject.objects.count()
        self.assertEqual(project_count, 1)

    def test_project_update(self):
        updated_title = 'Updated Project'
        self.project.title = updated_title
        self.project.save()
        updated_project = RaingouProject.objects.get(id=self.project.id)
        self.assertEqual(updated_project.title, updated_title)

    def test_project_deletion(self):
        self.project.delete()
        project_count = RaingouProject.objects.count()
        self.assertEqual(project_count, 0)

class SkillTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(name='John Doe', email='john@example.com', password='password')

    def test_skill_addition_and_categorization(self):
        skill_name = 'Python'
        skill_category = 'Programming'
        skill = RaingouSkill.objects.create(user=self.user, name=skill_name, category=skill_category)
        self.assertEqual(skill.name, skill_name)
        self.assertEqual(skill.category, skill_category)