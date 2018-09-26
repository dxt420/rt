from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'aa':'active'}
    return render(request,'ayy/index.html',context)


def flight(request):
    context = {'bb':'active'}
    return render(request,'ayy/flight-homepage.html',context)
    
def hotel(request):
    context = {'cc':'active'}
    return render(request,'ayy/hotel-homepage.html',context)

def tour(request):
    context = {'dd':'active'}
    return render(request,'ayy/tour-homepage.html',context)

def cruise(request):
    context = {'ee':'active'}
    return render(request,'ayy/cruise-homepage.html',context)

def car(request):
    context = {'ff':'active'}
    return render(request,'ayy/car-homepage.html',context)

def flightdetail(request):
    context = {'bb':'active'}
    return render(request,'ayy/flight-detail.html',context)


def hoteldetail(request):
    context = {'cc':'active'}
    return render(request,'ayy/hotel-detail.html',context)

def tourdetail(request):
    context = {'dd':'active'}
    return render(request,'ayy/tour-detail.html',context)

