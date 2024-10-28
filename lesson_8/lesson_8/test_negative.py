import requests
import pytest

token = 'rDRKVYyvJnBA3-mIifb1JZYAN6NbkRlr6pSH3ZSImm4ODBmwqdFsCozu3M6vgxqP'
headers = {
"Authorization": f"Bearer {token}",
"Content-Type": "application/json"
}

def test_get_project_by_id():
    project_id = 'acafc9d2-25bc-4921-a69c-23f13ce1a45'
    url = f'https://ru.yougile.com/api-v2/projects/{project_id}'
    response = requests.get(url, headers=headers)

    assert response.status_code == 404
    