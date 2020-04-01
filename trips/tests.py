import datetime
from django.test import TestCase
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.utils import timezone

from .models import Trip, Location


class TripModelTest(TestCase):

    def test_title_equal_to_string_representation(self):
        """
        Test that the title and string rep are the same
        """
        new_location = Location(name="Test Location")
        new_trip = Trip(title="Test Trip", location=new_location)
        self.assertTrue(new_trip.title, new_trip.__str__)
