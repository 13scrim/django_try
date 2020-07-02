from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccesRecord,webpage,Topic
from first_app import forms
from django.views.generic import TemplateView
def index(request):
    webpage_list = webpage.objects.order_by('name')
    records = AccesRecord.objects.order_by('name')
    date_dict = {'webpages':webpage_list,'record':records}
    return render(request,'index.html',context=date_dict)

def call (request):
    form = forms.NewForm()
    form2 = forms.Newform2()
    if request.method == "POST":
        form = forms.NewForm(request.POST)
        form2 = forms.Newform2(request.POST)
        if form2.is_valid() and form.is_valid():
            form1 = form.save(commit=True)
            form22 = form2.save(commit=False)
            form22.name = form1
            form2.save()
            return index(request)
        else :
            print("Error")
    return render(request,'basic.html',context={'form':form,'form2':form2})




#  class DashBoard(TemplateView):
#    template_name = "basic.html"
#    def call (request):
#        form = forms.NewForm()
#        my_dic  = {'form':form }

#        return render(request,'basic.html',context=my_dic)

#    def done(request):
#        form2 = forms.Newform2()
#        my_dic2 = {'form2':form2}
#        return render(request,"basic.html",context= my_dic2)
