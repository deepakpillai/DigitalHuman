import requests

def call_api(url, request_type, data = None):
    # url = 'http://localhost:8011/A2F/USD/Load'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    # data = {
    #     'file_name': 'D:/Omniverse/ov/pkg/audio2face-2023.1.1/exts/omni.audio2face.wizard/assets/demo_fullface_mark.usda'
    # }
    response = ""
    if data is None:
        if request_type == "post":
            response = requests.post(url, headers=headers)
        else:
            response = requests.get(url, headers=headers)
    else:
        if request_type == "post":
            response = requests.post(url, headers=headers, json=data)
        else:
            response = requests.get(url, headers=headers, json=data)
    
    print(url, response.status_code)
    print(url, response.json())
    return response.json()