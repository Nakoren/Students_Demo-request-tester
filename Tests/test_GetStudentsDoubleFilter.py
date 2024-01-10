import requests
import pytest

GET_LIST_URL = 'http://192.168.0.16:8080/students/general/get-student-list'

def GetUserDoubleFilterList(gitFilter, contactFilter):
    return {"version": "1.0",
    "filter":{
        "id": 0,
        "personalData": None,
        "fgit": {
            "hasGit": gitFilter,
            "git": None
        },
        "fcontact": {
            "hasContact": contactFilter,
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

def TestSortDoubleFilterList():
    testCounter = 9
    for git in [True,False]:
        for contact in [True,False]:
            t1 = 'no ' * (not git)
            t2 = 'no ' * (not contact)
            sendData = GetUserDoubleFilterList(git,contact)
            response = requests.post(GET_LIST_URL, json=sendData)

            assert response.status_code != 200
            assert len(data) == 0

            data = response.json()["info"]

            for i in range(1, len(data)):
                    assert (data[i]["fcontact"]["hasContact"] == contact) or (data[i]["fgit"]["hasGit"] == git)
