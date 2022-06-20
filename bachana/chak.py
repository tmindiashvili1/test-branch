import requests
import json



response = requests.get('https://api.chucknorris.io/jokes/random')

chak_joke = response.json()['value']


def jprint(obj):
    text = json.dumps(obj, sort_keys=True)
    return text

def joke_call():
    return jprint(chak_joke)



# joke_list = []

# def chuk_noris():


#     chak_result = jprint(chak_joke)

#     joke_list.append(chak_result)

#     return joke_list

