# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from .forms import LoginForm, VisitForm
from .models import Record
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from sendsms import api


# Create your views here.
def home(request):
    if request.method == "GET":
        form = LoginForm()
        if request.session.get('display_alert', False) == True:
            request.session["display_alert"] = False
            return render(request,"records/home.html", {"form":form, "display_alert": True})
        else:
            return render(request,"records/home.html", {"form":form, "display_alert" : False})
    else:
        form = LoginForm(request.POST)
        
        if "enter" in request.POST:
        
            if form.is_valid():
                print(form.cleaned_data["phone_number"])
                phone_number = form.cleaned_data["phone_number"]
                request.session["phone_number"] = phone_number
                total_visits = Record.objects.filter(visitor_number=phone_number).order_by("-check_in")
                print("done")
                print(total_visits)
                print("done2")
                if total_visits.count() is not 0:
                    record = total_visits[0]
                    print("entered")
                    if record.checked_in is True:
                        #show alert
                        request.session["display_alert"] = True
                        return redirect(reverse("records:home"))
                    else:
                        return redirect("record/")
                else:
                    print("entered 123")
                    return redirect("record/")
        else:

            if form.is_valid():
                phone_number = form.cleaned_data["phone_number"]
                request.session["phone_number"] = phone_number
                try:
                    records = Record.objects.filter(visitor_number=phone_number).order_by("-check_in")
                    if records[0].checked_in is True:
                        return redirect("checkout/")
                    else:
                        print("entered record")
                        return redirect("record/")
                except:
                    return redirect("record/")
            else:
                return redirect("home/")
            return redirect("checkout/")

def visit(request):
    if request.method == "GET":
        phone_number = request.session["phone_number"] or None
        if(request.session["phone_number"] == None):
            return redirect(reverse("records:home"))
        records = Record.objects.filter(visitor_number=phone_number).order_by("-check_in")
        visitor_name = None
        visitor_email = None
        if records.count() is not 0:
            record = records[0]
            visitor_name = record.visitor
            visitor_email = record.visitor_email
        context = {"visitor_number" : request.session["phone_number"],
                    "visitor_name" : visitor_name,
                    "visitor_email": visitor_email}
        form = VisitForm(initial=context)
        return render(request, "records/visit.html", {"form":form})
    else:
        form = VisitForm(request.POST)
        if form.is_valid():
            record = Record.objects.create(
                visitor = form.cleaned_data["visitor_name"],
                visitor_email = form.cleaned_data["visitor_email"],
                visitor_number = form.cleaned_data["visitor_number"],
                host = form.cleaned_data["host_name"],
                host_email = form.cleaned_data["host_email"],
                host_number = form.cleaned_data["host_number"],
            )
            record.checked_in = True
            record.save()
            # email = EmailMessage('Hello', 'World', to=['divy97@gmail.com'])
            # email.send()
            
            x = email(request,record)  
            #y = sms(request,record)
            #yaha pe check in karte waqt jo mail aur sms bhejna hai uska code aa jaiga
        return redirect(reverse("records:home"))

def check_out(request):
    if request.method == "GET":
        phone_number = request.session["phone_number"] or None
        if phone_number is None:
            return redirect(reverse("records:home"))
        else:
            record = Record.objects.filter(visitor_number=request.session["phone_number"]).order_by("-check_in")[0]
            return render(request, "records/checkout.html", {
                "record": record
            })
    else:
        phone_number = request.session["phone_number"]
        record = Record.objects.filter(visitor_number=phone_number).order_by("-check_in")[0]
        record.check_out()
        
        checkout_email(request,record)

        # yaha pe checkout wala pe sms aur email bhejne wala code aa jaiga
        return redirect(reverse("records:home"))
    return render(request, "records/home.html")

def email(request,record):
    subject = 'Check in Alert'
    message = 'A guest has checked in'+ '\n\nVisitor Name: ' + record.visitor + "\nPhone Number: " + record.visitor_number + "\nE-Mail: " + record.visitor_email
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [record.host_email,"17UCS126@lnmiit.ac.in"]
    send_mail( subject, message, email_from, recipient_list )
    return "nice"

def checkout_email(request,record):
    subject = 'Check out Alert'
    message = 'Check out successful'+ '\n\nVisitor Name: ' + record.visitor + "\nPhone Number: " + record.visitor_number + "\nCheck-in time: " + record.get_checkin_time() + "\nCheck-out time: " + record.get_checkout_time() + "\nHost name: " + record.host + "\nAddress Visited: " + record.host_email
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [record.visitor_email,"17UCS126@lnmiit.ac.in"]
    send_mail( subject, message, email_from, recipient_list )
    return "nice"

def sms(request,record):
    message = 'A guest has checked in'+ '\n\nVisitor Name: ' + record.visitor + "\nPhone Number: " + record.visitor_number + "\nE-Mail: " + record.visitor_email
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    client.messages.create(from_=settings.TWILIO_PHONE_NUMBER,
                    to="+91"+record.host_number,
                    body=message)
    return "nice"