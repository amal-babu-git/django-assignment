from django.shortcuts import render
from django.db import transaction
# Create your views here.
from .models import MyModel, SignalModel

def create_instance(request):
    # This will trigger the post_save signal
    MyModel.objects.create(name="Test Signal")
    return render(request, 'myapp/index.html')


def create_instance_for_question_3(request):
    try:
        with transaction.atomic():
            MyModel.objects.create(name="Test Model")
            # Manually raise an exception to force a rollback
            raise Exception("Simulating an error")
    except Exception as e:
        print(f"Error occurred: {e}")

    # Check if any records exist in SignalModel after the rollback
    signal_records = SignalModel.objects.all()
    print(f"SignalModel record count: {signal_records.count()}")
    return render(request, 'myapp/index.html')