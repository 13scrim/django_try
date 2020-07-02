from django.shortcuts import render
from five_app.forms import UserForm, UserProfilInfo
from django.urls import reverse
from five_app.models import Userprofil
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def index(request):
    context = {"index":"IndexPage"}
    return render(request,"index.html",context=context)

def register(request):
    # variable registred permet de codé dans l'html si Vrai on affiche des element et si false on affiche d'autre
    registred = False

    if request.method == "POST":
        # request.method = POst veut dire qu'on clique sur un bouton submit
        user_form = UserForm(data=request.POST) # on crée une instance de la class UserForm ( crée dans le fichier forms.py )
        profile = UserProfilInfo(request.POST) # pareil pour profil
        if user_form.is_valid() and profile.is_valid(): # on vérifie si les entrée sont valide
            user = user_form.save()  # on sauvegarde les entrée (dans ce cas on enregistre email, nom ect )
            user.set_password(user.password) # on Hash le password
            user.save() # on save les modification
            profile1 = profile.save(commit=False) # On prends les entrée mais on les enregistre pas dans la base de donnée
            profile1.user = user # on modifie les entrées dans ce cas on donne les mêmes valeurs de user a profil pour pas avoir de
            # probléme

            if 'profil_pic' in request.FILES:
                # profil_pic représente le variable choisi dans la classe modele
                # si il y'a une photo deprofil alors
                profile1.profil_pic = request.FILE['profil_pic']
                # la champ profil_pic de la base profile1 reçois l'image entrée
            profile1.save()
                # on sauvegarde les champs modifié
            registred= True
            # on passe registred on vrai pour afficher un message
        else :
            # Si les champs sont pas valide on affiches les erreurs
            print(user_form.errors, profile.errors)
    else :
        # si le bouton submit n'est pas cliqué bah on afficher le formulaire
        user_form = UserForm()
        profile = UserProfilInfo()

    return render(request,"inscription.html",context={"user_form":user_form,"profile_form":profile,"registred":registred} )




def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user =authenticate(username =username ,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse("index"))
            else :
                return HttpResponse ("ACCOUNT NOT ACTIVE")
        else :
            print ("FAIled connection")
            print(username,password)

            return HttpResponse("Invalid login")
    else :
        return render(request,"login.html",{})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    name  =  request.user.profile_name
    password = "welcome"
    return render(request,"index.html",context={"name":name,"password":password})
