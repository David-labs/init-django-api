from .models import *
import time
import ipaddress
import random

def create_user(uuid,email,pwd,membership,membership_date):
    new_user = User(
        uuid=uuid,
        email=email,
        password=pwd,
        membership=membership,
        membership_date=membership_date,
        create_at=int(time.time() * 1000)
    )
    new_user.save()
    return True
