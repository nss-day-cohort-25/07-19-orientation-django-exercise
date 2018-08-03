import unittest
from django.test import TestCase
from django.urls import reverse
from .models import Artist


class ArtistTest(TestCase):

    def test_list_artists(self):
        new_artist = Artist.objects.create(
            name="Suzy Saxophone",
            birth_date="12/25/58",
            biggest_hit="Honk Honk Squeak"
        )

        # Issue a GET request.
        # 'reverse' is used to generate a URL for a given view. The main advantage is that you do not hard code routes in your code.
        response = self.client.get(reverse('history:artists'))

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 1 artist.
        # The key 'artist_list' comes from the ArtistViewModel where we said context_object_name = 'artist_list'
        self.assertEqual(len(response.context['artist_list']), 1)

        # Is this stuff in the content of the body?
        # .encode converts from unicode to utf-8
        # example:
        # If the string is: pythön!
        # The encoded version is: b'pyth\xc3\xb6n!'
        self.assertIn(new_artist.name.encode(), response.content)

    def test_get_artist_form(self):

      response = self.client.get(reverse('history:artist_form'))

      self.assertIn(
          '<input type="text" name="name" maxlength="100" required id="id_name" />'.encode(), response.content)

    def test_post_artist(self):

      response = self.client.post(reverse('history:artist_form'), {'name': 'Bill Board', 'birth_date': '10/31/67', 'biggest_hit': "So Blue Fer You"})

      # Getting 302 back because we have a success url and the view is redirecting under the covers?
      self.assertEqual(response.status_code, 302)
