from django.shortcuts import render
from django.http import JsonResponse
# from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json


@csrf_exempt
def login_view(request):
    if request.method == "POST":
        data =json.loads(request.body)
        acc_no = data.get("account_number")
        pin = data.get("pin")
        
        try:
            user = User.objects.get(acc_no=acc_no, pin=pin)
            return JsonResponse({"message": "Login successful", "user":{
                "acc_no": user.acc_no,
                "name": user.name,
                "balance": user.balance,
            }})
        except User.DoesNotExist:
            return JsonResponse({"error": "Invalid account number or PIN"}, status=400)

@csrf_exempt
def withdraw_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        acc_no = data.get("account_number")
        amount = data.get("amount")
        
        try:
            user = User.objects.get(acc_no=acc_no)
            if user.balance < amount:
                return JsonResponse({"error": "Insufficient balance"}, status=400)
            user.balance -= amount
            user.save()
            return JsonResponse({ "message": "Withdrawal successful",
                "available_balance": f"₹{user.balance:.2f}",
                "new_balance": float(user.balance)})
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=400)
@csrf_exempt
def deposit_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        acc_no = data.get("account_number")
        amount = data.get("amount")
        
        try:
            user = User.objects.get(acc_no=acc_no)
            user.balance += amount
            user.save()
            return JsonResponse({"message": "Deposit successful","available_balance": f"₹{user.balance:.2f}",
                "new_balance": float(user.balance)})
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=400)

@csrf_exempt
def balance_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        acc_no = data.get("account_number")
        
        try:
            user = User.objects.get(acc_no=acc_no)
            return JsonResponse({"balance": float(user.balance)})
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=400)
def index_view(request):
    return render(request, "atm_app/index.html")
# Create your views here.
