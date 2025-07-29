import requests

url = "http://localhost:8000/"


# querystring = {"search": "ak"}

# response = requests.get(url, params=querystring)
# datas = response.json()


# for data in datas:
#     for key, value in data.items():
#         print(key, value, type(value))
#
#     print()


def create_category(name):
    url = "http://localhost:8000/"
    response = requests.post(url, data={"name": name})
    data = response.json()
    if response.status_code == 400:
        return f"BAD REQUEST: {data['name'][0]}"
    return data


def search_category(search):
    url = "http://localhost:8000/"
    querystring = {"search": search}

    response = requests.get(url, params=querystring)
    datas = response.json()
    return datas


def category_list():
    url = "http://localhost:8000/"
    response = requests.get(url)
    datas = response.json()
    return datas


def update_category(pk, name, parent=None):
    url = f"http://localhost:8000/{pk}/"

    payload = {"name": name}
    if parent:
        payload = {"name": name,
                   "parent": parent}
    headers = {"content-type": "application/json"}

    response = requests.put(url, json=payload, headers=headers)

    data = response.json()
    return data


# data = create_category("Poyabzallar")
# datas = search_category('ak')
# datas_list = category_list()
# print(data)
# print(datas)
# print(datas_list)

updated_data = update_category(14, "Aksesuarlar")
print(updated_data)
