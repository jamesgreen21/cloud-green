from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from .models import Trip, Location


class TripIndexView(generic.ListView):
    model = Trip
    context_object_name = 'trips'

    def get_queryset(self):
        """Return the last five published questions."""
        return Trip.objects.order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Trips'
        context['nbar'] = 'trips'
        return context


class TripDetailView(generic.DetailView):
    model = Trip

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Trips'
        context['nbar'] = 'trips'
        return context


class TripCreateView(LoginRequiredMixin, generic.CreateView):
    """
    Create form for adding new trips
    """
    model = Trip
    fields = ['title', 'location', 'star']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Trips'
        context['nbar'] = 'trips'
        return context

    def form_valid(self, form):
        """
        Check that form submitted is valid and save
        """
        form.instance.user = self.request.user
        return super().form_valid(form)


class TripUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """
    Update form for editing trips
    """
    model = Trip
    fields = ['title', 'location', 'star']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Trips'
        context['nbar'] = 'trips'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return True


def star_trip(request, pk):
    """
    A view for toggling the 'star' trips
    """
    trip = get_object_or_404(Trip, pk=pk)
    if trip.star:
        trip.star = False
    else:
        trip.star = True
    trip.save()
    return redirect('trips:detail', trip.id)


def delete_trip(request, pk):
    """
    A view for deleting trips
    """
    trip = get_object_or_404(Trip, pk=pk)
    trip.delete()
    messages.success(request, 'The trip has been deleted')
    return redirect('trips:index')
