from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from django.shortcuts import redirect


# Create your views here.

def Home(request):
  return render(request, 'omegaservices/home.html')




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
