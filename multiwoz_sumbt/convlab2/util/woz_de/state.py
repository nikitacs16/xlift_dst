def default_state():
    state = dict(user_action=[],
                 system_action=[],
                 belief_state={},
                 request_state={},
                 terminated=False,
                 history=[])
    state['belief_state'] = {
            "informable":{

                "essen": "",
                "preisklasse": "",
                "gegend": "",
            },
            "request":{
                "essen": "",
                "preisklasse": "",
                "gegend": "",
                "adresse":"",
                "postleitzahl":"",
                "telefon":"",
                "name":"",


            }

       
    }
    return state
