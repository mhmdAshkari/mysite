from django.shortcuts import render,redirect
from .forms import BMIForm
from django.http import JsonResponse
# Create your views here.
def index_views(request):
    form = BMIForm(request.POST)

    if form.is_valid():
        blood_pressure = request.POST.get('blood_pressure') # Retrieve the blood_Pressure
        cholesterol = request.POST.get('cholesterol') # Retrieve the cholesterol
        height = form.cleaned_data['height']
        age = request.POST.get('age') 
        weight = request.POST.get('weight')
        selected_gender = request.POST.get('selected_gender') # Retrieve the selected_gender
        blood_pressure = request.POST.get('blood_pressure') # Retrieve the blood_Pressure
        general_health = request.POST.get('general_health') # Retrieve the general_health
        physical_health = request.POST.get('physical_health') # Retrieve the physical
        mental_health = request.POST.get('mental_health') # Retrieve themental_
        heartattack = request.POST.get('heartattack') # Retrieve the heartbeat
        Fruits = request.POST.get('Fruits') # Retrieve the Fruits

    else:
        form = BMIForm()
    print("Fruits : ",Fruits)
    print("heartattack : ",heartattack)
    print("mental_health : ",mental_health)
    print('physical_health : ',physical_health)
    print("general_health : ",general_health)
    print("blood_Pressure : ",blood_pressure)
    print("cholesterol:",cholesterol)
    print("Height:", height)
    print("Age:", age)
    print("Weight:", weight)
    print("Selected Gender:", selected_gender)
    return render(request, 'index.html', {'form': form})

def ajax_post(request):
    if request.method == 'POST':
        data = request.POST.get('data')  # Adjust this according to your data format
        # Process the data or save it to the database
        #print(data)