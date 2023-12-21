import json
import requests

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


log = open("Test_log.txt",'w')

GET_COUNT_URL = 'http://192.168.0.16:8080/students/general/get-student-count'
GET_LIST_URL = 'http://192.168.0.16:8080/students/general/get-student-list'

#Тесты 1-8 прописаны вручную
#Тесты 9-16 и JSON файлы для POST-запроса генерируются итерационно

#Тесты отвечающие за проверку получения корректного списка
def TestSortGitTrue():
    log_text = "Test 1\ngetting records with git:\n"
    response = requests.post(GET_LIST_URL, json=GetUserGitTrueList)
    log_text += f"ResponseCode: {response.status_code}\n"

    if(response.status_code!=200):
        log_text += "Status: Failed\n\n"
    else:
        data = response.json()["info"]
        if(len(data)==0):
            testFlag = False
        else:
            for i in range(1,len(data)):
                if(data[i]["fgit"]["hasGit"] == False):
                    testFlag = False
                    break

        if (testFlag):
            log_text+= "Status: Success\n\n"
        else:
            log_text+= "Status: Failed\n\n"
    log.write(log_text)

def TestSortGitFalse():
    log_text = "Test 2\ngetting records with no git:\n"
    response = requests.post(GET_LIST_URL, json=GetUserGitFalseList)
    log_text += f"ResponseCode: {response.status_code}\n"

    if(response.status_code!=200):
        log_text += "Status: Failed"
    else:
        data = response.json()["info"]
        testFlag=True
        if(len(data)==0):
            testFlag = False
        else:
            for i in range(1,len(data)):
                if(data[i]["fgit"]["hasGit"] == True):
                    testFlag = False
                    break

        if (testFlag):
            log_text+= "Status: Success\n\n"
        else:
            log_text+= "Status: Failed\n\n"
    log.write(log_text)

def TestSortContactTrue():
    log_text = "Test 3\ngetting records with contact:\n"
    response = requests.post(GET_LIST_URL, json=GetUserContactTrueList)
    log_text += f"ResponseCode: {response.status_code}\n"

    if(response.status_code!=200):
        log_text += "Status: Failed\n\n"
    else:
        data = response.json()["info"]
        testFlag=True
        if(len(data)==0):
            testFlag = False
        else:
            for i in range(1,len(data)):
                if(data[i]["fcontact"]["hasContact"] == False):
                    testFlag = False
                    break

        if (testFlag):
            log_text+= "Status: Success\n\n"
        else:
            log_text+= "Status: Failed\n\n"
    log.write(log_text)

def TestSortContactFalse():
    log_text = "Test 4\ngetting records with no contact:\n"
    response = requests.post(GET_LIST_URL, json=GetUserContactFalseList)
    log_text += f"ResponseCode: {response.status_code}\n"

    if(response.status_code!=200):
        log_text += "Status: Failed\n\n"
    else:
        data = response.json()["info"]
        testFlag=True
        if(len(data)==0):
            testFlag = False
        else:
            for i in range(1,len(data)):
                if(data[i]["fcontact"]["hasContact"] == True):
                    testFlag = False
                    break

        if (testFlag):
            log_text+= "Status: Success\n\n"
        else:
            log_text+= "Status: Failed\n\n"
    log.write(log_text)

#Тесты, отвечающие за проверку получения количества записей по фильтрам

def TestSortGitTrueCount():
    log_text = "Test 5\ngetting records count with git:\n"
    response = requests.post(GET_COUNT_URL, json=GetUserGitTrueCount)
    log_text += f"ResponseCode: {response.status_code}\n"

    if(response.status_code!=200 or response.json()["resultData"] == None):
        log_text += "Status: Failed\n\n"
    else:
        log_text += "Status: Success\n\n"
    log.write(log_text)

def TestSortGitFalseCount():
    log_text = "Test 6\ngetting records count with no git:\n"
    response = requests.post(GET_COUNT_URL, json=GetUserGitFalseCount)
    log_text += f"ResponseCode: {response.status_code}\n"

    if(response.status_code!=200 or response.json()["resultData"] == None):
        log_text += "Status: Failed\n\n"
    else:
        log_text += "Status: Success\n\n"
    log.write(log_text)

def TestSortContactTrueCount():
    log_text = "Test 7\ngetting records count with contact:\n"
    response = requests.post(GET_COUNT_URL, json=GetUserContactTrueCount)
    log_text += f"ResponseCode: {response.status_code}\n"

    if(response.status_code!=200 or response.json()["resultData"] == None):
        log_text += "Status: Failed\n\n"
    else:
        log_text += "Status: Success\n\n"
    log.write(log_text)

def TestSortContactFalseCount():
    log_text = "Test 8\ngetting records count with no contact:\n"
    response = requests.post(GET_COUNT_URL, json=GetUserContactFalseCount)
    log_text += f"ResponseCode: {response.status_code}\n"

    if(response.status_code!=200 or response.json()["resultData"] == None):
        log_text += "Status: Failed\n\n"
    else:
        log_text += "Status: Success\n\n"
    log.write(log_text)

#Множественная функция тестов для проверки получения списка по нескольким фильтрам

def TestSortDoubleFilterList():
    testCounter = 9
    for git in [True,False]:
        for contact in [True,False]:
            t1 = 'no ' * (not git)
            t2 = 'no ' * (not contact)
            log_text = f'Test {testCounter}\ngetting records with {t1}git and {t2}contact:\n'
            sendData = GetUserDoubleFilterList(git,contact)
            response = requests.post(GET_LIST_URL, json=sendData)
            log_text += f"ResponseCode: {response.status_code}\n"

            if (response.status_code != 200):
                log_text += "Status: Failed\n\n"
            else:
                data = response.json()["info"]

                testFlag = True
                if (len(data) == 0):
                    testFlag = False
                else:
                    for i in range(1, len(data)):
                        if (not (data[i]["fcontact"]["hasContact"] == contact)) or (not(data[i]["fgit"]["hasGit"] == git)):
                            testFlag = False
                            break

                if (testFlag):
                    log_text += "Status: Success\n\n"
                else:
                    log_text += "Status: Failed\n\n"
            log.write(log_text)
            testCounter+=1

#Множественная функция тестов для проверки получения количества записей по нескольким фильтрам
def TestSortDoubleFilterCount():
    testCounter = 13
    for git in [True, False]:
        for contact in [True, False]:
            t1 = 'no ' * (not git)
            t2 = 'no ' * (not contact)
            log_text = f'Test {testCounter}\ngetting records count with {t1}git and {t2}contact:\n'
            sendData = GetUserDoubleFilterCount(git, contact)
            response = requests.post(GET_COUNT_URL, json=sendData)
            log_text += f"ResponseCode: {response.status_code}\n"

            if (response.status_code != 200 or response.json()["resultData"] == None):
                log_text += "Status: Failed\n\n"
            else:
                log_text += "Status: Success\n\n"
            log.write(log_text)
            testCounter+=1


TestSortGitTrue()
TestSortGitFalse()

TestSortContactTrue()
TestSortContactFalse()

TestSortGitTrueCount()
TestSortGitFalseCount()

TestSortContactTrueCount()
TestSortContactFalseCount()

TestSortDoubleFilterList()
TestSortDoubleFilterCount()
