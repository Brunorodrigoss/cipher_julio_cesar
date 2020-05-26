import requests

PARAMS = {'token': '4f83b0acf61e8987cfb69913271c846bbc6a5276'}


def get_request():
    URL = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data'
    req = requests.get(url=URL, params=PARAMS)
    return req


def post_request():
    URL = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution'
    answer = {'answer': open('answer.json', 'rb')}
    submit = requests.post(url=URL, params=PARAMS, files=answer)

    print(submit.headers)