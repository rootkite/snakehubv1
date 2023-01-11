from django.shortcuts import render
from main.forms import NewsLetterUserForm
from main.models import NewsLetterUser
# Create your views here.
def index(request):
    return render(request, 'main/index.html')



def registernl(request):
    form = NewsLetterUserForm()
    if request.method == 'POST':
        form = NewsLetterUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'main/index.html')
        else:
            print('Error : Form invalid')
    return render(request, 'main/registernl.html',{'form':form})

         
        


    



def login_user(request):
    pass


def newsletter_users(request):
    users_list = NewsLetterUser.objects.order_by('name')
    return render(request, 'main/users.html',{'userdict':users_list})


def about(request):
    return render(request, 'main/about.html')


   