from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView
from .forms import SignUpForm, ProfileForm, CustomerForm
from django.contrib.auth.models import User
from .models import Customer
import os
import datetime
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import login
class SignUpView(View):
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # Write to activity log
            log_data = f"New user signed up: {user.username} - {datetime.datetime.now()}\n"
            log_path = os.path.join(os.path.dirname(__file__), 'activity_log.txt')
            
            with open(log_path, 'a') as log_file:
                log_file.write(log_data)

            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('emails/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            messages.success(request, ('Please Confirm your email to complete registration.'))
            return redirect('login')

        return render(request, self.template_name, {'form': form})

class ActivateAccount(View):
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.profile.email_confirmed = True
            user.save()
            login(request, user)
            messages.success(request, ('Your account has been confirmed.'))
            return redirect('home')
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return redirect('home')


# Edit Profile View
@method_decorator(login_required, name='dispatch')
class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'registration/profile.html'

@method_decorator(login_required, name='dispatch')
class AddcustomerView(View):
    def get(self, request):
        form = CustomerForm()
        return render(request, 'registration/addcustomer.html', {'form':form})

    def post(self, request):
        form = CustomerForm(request.POST)
        user = request.user
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            city = form.cleaned_data['city']
            address = form.cleaned_data['address']
            locality = form.cleaned_data['locality']
            phone_no = form.cleaned_data['phone_no']
            house_no = form.cleaned_data['house_no']
            zip_code = form.cleaned_data['zip_code']
            cus = Customer(user=user, full_name=full_name, city=city, address=address, locality=locality, phone_no=phone_no, house_no=house_no, zip_code=zip_code)
            cus.save()
            messages.success(request, 'Address/Customer added successfully!!')
            return redirect('customers')
        return render(request, 'registration/addcustomer.html', {'form':form})

@method_decorator(login_required, name='dispatch')    
class CustomerView(View):
    def get(self, request):
        customers = Customer.objects.filter(user=self.request.user)
        return render(request, 'registration/customers.html', {'customers':customers})

def deleteaddress(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    messages.success(request, "Your address has been deleted successfully!!")
    return redirect('customers')

def user(request):
    return request.user.id