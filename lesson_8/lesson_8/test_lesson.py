import requests
import pytest

token = 'rDRKVYyvJnBA3-mIifb1JZYAN6NbkRlr6pSH3ZSImm4ODBmwqdFsCozu3M6vgxqP'
headers = {
"Authorization": f"Bearer {token}",
"Content-Type": "application/json"
}

def test_get_progects():
    url = 'https://ru.yougile.com/api-v2/projects'
    response = requests.get(url, headers=headers)


    assert response.status_code == 200
    assert 'content' in response.json()

def test_create_project():
    url = "https://ru.yougile.com/api-v2/projects" 
    data = {
        'title' : 'project_test'  
    }
    response = requests.post(url, json=data, headers=headers)

    assert response.status_code == 201
    assert 'id' in response.json()

def test_update_project():
    project_id = 'acafc9d2-25bc-4921-a69c-23f13ce1a495'
    url = f'https://ru.yougile.com/api-v2/projects/{project_id}'
    data = {
        'title' : 'Updated Project Name'
    }
    response = requests.put(url, json=data, headers=headers)

    assert response.status_code == 200    




def test_get_project_by_id():
    project_id = 'acafc9d2-25bc-4921-a69c-23f13ce1a495'
    url = f'https://ru.yougile.com/api-v2/projects/{project_id}'
    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    assert 'title' in response.json()
