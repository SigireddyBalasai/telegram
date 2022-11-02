import os
import json


class env:


    def __init__(self):
        if(os.path.exists("/response.json")):
            print("exists")
        else:
            with open("response.json", "w") as fil:
                ok = json.dumps(
                    {'update':
                        {
                            'update_id': 1234
                        }
                    }
                                )

                json.dump(ok, fil)


env().add_update_id(123456)