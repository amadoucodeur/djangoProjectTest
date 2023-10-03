from django.test import TestCase
from django.contrib.auth.models import User
from .models import Model3d, Badge, UserProfile
from .serializers import Model3dSerializer, BadgeSerializer, UserProfileSerializer, UserSerializer
from rest_framework.test import APIClient
from rest_framework import status


class Model3dTestCase(TestCase):
    def setUp(self):
        # Créez un utilisateur pour le test
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Créez un badge pour le test
        self.badge = Badge.objects.create(name='Star', description="le modèle d'un utilisateur a plus de 1k views")

    def test_model3d_creation(self):
        # Test de la création d'un modèle 3D
        model3d = Model3d.objects.create(user=self.user, name='Test Model', image='model_images/test.jpg', views=0)
        self.assertEqual(model3d.name, 'Test Model')
        self.assertEqual(model3d.views, 0)
        self.assertEqual(model3d.user, self.user)

class UserProfileTestCase(TestCase):
    def setUp(self):
        # Créez un utilisateur pour le test
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Créez un badge pour le test
        self.badge = Badge.objects.create(name='Test Badge', description='Test Description')

    def test_userprofile_creation(self):
        # Test de la création d'un profil utilisateur
        user_profile = UserProfile.objects.create(account=self.user)
        user_profile.badge.add(self.badge)
        self.assertEqual(user_profile.account, self.user)
        self.assertEqual(user_profile.badge.count(), 1)

class BadgeTestCase(TestCase):
    def test_badge_creation(self):
        # Test de la création d'un badge
        badge = Badge.objects.create(name='Star', description="le modèle d'un utilisateur a plus de 1k views")
        self.assertEqual(badge.name, 'Star')
        self.assertEqual(badge.description, "le modèle d'un utilisateur a plus de 1k views")

class UserSerializerTestCase(TestCase):
    def test_user_serializer(self):
        # Créez un utilisateur
        user = User.objects.create(username='testuser', email='test@example.com')

        # Créez un sérialiseur pour l'utilisateur
        serializer = UserSerializer(instance=user)

        # Vérifiez si les champs du sérialiseur correspondent aux champs de l'utilisateur
        self.assertEqual(serializer.data['username'], 'testuser')
        self.assertEqual(serializer.data['email'], 'test@example.com')

class BadgeSerializerTestCase(TestCase):
    def test_badge_serializer(self):
        # Créez un badge
        badge = Badge.objects.create(name='Test Badge', description='Test Description')

        # Créez un sérialiseur pour le badge
        serializer = BadgeSerializer(instance=badge)

        # Vérifiez si les champs du sérialiseur correspondent aux champs du badge
        self.assertEqual(serializer.data['name'], 'Test Badge')
        self.assertEqual(serializer.data['description'], 'Test Description')

class UserProfileSerializerTestCase(TestCase):
    def test_userprofile_serializer(self):
        # Créez un utilisateur
        user = User.objects.create(username='testuser')

        # Créez un profil utilisateur associé à cet utilisateur
        user_profile = UserProfile.objects.create(account=user)

        # Créez un badge
        badge = Badge.objects.create(name='Test Badge', description='Test Description')

        # Associez ce badge au profil utilisateur
        user_profile.badge.add(badge)

        # Créez un sérialiseur pour le profil utilisateur
        serializer = UserProfileSerializer(instance=user_profile)

        # Vérifiez si les champs du sérialiseur correspondent aux champs du profil utilisateur
        self.assertEqual(serializer.data['account']['username'], 'testuser')
        self.assertEqual(serializer.data['badges'][0]['name'], 'Test Badge')

class Model3dSerializerTestCase(TestCase):
    def test_model3d_serializer(self):
        # Créez un utilisateur
        user = User.objects.create(username='testuser')

        # Créez un modèle 3D associé à cet utilisateur
        model3d = Model3d.objects.create(user=user, name='Test Model', image='model_images/test.jpg', views=5)

        # Créez un sérialiseur pour le modèle 3D
        serializer = Model3dSerializer(instance=model3d)

        # Vérifiez si les champs du sérialiseur correspondent aux champs du modèle 3D
        self.assertEqual(serializer.data['name'], 'Test Model')
        self.assertEqual(serializer.data['user']['username'], 'testuser')

class Model3dViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.model3d = Model3d.objects.create(user=self.user, name='Test Model', image='model_images/test.jpg', views=5)
        self.client = APIClient()

    def test_model3d_detail_view(self):
        # Test de la vue Model3dDetailView (détail)
        response = self.client.get(f'/models/{self.model3d.id}/')  # Remplacez l'URL par celle de votre vue
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        initial_views = self.model3d.views
        response = self.client.get(f'/models/{self.model3d.id}/')  # Appel à la vue à nouveau
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.model3d.views, initial_views + 1)

class BadgeViewsTestCase(TestCase):
    def setUp(self):
        self.badge = Badge.objects.create(name='Test Badge', description='Test Description')
        self.client = APIClient()

    def test_badge_detail_view(self):
        # Test de la vue BadgeDetailView (détail)
        response = self.client.get(f'/badges/{self.badge.id}/')  # Remplacez l'URL par celle de votre vue
        self.assertEqual(response.status_code, status.HTTP_200_OK)

