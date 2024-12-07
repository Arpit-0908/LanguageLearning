from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm, RegistrationForm  # Import your forms here

def base(request):
    return render(request, 'base.html')
# Index view
def index(request):
    return render(request, 'index.html')

def review(request):
    return render(request, 'review.html')

def Language(request):
    return render(request, 'MainLanguage.html')
def quiz_view(request):
    return render(request, 'quiz.html')

def Japan_view(request):
    return render(request, 'Japan.html')

def Spanish_view(request):
    return render(request, 'Spanish.html')
def French_view(request):
    return render(request, 'French.html')
def German_view(request):
    return render(request, 'German.html')
def Hindi_view(request):
    return render(request, 'Hindi.html')
# Login view
from django.contrib import messages  # Ensure this import is present
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages  # Ensure this import is present
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)  # Log the user in
                # Add a success message for successful login
                messages.success(request, f"WELCOME BACK ,  {username}!")
                return redirect('index')  # Redirect to the home page or dashboard
            else:
                # If the user is not found, add an error message
                messages.error(request, 'Error: The username or password is incorrect.')
                return render(request, 'login.html', {'form': form})  # Render the form with errors
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


# Registration view
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user instance
            login(request, user)  # Automatically log in the user after registration
            messages.success(request, 'Registration successful! Welcome!')
            return redirect('index')  # Redirect to a home page or another appropriate page
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

def chat_view(request):
    return render(request, 'chat.html')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Define class details in a dictionary
CLASS_DETAILS = {
    'French Beginners': {
        'teacher_name': 'Madame Rousseau',
        'image_url': 'img/french-beg.jpg',  # Change to correct path
        'price': 50
    },
    'French Advanced': {
        'teacher_name': 'Monsieur Bouchard',
        'image_url': 'img/french-ad.jpg',  # Change to correct path
        'price': 65
    },
    'Spanish Beginners': {
        'teacher_name': 'Maria Gonzalez',
        'image_url': 'img/spansih-beg.jpg',  # Change to correct path
        'price': 50
    },
    'Spanish Advanced': {
        'teacher_name': 'Señorita Castill',
        'image_url': 'img/spansih-ad.jpg',
        'price': 70
    },
    'Japanense Beginners': {
        'teacher_name': 'Sensei Nakamura',
        'image_url': 'img/japan_beg.jpg',  # Change to correct path
        'price': 60
    },
    'Japanense Advanced': {
        'teacher_name': ' Akira Yamamotori',
        'image_url': 'img/japan_ad.jpg',
        'price': 75
    },
    'English': {
        'teacher_name': ' Johnsin Smithsen',
        'image_url': 'img/eng.jpg',
        'price': 40
    },
    'Hindi': {
        'teacher_name': ' Sushma Srivastava',
        'image_url': 'img/hindilog.jpg',
        'price': 45
    },
    # Add more classes as needed
}
from django.contrib import messages

def book_slot(request):
    if request.method == 'POST':
        # Retrieve details from the form
        class_name = request.POST.get('class_name')
        time_slot = request.POST.get('time_slot')

        if not time_slot:
            messages.error(request, 'Please select a time slot before booking.')
            return redirect('Bookclass')  # Redirect to the booking page
        
        # Look up class details in the dictionary
        class_details = CLASS_DETAILS.get(class_name)

        if class_details:
            teacher_name = class_details['teacher_name']
            image_url = class_details['image_url']
            price = class_details['price']
            total_price = price  # For simplicity, assuming a fixed price

            # Save booking details in session
            request.session['booking_details'] = {
                'class_name': class_name,
                'teacher_name': teacher_name,
                'image_url': image_url,
                'time_slot': time_slot,
                'price': price,
                'total_price': total_price
            }

            # Redirect to payment gateway
            return redirect('payment')  # Redirect to the payment page
        else:
            messages.error(request, 'Selected class is unavailable.')
            return redirect('index')  # Or redirect to an error page

    return render(request, 'Bookclass.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

def send_confirmation_email(user_email, booking_details):
    subject = f"Confirmation for {booking_details['class_name']} Class"
    message = f"""
    Dear Student,

    Thank you for registering for our class! We're excited to have you on board.

    Here are your booking details:
    - Class: {booking_details['class_name']}
    - Teacher: {booking_details['teacher_name']}
    - Time Slot: {booking_details['time_slot']}
    - Price: ${booking_details['price']}

    Additional Information:
    - Please ensure you have a stable internet connection for the class.
    - If you need to reschedule or cancel, kindly inform us at least 24 hours in advance.
    - You will receive a reminder email 1 hour before the class begins.
    
    We look forward to seeing you in class and helping you achieve your language learning goals.

    If you have any questions or need further assistance, feel free to reach out to us at support@italki.com.

    Best regards,
    Italki - The Language Learning Team
    """

    sender_email = settings.EMAIL_HOST_USER  # Sender email from settings
    recipient_email = [user_email]

    try:
        send_mail(subject, message, sender_email, recipient_email, fail_silently=False)
        return True
    except Exception as e:
        # You can log or print the error for debugging
        print(f"Error sending email: {e}")
        return False

def payment_view(request):
    # Retrieve booking details from session
    booking_details = request.session.get('booking_details')

    if not booking_details:
        return redirect('book_slot')

    if request.method == 'POST':
        user_email = request.POST.get('email')

        if not user_email:
            messages.error(request, "Please provide an email address.")
            return redirect('payment')

        # Send confirmation email
        email_sent = send_confirmation_email(user_email, booking_details)

        if email_sent:
            messages.success(request, "Payment successful! A confirmation email has been sent.")
            return redirect('index')  # Redirect to the index page or another appropriate page
        else:
            messages.error(request, "Payment successful, but the confirmation email could not be sent.")
            return redirect('index')  # Redirect to index if email could not be sent

    return render(request, 'payment.html', {'booking_details': booking_details})
