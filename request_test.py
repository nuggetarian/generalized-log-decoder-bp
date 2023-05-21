import requests
from time import perf_counter

url = "http://127.0.0.1:29170/v1/processmsg"

payload = {
    "@timestamp": "2022-12-08T23:37:18Z",
    "@version": "1",
    "event": {
        "original": "<86>Dec  8 23:37:18 miri logon: LOGIN ON tty1 BY mzernovic"
    },
    "host": {
        "hostname": "miri",
        "ip": "10.50.64.5"
    },
    "log": {
        "syslog": {
            "facility": {
                "code": 10,
                "name": "security/authorization"
            },
            "priority": 86,
            "severity": {
                "code": 6,
                "name": "Informational"
            }
        }
    },
    "message": "LOGIN ON tty1 BY mzernovic",
    "process": {
        "name": "login"
    },
    "service": {
        "type": "system"
    }
}

headers = {
    "Content-Type": "application/json"
}

start = perf_counter()
for _ in range(15):
    response = requests.post(url, json=payload, headers=headers)
    print(response.status_code)
end = perf_counter()
time = format(round((end - start)*1000))
print(time)