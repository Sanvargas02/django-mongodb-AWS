
from django.shortcuts import render
from .models import Submission

def home(request):
    message = ""
    saved = None

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        age = int(request.POST.get("age"))
        if age < 18:
            result = "minor"
            message = f"Hi {name}, you are a minor."
        else:
            result = "adult"
            message = f"Hi {name}, you are an adult."

        saved = Submission.objects.create(name=name, age=age, result=result)

    last_five = Submission.objects.order_by("-created_at")[:5]
    total = Submission.objects.count()

    ctx = {"message": message, "saved": saved, "last_five": last_five, "total": total}
    return render(request, "home.html", ctx)
