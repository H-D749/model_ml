from django.shortcuts import render
from django.http import HttpResponse
from joblib import load
import os

# Construct the absolute path to the model file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'savedmodel', 'model.joblib')
model = load(model_path)

def home(request):
    y_pred = None
    if request.method == 'POST':
        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))

        y_pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        if y_pred[0] == 0:
            y_pred = "setosa"
        elif y_pred [0]== 1:
            y_pred = "versicolor"
        else:
            y_pred = "virginica"

        return render(request, 'myapp/home.html', {'result': y_pred})
    


    print(y_pred)
    return render(request, "myapp/home.html")

    
