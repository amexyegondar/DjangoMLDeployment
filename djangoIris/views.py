from django.shortcuts import render
from joblib import load 
model=load('./savedmodel/iris.joblib')
def prediction(request):
    return render(request,'main.html')
           
def formInfo(request):
      sepal_length=request.GET['sepal_length']
      sepal_width=request.GET['sepal_width']
      petal_length=request.GET['petal_length']
      petal_width=request.GET['petal_width']
      y_pred=model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
      print(y_pred)
      return render(request, 'main.html')