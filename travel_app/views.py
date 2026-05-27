from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterForm, TravelForm
from .models import TravelPreference

# Registration
def register_view(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect('login')

    return render(request, 'register.html', {'form': form})

# Login
def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'login.html')

# Dashboard
def dashboard(request):

    form = TravelForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            travel = form.save(commit=False)
            travel.user = request.user
            travel.save()

            return redirect('recommendation')

    return render(request, 'dashboard.html', {'form': form})

# Recommendation
def recommendation(request):

    latest = TravelPreference.objects.filter(
        user=request.user
    ).last()

    result = ""

    if latest.place_type == "Hill" and latest.weather == "Cool":

        result = "Ooty, Manali, Shimla"

    elif latest.place_type == "Beach" and latest.weather == "Hot":

         result = "Goa, Maldives, Pondicherry"

    elif latest.place_type == "Mountain":

        result = "Ladakh, Himachal Pradesh"

    elif latest.place_type == "Temple":

      result = """
    Tirupati,
    Varanasi,
    Kedarnath,
    Bhadrachalam,
    Rameshwaram
    """

    elif latest.place_type == "Historical":

       result = """
    Taj Mahal,
    Hampi,
    Jaipur,
    Delhi Red Fort
    """

    elif latest.place_type == "Adventure":

       result = """
    Rishikesh,
    Manali,
    Goa Water Sports,
    Leh Ladakh Bike Trip
    """

    else:

       result = "Kerala, Mysore"

    return render(request, 'recommendation.html',
                  {'result': result})