from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *



class WorkTest(APITestCase):

    def setUp(self) -> None:
        team = Team.objects.create(name='cho-peace-busters')
        genre = Genre.objects.create(
            title='Animation',
            bg_color='#FFDD33'
        )
        work = Work.objects.create(
            title='anohana',
            description='Super nakeru Animation',
            team=team,
            genre=genre
        )
    
    def test_get_work(self):
        res = self.client.get('/api/v1/works/', format='json')       
        assert res.status_code == 200
        datas = res.json()
        assert type(datas) == list and len(datas) == 1
        data = datas[0]
        assert data['title'] == 'anohana'
        assert data['team']['name'] == 'cho-peace-busters'
        assert data['genre']['title'] == 'Animation'
    
    def test_create_comment(self):
        res = self.client.post('/api/v1/works/1/comments/', {
            'name': 'anal',
            'text': 'www'
        }, format='json')
        assert res.status_code == 201
        data = res.json()

        res = self.client.get('/api/v1/works/1/', format='json')       
        assert res.status_code == 200
        data = res.json()
        assert len(data['comments']) == 1
        comment = data['comments'][0]
        assert comment['name'] == 'anal'
        assert comment['text'] == 'www'
    
    def test_increment_goods(self):
        res = self.client.post('/api/v1/works/1/goods/', None, format='json')
        assert res.status_code == 201
        data = res.json()

        assert data['goods'] == 1

        res = self.client.post('/api/v1/works/1/goods/', None, format='json')
        assert res.status_code == 201
        data = res.json()

        assert data['goods'] == 2