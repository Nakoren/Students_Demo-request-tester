import requests
import pytest

GET_LIST_URL = 'http://192.168.0.16:8080/students/general/get-student-list'

GetUserGitFalseList = {
    "version": "1.0",
    "filter":{
        "id": 0,
        "personalData": None,
        "fgit": {
            "hasGit": False,
            "git": None
        },
        "fcontact": None
    },
    "pagination":{
        "count":100,
        "number":0,
        "random":False,
        "sort": "lastname",
        "orderDesc":"false"
    }
}

GetUserGitTrueList = {
    "version": "1.0",
    "filter":{
        "id": 0,
        "personalData": None,
        "fgit": {
            "hasGit": True,
            "git": None
        },
        "fcontact": None
    },
    "pagination":{
        "count":100,
        "number":0,
        "random":False,
        "sort": "lastname",
        "orderDesc":"false"
    }
}

def testSortGitTrue():
    response = requests.post(GET_LIST_URL, json=GetUserGitTrueList)

    assert response.status_code == 200

    data = response.json()["info"]

    assert len(data)!=0

    for i in range(1,len(data)):
        assert data[i]["fgit"]["hasGit"] == True


def testSortGitFalse():
    response = requests.post(GET_LIST_URL, json=GetUserGitFalseList)

    assert response.status_code == 200

    data = response.json()["info"]
    assert len(data)!=0

    for i in range(1,len(data)):
        assert data[i]["fgit"]["hasGit"] == False


