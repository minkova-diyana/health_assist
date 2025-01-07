import os
from datetime import datetime

from health_assist.accounts.models import EmployeeProfile


def user_directory_path(instance, filename):
    user = instance.user
    profile = EmployeeProfile.objects.get(user=user)
    company_name = profile.company
    user_name = f'{profile.first_name}_{profile.last_name}'
    date = datetime.now().strftime("%Y_%m_%d_%H")
    return f"reimbursement_files/{company_name}/{user_name}/{date}/{filename}"
