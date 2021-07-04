from django.shortcuts import render, redirect
#form to create users
# from django.contrib.auth.forms import UserCreationForm
#messages display
from django.contrib import messages
#our own created form and user update form
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
#to make profile page login restricted
from django.contrib.auth.decorators import login_required

# Create your views here.
#get request means display blank form , post request menas save data
def register(request):
    if request.method=='POST':
        # form=UserCreationForm(request.POST)
        form=UserRegisterForm(request.POST)

        if form.is_valid():
            # saving user
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}! You are now able to Login')
            return redirect('login')
    else:
        # form=UserCreationForm()
        form=UserRegisterForm()

    return render(request,'users/register.html',{'form':form})

# login required to access this
@login_required
def profile(request):
    # profile update(model form means they expect filled data of current instance)
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your Account has been updated')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_form':u_form,
        'p_form':p_form
        }

    return render(request,'users/profile.html',context)


# message.info
# messages.success
# messages.warning
# messages.debug