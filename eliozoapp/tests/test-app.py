from eliozoapp import Flask # Flask instance of the API

def test_index_route():
    response = Flask.test_client().get('/')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Testing, Flask!'