# OPEN API EXAMPLE DOCUMENTATION
FIND_USER_BY_ID_RESPONSE_EXAMPLE = {
    "message": "user found",
    "user": {
        "user_id": "634849b15be3416c39a868ad",
        "provider_id": None,
        "provider": None,
        "name": "Kang",
        "email": "kang@kong.com",
        "description": "Hi, my name is Kang. What's yours?? 🎈",
        "profile_pic": "123",
        "graduation_year": "2045",
        "current_semester": "5"
    }
}

CREATE_USER_BODY_EXAMPLE = {
    "provider_id": None,
    "provider": None,
    "name": "Kang",
    "email": "kang@king.com",
    "profile_pic": "123",
    "graduation_year": "2045",
    "current_semester": "5"
}

CREATE_USER_RESPONSE_EXAMPLE = {
    "message": "user was successfully created",
    "user": {
        "user_id": "63485899454b956526b9aaaf",
        "provider_id": None,
        "provider": None,
        "name": "Kang",
        "email": "kang@king.com",
        "description": "",
        "profile_pic": "123",
        "graduation_year": "2045",
        "current_semester": "5"
    }
}
