import requests
import pytest

GET_COUNT_URL = 'http://192.168.0.16:8080/students/general/get-student-count'

GetUserContactFalseCount = {
    "version": "1.0",
    "filter": {
        "id": 0,
        "personalData": None,
        "fgit": None,
        "fcontact": {
            "hasContact": False,
            "femail": None,
            "ftelegram": None,
            "fphone": None
        }
    }
}

GetUserContactTrueCount = {
    "version": "1.0",
    "filter": {
        "id": 0,
        "personalData": None,
        "fgit": None,
        "fcontact": {
            "hasContact": True,
            "femail": None,
            "ftelegram": None,
            "fphone": None
        }
    }
}

def testSortContactTrueCount():
    log_text = "Test 7\ngetting records count with contact:\n"
    response = requests.post(GET_COUNT_URL, json=GetUserContactTrueCount)
    log_text += f"ResponseCode: {response.status_code}\n"

    assert response.status_code!=200 or response.json()["resultData"] != None

def testSortContactFalseCount():
    log_text = "Test 8\ngetting records count with no contact:\n"
    response = requests.post(GET_COUNT_URL, json=GetUserContactFalseCount)
    log_text += f"ResponseCode: {response.status_code}\n"

    assert response.status_code != 200 or response.json()["resultData"] != None
