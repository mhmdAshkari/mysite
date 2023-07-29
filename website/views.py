from django.shortcuts import render
from .forms import BMIForm
import numpy as np
import  tensorflow as tf
from tensorflow import keras
import h5py
from sklearn.preprocessing import StandardScaler
import os
from django.http import JsonResponse
try:
    with h5py.File('scaler.h5', 'r') as f:
        mean = f['mean'][:]
        scale = f['scale'][:]
        scaler = StandardScaler()
        scaler.mean_ = mean
        scaler.scale_ = scale
except Exception as e:
    print("Error reading the model file:", e)

try:
    # Load the model using tf.keras
    model = keras.models.load_model('model_history.h5')
    print("Model loaded successfully.")
except Exception as e:
    print("Error reading the model file:", e)



def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def calculate_risk(**args):
    dict_values_obj = args.values()

    # Convert to an array of integers using list comprehension
    result_array = np.array([int(value) for value in dict_values_obj])

    # Reshape the 1D array to a 2D array with 9 features (9 samples, 9 features)
    result_array = result_array.reshape(1, -1)

    try:
        # Make sure to use the loaded scaler to transform the data
        result_array = scaler.transform(result_array)
    except Exception as e:
        print("Error reading the model file:", e)

    percentage = model.predict(result_array) * 100
    formatted_prediction = f"{percentage[0][0]:.1f}"
    print(formatted_prediction , "%")
    risk = formatted_prediction
    return risk

risk = None
def index_views(request):
    global risk
    form = BMIForm(request.POST)
    if form.is_valid():
        try:
            cholesterol = request.POST.get('cholesterol') # Retrieve the cholesterol
            height = int(request.POST.get('height'))
            age = request.POST.get('age') 
            weight = int((request.POST.get('weight')).replace(' KG', ''))
            selected_gender = request.POST.get('selected_gender') # Retrieve the selected_gender
            blood_pressure = request.POST.get('blood_pressure') # Retrieve the blood_Pressure
            general_health = request.POST.get('general_health') # Retrieve the general_health
            physical_health = int((request.POST.get('physical_health')).replace(' Days', '')) # Retrieve the physical
            mental_health = int((request.POST.get('mental_health')).replace(' Days', '')) # Retrieve the mental_health
            heartattack = request.POST.get('heartattack') # Retrieve the heartbeat
            Fruits = request.POST.get('Fruits') # Retrieve the Fruits
            calculate = request.POST.get('calc')
            BMI = calculate_bmi(weight, height/100)
            if int(calculate)==1:
                risk = (calculate_risk(BMI=BMI,age=age,general_health=general_health,physical_health=physical_health, 
                        blood_pressure=blood_pressure,mental_health=mental_health,  cholesterol=cholesterol,
                        heartattack=heartattack, 
                        Fruits=Fruits ))
                return JsonResponse({'risk': risk})



        except Exception as e:
            print(e)
    else:
        pass
    try:
        print(calculate)
        print("BMI : ",BMI)
        print("Fruits : ",Fruits)
        print("heartattack : ",heartattack)
        print("mental_health : ",mental_health)
        print('physical_health : ',physical_health)
        print("general_health : ",general_health)
        print("blood_Pressure : ",blood_pressure)
        print("cholesterol:",cholesterol)
        print("Age:", age)

    except Exception as e:
        print(e)
    print("Not hitting")
  
    return render(request, 'index.html',{'risk': risk})

