import requests
from time import perf_counter

# Url endpointu s modmi
url = "http://127.0.0.1:29170/v1/processmsg"
# Pocet odoslania poziadavky
logs_sent = 10

# Odosielany log
payload = {
    "@timestamp": "2022-12-08T23:37:18Z",
    "@version": "1",
    "event": {
      "original": "<86>Dec  8 23:37:18 miri logon: LOGIN ON tty1 BY mzernovic"
    },
    "host": {
      "hostname": "daniellerobertson",
      "ip": "10.221.105.224"
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

# Header, ze ide o json poziadavku
headers = {
    "Content-Type": "application/json"
}


start = perf_counter() # Pocitadlo odosielaneho casu v ms
for _ in range(logs_sent): # For loop na odosielanie poziadaviek a ziskanie status kodu
    response = requests.post(url, json=payload, headers=headers)
    print(response.status_code)
end = perf_counter()
time = format(round((end - start)*1000))
print("Time taken to send requests: " + time)