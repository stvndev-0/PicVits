import pytest
from django.contrib.auth.models import User
 
@pytest.mark.django_db
def test_my_user():
    me = User.objects.create_user(username='admin', password='admin1')
    me.is_superuser = True
    me.save()

    retriever_user = User.objects.get(username='admin')
    assert retriever_user.is_superuser