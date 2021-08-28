from flask import Flask
from flask import request
from flask import json

app = Flask(__name__)


# -- DO NOT EDIT
# sample end point for HTTP Get
@app.route("/")
def default():
    """
    default endpoint for this server, just for demo.

    :return: str
    """
    return "FIRST PROJECT - we have " + str(len(get_client_rates())) + " clients in total."


# sample data load function
# This is a temporary data file - when we get to know more about database and cloud storage
# we would not be using this kind of data storage.
def get_client_rates():
    """
    return all the client - rate pairs we have.

    :return: dict {id: {'rate':float}}
    """
    import pandas as pd
    df = pd.read_json("client_rate.json")
    return df.to_dict()
# -- DO NOT EDIT END


# -- TODO: Part 1 - add an endpoint to get rate by client id
# When query http://hostname/rate/client1 it would return the rate number for client1 - 0.2
@app.route("/rate/<client_id>")
def get_client_rate(client_id):
    """
    End point for getting rate for a client_id.

    :param client_id: str
    :return: http response
    """
    import pandas as pd
    df = pd.read_json("client_rate.json")
    df_dict = df.to_dict()
    # How to get the actual rate from client_id?
    return df_dict[client_id]
# -- TODO END: Part 1


# -- TODO: Part 4 - add an endpoint to add more client and rates data
@app.route("/rate", methods=['POST'])
def upsert_client_rate():
    """
    End point for updating or inserting client rate values in the post param.

    :return: http response.
    """

    name = request.json
    # We want to update if the client exist in the client_rate.json data
    update_client_rates(name.values().index(0), name[0])
    # Or insert a new client-rate pair into client_rate.json data

    print(request)

    # After getting post request - how to update json file?
    return request.get_json()

def rewrite_json_file(filepath, json_data):
    with open(filepath, 'w') as f:
        json.dump(json_data, f)
    f.close()

def update_client_rates(client_id: str, rate: float):
    """
    update or insert a client_id - rate pair.

    :param client_id: string, e.g. 'client1'
    :param rate: float, e.g. 0.1
    :return:
    """
    import pandas as pd
    df = pd.read_json("client_rate.json")
    df_dict = df.to_dict()
    if client_id in df_dict:
        df_dict[client_id] = rate
        rewrite_json_file("client_rate.json", df_dict)
        return "Client_id Exist Rate Updated"
    else:
        df_dict[client_id] = rate
        rewrite_json_file("client_rate.json", df_dict)
        return "Client_id Not Exist Rate Inserted"
    # check if exist
    # replace or add client rate
    # re-write the file
    pass
# -- TODO END: Part 4


if __name__ == "__main__":
    app.run()
