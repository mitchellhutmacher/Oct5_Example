from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])  # Decorator - Improves or enhances python function functionality.  Tells python to add
# a route, basic one.  Want it to be a GET request
def server_status():
    return "My server is on"


@app.route("/info", methods=["GET"])
def info():
    info_str = "Here is where I might share usage information. "
    return info_str


@app.route("/add", methods=["POST"])
def add_func():
    """
    dict = {"a": int, "b": int}
    """
    in_data = request.get_json()
    print(type(in_data))
    answer = in_data["a"] + in_data["b"]
    if answer < 0:
        return "No negative numbers", 400
    else:
        return "The answer is {}".format(answer)


@app.route("/say_hello/<name>", methods=["GET"])
def say_hello(name):
    return "Hello, {}".format(name)


@app.route("/add_numbers/<a>/<b>", methods=["GET"])
def add_nums(a, b):
    x = int(a) + int(b)
    return "The answer is {}".format(x)


if __name__ == "__main__":
    app.run()  # Run the server


"""
NOTES
* If you just run this in PyCharm it will give you an address to go to in the thing below
* Can also run in terminal
* URL provided is called the "loopback URL", http://128.0.0.1:5000 IP address will always make computer look at itself
* Click the URL, visit in default browser, cool.  
* Communication programs (Slack, Discord) use local ports
  - Haha Discord this guy is a nerd
* Possible for other users to visit?  If you set your computer up right, yes
  - This address is only running locally, so no
  - We will use VM
* After you make a change, stop and rerun to see those changes in the website
* When terminal is running the code, you don't have a prompt, press CTRL+C to quit
  - Not working when i was typing that in the PyCharm terminal
* Moving to client.py
* POST request - receive information
* PyCharm has built in docstring functionality - neat!
  - If you add parameters to function, PyCharm adds their names to the automatically generated docstring
* Flask has built in request function thingy (NOT requests)
* Add another requests to client to use new add function
* print statements on the server side (like line 24) are for debugging, the client will never see it
* The return statements go to the client
* return "str", error code
  - Line 27
* If you try to return a list, client gets it no problem?
  - Client can not access it as a list because it's really just a string that looks like a list
    - That's what jsonify does
* ALWAYS jsonify result
  - On the client side, can always work if you .json() the answer
* say_hello
  - Variable being provided as an argument must be same variable name in the <>
* My add_numbers is not working, why?  Getting 500 error, internal server error
  - Apparently just need to always return string
"""