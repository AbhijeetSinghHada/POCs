constella_response = {
    "status": 200,
    "description": "OK",
    "data": {
        "results": [
            {
                "type": "stolenid breach",
                "information": {
                    "city": "summerset",
                    "country": "barbados",
                    "nid": "45383702",
                    "ssn": "152684148",
                    "company": "viocular",
                    "credit_card": "5063603575300913",
                    "passport": "10249423",
                    "telephone": "9915762398",
                    "state": "federated states of micronesia",
                    "domain": "viocular.com",
                    "credit_card_10": "5063600913",
                    "zip": "28547",
                    "email": "valencia.phillips@viocular.com",
                    "uid": "3034303030303030353937613131306261623065396464663365623436333962",
                    "date": "2013-04-25 01:42:01",
                    "password": 0,
                    "mother_name": "ellen",
                    "address": "mckenzie aguirre flora leblanc street",
                    "name": "valencia phillips anthony"
                },
                "source": {
                    "description": "The site breach test p2p has been reported to possibly have suffered a data exposure that could include emails and passwords. The possible exposure would have happened in April 2017 although it was reported in April 2017",
                    "name": "breach test p2p",
                    "source": "darkweb",
                    "recommendations": "Update your password to the account associated to the exposure immediately and review any other services where you use the same or similar password as soon as possible. Be alert for suspicious activity related to your identity.",
                    "key": "a11111111111111111111114",
                    "type": "breach"
                },
                "validated": 100,
                "scores": {
                    "Breach Record Exposure Score": {
                        "value": "High"
                    }
                }
            },
            {
                "type": "stolenid breach",
                "information": {
                    "city": "summerset",
                    "password": 1,
                    "country": "barbados",
                    "nid": "45383702",
                    "ssn": "152684148",
                    "company": "viocular",
                    "credit_card": "5063603575300910",
                    "username": "valencia.phillips",
                    "name": "valencia phillips anthony",
                    "passport": "10249423",
                    "telephone": "9915762398",
                    "mother_name": "ellen",
                    "state": "federated states of micronesia",
                    "domain": "viocular.com",
                    "credit_card_10": "5063600910",
                    "cvv": "1",
                    "zip": "28547",
                    "email": "valencia.phillips@viocular.com",
                    "address": "mckenzie aguirre flora leblanc street",
                    "uid": "3034303030303030653133326333313064353339353661613131323933616131",
                    "date": "2023-11-10 07:21:35",
                    "password_info": {
                        "password_last_chars": "*****1",
                        "password_is_encrypted": 0,
                        "password_clear": 1
                    }
                },
                "source": {
                    "description": "Your personal information (which could include bank accounts, emails, driver licenses and more information), was identified in a data exposure associated with breach_direct_new. The data was located on the Dark Web in December 2020.",
                    "type": "breach",
                    "name": "breach_direct_new",
                    "source": "darkweb",
                    "key": "654df1f9545a6e31f7000436",
                    "recommendations": "Update your password to the account associated to the exposure immediately and review any other services where you use the same or similar password as soon as possible. Be alert for suspicious activity related to your identity."
                },
                "validated": 100,
                "scores": {
                    "Breach Record Exposure Score": {
                        "value": "High"
                    }
                }
            }
        ],
        "query": {
            "pagination": {
                "total": 2,
                "count": 2,
                "page": 0
            }
        },
        "next_id": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIiLCJhdWQiOiIiLCJpYXQiOjE0NDg2MTUyMzUsIm5iZiI6MTQ0ODYxNTIzNSwiZGF0YSI6eyJwYWdpbmF0aW9uUGFyYW1ldGVycyI6eyJzdG9sZW5pZFwvYnJlYWNoXC9zZWFyY2giOnsiZnJvbV9wYWdlIjowLCJmcm9tX2lkIjowLCJmcm9tX29mZnNldCI6Mn19fX0.TDg32p04wMUViI7IvS7vG_X3fInTXaC1jIWKUg_QDig"
    }
}


threat_lab_response = {
    "EmailAlias": "udbhavmani20",
    "EmailDomain": "gmail.com",
    "PasswordCount": 0,
    "Passwords": [],
    "Breaches": [
        {
            "name": "Canva",
            "title": "Canva",
            "domain": "https://canva.com",
            "breach_date": "2019-05-24T00:00:00.000Z",
            "disclosure_date": "2019-06-01T00:00:00.000Z",
            "added_date": "2020-02-21T00:00:00.000Z",
            "modified_date": "2020-02-21T00:00:00.000Z",
            "record_count": 137272116,
            "description": "Attackers breached graphic design tool website Canva in May 2019, stealing over 137 million records including names, email addresses and passwords.",
            "logo_path": "https://darkwebscan-images.s3-us-west-1.amazonaws.com/canva.png",
            "data_classes": [
                "Usernames",
                "Email addresses",
                "Geographic locations",
                "Names",
                "Passwords"
            ],
            "is_verified": 1,
            "is_sensitive": 0,
            "is_retired": 0,
            "is_spam": 0,
            "is_collection": 0,
            "is_enabled": 1
        }
    ]
}


mapping = {
    "EmailAlias": "Email from event body",
    "EmailDomain": "Email from event body",
    "PasswordCount": "Not Found", # Missing, Can use count of password_info fields in all dicts
    "Passwords": "password_last_chars",
    "Breaches": [
        {
            "name": "source.breach",
            "title": "source.breach",
            "domain": "https://canva.com", # Missing Field
            "breach_date": "information.date",
            "disclosure_date": "2019-06-01T00:00:00.000Z", # Missing Field
            "added_date": "2020-02-21T00:00:00.000Z", # Missing Field
            "modified_date": "2020-02-21T00:00:00.000Z", # Missing Field
            "record_count": 137272116, # Missing Field
            "description": "source.description",
            "logo_path": "https://darkwebscan.png", # Missing Field
            "data_classes": [
                "Usernames",
                "Email addresses",
                "Geographic locations",
                "Names",
                "Passwords"
            ], # Present can extract keys.
            "is_verified": "validated", 
            "is_sensitive": 0, # can be taken from "scores"."Breach Record Exposure Score".value
            "is_retired": 0, # Missing Field
            "is_spam": 0, # Missing Field
            "is_collection": 0, # Missing Field
            "is_enabled": 1 # Missing Field
        }
    ]
}