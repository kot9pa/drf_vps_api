import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from test_site.apps.test_app.models import Operation


@pytest.mark.django_db
def test_create_operation():
    client = APIClient()
    url = reverse('operation-list')
    data = {'name': 'Test Operation 1', 'cost': 100}
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Operation.objects.count() == 1
    assert Operation.objects.get().name == 'Test Operation 1'
    assert Operation.objects.get().cost == 100


@pytest.mark.django_db
def test_list_operation():
    client = APIClient()
    url = reverse('operation-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == Operation.objects.count()


@pytest.mark.django_db
def test_retrieve_operation():
    operation = Operation.objects.create(name='Test Operation 2', cost=200)
    client = APIClient()
    url = reverse('operation-detail', args=[operation.id])
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == 'Test Operation 2'
    assert response.data['cost'] == 200


@pytest.mark.django_db
def test_update_operation():
    operation = Operation.objects.create(name='Test Operation 3', cost=300)
    client = APIClient()
    url = reverse('operation-detail', args=[operation.id])
    data = {'name': 'New Operation Name', 'cost': 333}
    response = client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert Operation.objects.get().name == 'New Operation Name'
    assert Operation.objects.get().cost == 333


@pytest.mark.django_db
def test_delete_operation():
    operation = Operation.objects.create(name='Test Operation 4', cost=400)
    client = APIClient()
    url = reverse('operation-detail', args=[operation.id])
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Operation.objects.count() == 0
