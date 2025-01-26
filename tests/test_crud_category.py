import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from test_site.apps.test_app.models import Category


@pytest.mark.django_db
def test_create_category():
    client = APIClient()
    url = reverse('category-list')
    data = {'name': 'Test Category 1'}
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Category.objects.count() == 1
    assert Category.objects.get().name == 'Test Category 1'


@pytest.mark.django_db
def test_list_category():
    client = APIClient()
    url = reverse('category-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == Category.objects.count()


@pytest.mark.django_db
def test_retrieve_category():
    category = Category.objects.create(name='Test Category 2')
    client = APIClient()
    url = reverse('category-detail', args=[category.id])
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == 'Test Category 2'


@pytest.mark.django_db
def test_update_category():
    category = Category.objects.create(name='Test Category 3')
    client = APIClient()
    url = reverse('category-detail', args=[category.id])
    data = {'name': 'New Category Name'}
    response = client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert Category.objects.get().name == 'New Category Name'


@pytest.mark.django_db
def test_delete_category():
    category = Category.objects.create(name='Test Category 4')
    client = APIClient()
    url = reverse('category-detail', args=[category.id])
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Category.objects.count() == 0
