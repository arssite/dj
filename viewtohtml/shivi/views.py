from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
def shivi(request):
    tablelist=[
        {'name':'ka','age':12},
        {'name':'ko','age':10},
        {'name':'ku','age':22},
        {'name':'ki','age':23}
    ]
    #for i in tablelist:
        #print(i)
    content="using context attribute in views while rendring index html template .............................................................................................................................................................................................................................................................................................kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
    return render(request,"index.html",context={"keys":tablelist,"text":content})
    #https://docs.djangoproject.com/en/5.0/ref/templates/builtins/
