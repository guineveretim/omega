from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from django.shortcuts import redirect
from .models import Testimonial
from .forms import TestimonialForm
from .models import Booking, ContactUs, Testimonial

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking, ContactUs, Testimonial
from .forms import BookingForm, ContactUsForm, TestimonialForm

# Dashboard view
@login_required
def admin_dashboard(request):
    bookings = Booking.objects.all()
    contacts = ContactUs.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, 'admin_dashboard.html', {
        'bookings': bookings,
        'contacts': contacts,
        'testimonials': testimonials,
    })

# Booking CRUD
@login_required
def edit_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'edit_form.html', {'form': form, 'title': 'Edit Booking'})

@login_required
def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('admin_dashboard')
    return render(request, 'confirm_delete.html', {'object': booking, 'title': 'Delete Booking'})

# ContactUs CRUD
@login_required
def edit_contact(request, pk):
    contact = get_object_or_404(ContactUs, pk=pk)
    if request.method == 'POST':
        form = ContactUsForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ContactUsForm(instance=contact)
    return render(request, 'edit_form.html', {'form': form, 'title': 'Edit Contact Message'})

@login_required
def delete_contact(request, pk):
    contact = get_object_or_404(ContactUs, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('admin_dashboard')
    return render(request, 'confirm_delete.html', {'object': contact, 'title': 'Delete Contact Message'})

@login_required
def edit_testimonial(request, slug):
    testimonial = get_object_or_404(Testimonial, slug=slug)
    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = TestimonialForm(instance=testimonial)
    return render(request, 'edit_form.html', {'form': form, 'title': 'Edit Testimonial'})

# Delete Testimonial
@login_required
def delete_testimonial(request, slug):
    testimonial = get_object_or_404(Testimonial, slug=slug)
    if request.method == 'POST':
        testimonial.delete()
        return redirect('admin_dashboard')
    return render(request, 'confirm_delete.html', {'object': testimonial, 'title': 'Delete Testimonial'})


def Home(request):
    # Fetch testimonials to display
    testimonials = Testimonial.objects.order_by('-created_at')  # latest first

    # Handle form submission
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to refresh page and show new testimonial
    else:
        form = TestimonialForm()

    context = {
        'testimonials': testimonials,
        'form': form,
    }
    return render(request, 'omegaservices/home.html', context)




def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Associate the booking with the logged-in user
            booking.save()  # Save the booking record

            # Redirect to the success page with the booking ID
            return redirect('booking_success', booking_id=booking.id) 
    else:
        form = BookingForm()
        
    return render(request, 'omegaservices/booking.html', {'form': form})
  
def about(request):
    return render(request, 'omegaservices/about.html')

def services(request):
    # Fetch testimonials to display
    testimonials = Testimonial.objects.order_by('-created_at')  # latest first

    # Handle form submission
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('services')  # Redirect to refresh page and show new testimonial
    else:
        form = TestimonialForm()

    context = {
        'testimonials': testimonials,
        'form': form,
    }
    return render(request, 'omegaservices/services.html')

def contact(request):
    return render(request, 'omegaservices/contact.html')
