def default_state():
    state = dict(user_action=[],
                 system_action=[],
                 belief_state={},
                 request_state={},
                 terminated=False,
                 history=[])
    state['belief_state'] = {
            "informable":{

                "food": "",
                "pricerange": "",
                "area": "",
            },
            "request":{
                "food": "",
                "pricerange": "",
                "area": "",
                "address":"",
                "postcode":"",
                "phone":"",
                "name":"",


            }

       
    }
    return state
