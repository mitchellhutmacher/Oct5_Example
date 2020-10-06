import requests

server = "http://127.0.0.1:5000"

r = requests.get(server+"/info") # Puts response into r variable
print(r.status_code)
print(r.text) # Open another terminal window to use this code, need to have server.py running

out_data = {"a": 5, "b": 10}
r = requests.post(server+"/add", json=out_data)
print(r.status_code)
print(r.text)

# Bad request
out_data = {"a": 10, "b": -50}
r = requests.post(server+"/add", json=out_data)
print(r.status_code)
print(r.text)

r = requests.get(server+"/say_hello/Mitchell")
print(r.status_code)
print(r.text)

r = requests.get(server+"/add_numbers/10/15")
print(r.status_code)
print(r.text)
"""
NOTES
* Make sure to remember to activate venv in the second terminal window
* You can see the server window gets the request from this code
* Opening 2 windows in IDE - server and client
* After running server.py, just go to client, right click and run client.py and it'll run both
  - Opens a second tab in PyCharm terminal
"""