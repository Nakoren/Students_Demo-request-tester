import requests
import pytest

GET_LIST_URL = 'http://192.168.0.16:8080/students/general/get-student-list'

GetUserContactFalseList = {
    "version": "1.0",
    "filter":{
        "id": 0,
        "personalData": None,
        "fgit": None,
        "fcontact": {
            "hasContact": False,
            "femail": None,
            "ftelegram": None,
            "fphone": None
        }
    },
    "pagination":{
        "count":100,
        "number":0,
        "random":False,
        "sort": "lastname",
        "orderDesc":"false"
    }
}

GetUserContactTrueList = {
    "version": "1.0",
    "filter":{
        "id": 0,
        "personalData": None,
        "fgit": None,
        "fcontact": {
            "hasContact": True,
            "femail": None,
            "ftelegram": None,
            "fphone": None
        }
    },
    "pagination":{
        "count":100,
        "number":0,
        "random":False,
        "sort": "lastname",
        "orderDesc":"false"
    }
}

def TestSortContactTrue():
    response = requests.post(GET_LIST_URL, json=GetUserContactTrueList)

    assert response.status_code == 200

    data = response.json()["info"]
    assert data!=0

    for i in range(1,len(data)):
        assert [i]["fcontact"]["hasContact"] == True

def TestSortContactFalse():
    response = requests.post(GET_LIST_URL, json=GetUserContactFalseList)

    assert response.status_code == 200

    data = response.json()["info"]
    assert len(data) != 0

    for i in range(1,len(data)):
        assert data[i]["fcontact"]["hasContact"] == False

