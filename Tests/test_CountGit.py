import requests
import pytest

GET_COUNT_URL = 'http://192.168.0.16:8080/students/general/get-student-count'

GetUserGitFalseCount = {
    "version": "1.0",
    "filter": {
        "id": 0,
        "personalData": None,
        "fgit": {
            "hasGit": False,
            "git": None
        },
        "fcontact": None
    }
}

GetUserGitTrueCount = {
    "version": "1.0",
    "filter": {
        "id": 0,
        "personalData": None,
        "fgit": {
            "hasGit": True,
            "git": None
        },
        "fcontact": None
    }
}

def testSortGitTrueCount():
    response = requests.post(GET_COUNT_URL, json=GetUserGitTrueCount)

    assert response.status_code == 200 or response.json()["resultData"] != None

def testSortGitFalseCount():
    response = requests.post(GET_COUNT_URL, json=GetUserGitFalseCount)

    assert response.status_code == 200 or response.json()["resultData"] != None