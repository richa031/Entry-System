# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from .forms import LoginForm, VisitForm
from .models import Record
# Create your views here.
def home(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request,"records/home.html", {"form":form})
    else:
        form = LoginForm(request.POST)
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
                if record.check_out is None:

                    return redirect("checkout/")
                else:
                    return redirect("record/")
            else:
                print("entered 123")
                return redirect("record/")

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
            record.save()
            #yaha pe check in karte waqt jo mail aur sms bhejna hai uska code aa jaiga
            return redirect(reverse("records:checkout"))

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
        record.checkout_visitor()
        # yaha pe checkout wala pe sms aur email bhejne wala code aa jaiga
        return redirect(reverse("records:home"))
    return render(request, "records/home.html")
