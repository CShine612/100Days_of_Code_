import requests
import config
import datetime

pixella_user_params = {"token": config.pixella_token,
                  "username": config.username,
                  "agreeTermsOfService": "yes",
                  "notMinor": "yes"}

# response = requests.post("https://pixe.la/v1/users", json=pixella_user_params)
# print(response.text)

graphs_endpoint = f"https://pixe.la/v1/users/{config.username}/graphs"

graph_config = {"id": "graph1",
                "name": "Python Graph",
                "unit": "hr",
                "type": "float",
                "color": "ajisai"}

headers = {"X-USER-TOKEN": config.pixella_token}

# response = requests.post(graphs_endpoint, json=graph_config, headers=headers)
# print(response.text)

python_graph_endpoint = f"https://pixe.la/v1/users/{config.username}/graphs/{graph_config['id']}"

today = datetime.datetime.now()

data_params = {"date": today.strftime("%Y%m%d"),
               "quantity": "7.5"}

# response = requests.post(python_graph_endpoint, json=data_params, headers=headers)
# print(response.text)

update_endpoint = f"https://pixe.la/v1/users/{config.username}/graphs/{graph_config['id']}/{today.strftime('%Y%m%d')}"

updated_params = {"quantity": "8"}

# response = requests.put(update_endpoint, json=updated_params, headers=headers)

# delete_endpoint = f"https://pixe.la/v1/users/{config.username}/graphs/{graph_config['id']}/{today.strftime('%Y%m%d')}"
#
# response = requests.delete(delete_endpoint, headers=headers)

get_svc_endpoint = f"https://pixe.la/v1/users/{config.username}/graphs/{graph_config['id']}"

response = requests.get(get_svc_endpoint, headers=headers)
print(response.text)
