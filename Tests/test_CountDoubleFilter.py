import requests
import pytest

GET_COUNT_URL = 'http://192.168.0.16:8080/students/general/get-student-count'

def GetUserDoubleFilterCount(gitFilter, contactFilter):
    return {
    "version": "1.0",
    "filter": {
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
    }
}

def TestSortDoubleFilterCount():
    for git in [True, False]:
        for contact in [True, False]:

            sendData = GetUserDoubleFilterCount(git, contact)
            response = requests.post(GET_COUNT_URL, json=sendData)

            assert response.status_code != 200 or response.json()["resultData"] == None
