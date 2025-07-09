from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from django.shortcuts import redirect
from .models import Testimonial
from .forms import TestimonialForm


# Create your views here.

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
