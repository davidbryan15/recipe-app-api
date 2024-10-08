# """
# Test for the tags API
# """

# from django.contrib.auth import get_user_model
# from django.urls import reverse
# from django.test import TestCase

# from rest_framework import status
# from rest_framework.test import APIClient

# from core.models import Tag

# from recipe.serializers import TagSerializer

# TAGS_URL = reverse('recipe:tag-list')

# def detail_url(tag_id):
#   """return tag url"""
#   return reverse('recipe:tag-detail', args=[tag_id])

# def create_user(email='user@example.com', password='test123'):
#   """create and return user"""
#   return get_user_model().objects.create_user(email, password)

# class PublicTagApiTests(TestCase):
#   """Test unauthenticated API requests"""

#   def setUp(self):
#     self.client = APIClient

#   def test_auth_required(self):
#     """Test auth is required when retrieving tags"""
#     res = self.client.get(TAGS_URL)

#     self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

# class PrivateTagsApiTest(TestCase):
#   """Test authenticated api requests"""

#   def setUp(self):
#     self.user = create_user()
#     self.client = APIClient
#     self.client.force_authenticate(self.user)

#   def test_retrieve_tags(self):
#     """Retrieving a list of tags"""

#     Tag.objecte.create(user=self.user, name="Dessert")
#     Tag.objecte.create(user=self.user, name="Vegan")

#     res = self.client.get(TAGS_URL)

#     tags = Tag.objects.all().order_by('-name')
#     serializer = TagSerializer(tags, many=True)
#     self.assertEqual(res.status_code, status.HTTP_200_ok)
#     self.assertEqual(res.data, serializer.data)

#   def test_tags_limited_to_user(self):
#     """Test list of tags is limited to the authenticated user"""

#     user2 = create_user(email='user2@example.com')
#     Tag.objects.create(user=user2, name='Fruity')
#     tag = Tag.objects.create(user=user2, name='comfort food')

#     res = self.client.get(TAGS_URL)

#     self.assertEqual(res.status_code, status.HTTP_200_ok)
#     self.assertEqual(len(res.data), 1)
#     self.assertEqual(res.data[0]['name'], tag.name)
#     self.assertEqual(res.data[0]['id'], tag.id)

#   def test_update_date(self):
#     """update tag"""

#     tag = Tag.objects.create(user=self.user, name='After Dinner')

#     payload = {'name':'Dessert'}
#     url = detail_url(tag.id)
#     res = self.client.post(url, payload)

#     self.assertEqual(res.status_code, status.HTTP_200_ok)
#     tag.refresh_from_db()
#     self.assertEqual(tag.name, payload['name'])


