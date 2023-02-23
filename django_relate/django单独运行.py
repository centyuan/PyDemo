import os, sys

parent_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(parent_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CcstcAdmin.settings")
import django

django.setup()
if __name__ == '__main__':
    pass
    # from users.models import UserInfo
    # for user in UserInfo.objects.all():
    #     print(user.username)
