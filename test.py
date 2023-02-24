import json

json1 = {
    "@timestamp": "2022-11-25T20:10:35.544Z",
    "@version": "1",
    "agent": {
        "ephemeral_id": "7be1585c-a6b3-42f4-9f89-3941f0cb582b",
        "id": "9e448ec3-a416-4bce-bc2a-73bed1c4ec85",
        "name": "winlogbeat-shipper",
        "type": "winlogbeat",
        "version": "8.1.1"
    },
    "ecs": {
        "version": "8.0.0"
    },
    "event": {
        "action": "Logoff",
        "code": "4634",
        "created": "2022-11-25T20:10:37.342Z",
        "kind": "event",
        "original": "<Event xmlns='http://schemas.microsoft.com/win/2004/08/events/event'><System><Provider Name='Microsoft-Windows-Security-Auditing' Guid='{54849625-5478-4994-A5BA-3E3B0328C30D}'/><EventID>4634</EventID><Version>0</Version><Level>0</Level><Task>12545</Task><Opcode>0</Opcode><Keywords>0x8020000000000000</Keywords><TimeCreatedSystemTime='2022-11-25T20:10:35.544859500Z'/><EventRecordID>6170175</EventRecordID><Correlation/><Execution ProcessID='576' ThreadID='4544'/><Channel>Security</Channel><Computer>radka.vmware.fekt.cz</Computer><Security/></System><EventData><Data Name='TargetUserSid'>S-1-5-18</Data><Data Name='TargetUserName'>radka20</Data><Data Name='TargetDomainName'>vmware</Data><Data Name='TargetLogonId'>0x2e5d58d2</Data><Data Name='LogonType'>3</Data></EventData><RenderingInfo Culture='en-US'><Message>An account was logged off.\r\n\r\nSubject:\r\n\tSecurity ID:\t\tS-1-5-18\r\n\tAccount Name:\t\tradka20\r\n\tAccount Domain:\t\tvmware\r\n\tLogon ID:\t\t0x2E5D58D2\r\n\r\nLogon Type:\t\t\t3\r\n\r\nThis event is generated when a logon session is destroyed. It may be positively correlated with a logon event using the Logon ID value. Logon IDs are only unique between reboots on the same computer.</Message><Level>Information</Level><Task>Logoff</Task><Opcode>Info</Opcode><Channel>Security</Channel><Provider>Microsoft Windows security auditing.</Provider><Keywords><Keyword>Audit Success</Keyword></Keywords></RenderingInfo></Event>",
        "outcome": "success",
        "provider": "Microsoft-Windows-Security-Auditing"
    },
    "host": {
        "architecture": "x86_64",
        "hostname": "radka",
        "id": "449dafd7-34fb-460e-babb-70a78ed83d18",
        "ip": [
            "10.50.64.8",
            "fe80::5efe:a32:4002",
            "fe80::ffff:ffff:fffe"
        ],
        "mac": [
            "00:0c:29:5e:62:96",
            "00:00:00:00:00:00:00:e0",
            "00:00:00:00:00:00:00:e0"
        ],
        "name": "radka.vmware.fekt.cz",
        "os": {
            "build": "14393.693",
            "family": "windows",
            "kernel": "10.0.14393.693 (rs1_release.161220-1747)",
            "name": "Windows Server 2016 Standard Evaluation",
            "platform": "windows",
            "type": "windows",
            "version": "10.0"
        }
    },
    "log": {
        "level": "information"
    },
    "message": "An account was logged off.\n\nSubject:\n\tSecurity ID:\t\tS-1-5-18\n\tAccount Name:\t\tradka20\n\tAccount Domain:\t\tvmware\n\tLogon ID:\t\t0x2E5D58D2\n\nLogon Type:\t\t\t3\n\nThis event is generated when a logon session is destroyed. It may be positively correlated with a logon event using the Logon ID value. Logon IDs are only unique between reboots on the same computer.",
    "tags": [
        "Windows",
        "DP-test",
        "beats_input_codec_plain_applied"
    ],
    "winlog": {
        "api": "wineventlog",
        "channel": "Security",
        "computer_name": "radka.vmware.fekt.cz",
        "event_data": {
            "LogonType": "3",
            "TargetDomainName": "vmware",
            "TargetLogonId": "0x2e5d58d2",
            "TargetUserName": "radka20",
            "TargetUserSid": "S-1-5-18"
        },
        "event_id": "4634",
        "keywords": [
            "Audit Success"
        ],
        "opcode": "Info",
        "process": {
            "pid": 576,
            "thread": {
                "id": 4544
            }
        },
        "provider_guid": "{54849625-5478-4994-A5BA-3E3B0328C30D}",
        "provider_name": "Microsoft-Windows-Security-Auditing",
        "record_id": 6170175,
        "task": "Logoff"
    }
}

json2 = {
    "@timestamp": "2022-11-25T20:10:35.544Z",
    "@version": "1",
    "agent": {
        "ephemeral_id": "7be1585c-a6b3-42f4-9f89-3941f0cb582b",
        "id": "9e448ec3-a416-4bce-bc2a-73bed1c4ec85",
        "name": "winlogbeat-shipper",
        "type": "winlogbeat",
        "version": "8.1.1"
    },
    "ecs": {
        "version": "8.0.0"
    },
    "event": {
        "action": "Logoff",
        "code": "4634",
        "created": "2022-11-25T20:10:37.342Z",
        "kind": "event",
        "original": "<Event xmlns='http://schemas.microsoft.com/win/2004/08/events/event'><System><Provider Name='Microsoft-Windows-Security-Auditing' Guid='{54849625-5478-4994-A5BA-3E3B0328C30D}'/><EventID>4634</EventID><Version>0</Version><Level>0</Level><Task>12545</Task><Opcode>0</Opcode><Keywords>0x8020000000000000</Keywords><TimeCreatedSystemTime='2022-11-25T20:10:35.544859500Z'/><EventRecordID>6170175</EventRecordID><Correlation/><Execution ProcessID='576' ThreadID='4544'/><Channel>Security</Channel><Computer>regina.vmware.fekt.cz</Computer><Security/></System><EventData><Data Name='TargetUserSid'>S-1-5-18</Data><Data Name='TargetUserName'>regina123</Data><Data Name='TargetDomainName'>vmware</Data><Data Name='TargetLogonId'>0x2e5d58d2</Data><Data Name='LogonType'>3</Data></EventData><RenderingInfo Culture='en-US'><Message>An account was logged off.\r\n\r\nSubject:\r\n\tSecurity ID:\t\tS-1-5-18\r\n\tAccount Name:\t\tregina123\r\n\tAccount Domain:\t\tvmware\r\n\tLogon ID:\t\t0x2E5D58D2\r\n\r\nLogon Type:\t\t\t3\r\n\r\nThis event is generated when a logon session is destroyed. It may be positively correlated with a logon event using the Logon ID value. Logon IDs are only unique between reboots on the same computer.</Message><Level>Information</Level><Task>Logoff</Task><Opcode>Info</Opcode><Channel>Security</Channel><Provider>Microsoft Windows security auditing.</Provider><Keywords><Keyword>Audit Success</Keyword></Keywords></RenderingInfo></Event>",
        "outcome": "success",
        "provider": "Microsoft-Windows-Security-Auditing"
    },
    "host": {
        "architecture": "x86_64",
        "hostname": "regina",
        "id": "449dafd7-34fb-460e-babb-70a78ed83d18",
        "ip": [
            "10.50.64.6",
            "fe80::5efe:a32:4002",
            "fe80::ffff:ffff:fffe"
        ],
        "mac": [
            "00:0c:29:5e:62:96",
            "00:00:00:00:00:00:00:e0",
            "00:00:00:00:00:00:00:e0"
        ],
        "name": "regina.vmware.fekt.cz",
        "os": {
            "build": "14393.693",
            "family": "windows",
            "kernel": "10.0.14393.693 (rs1_release.161220-1747)",
            "name": "Windows Server 2016 Standard Evaluation",
            "platform": "windows",
            "type": "windows",
            "version": "10.0"
        }
    },
    "log": {
        "level": "information"
    },
    "message": "An account was logged off.\n\nSubject:\n\tSecurity ID:\t\tS-1-5-18\n\tAccount Name:\t\tregina123\n\tAccount Domain:\t\tvmware\n\tLogon ID:\t\t0x2E5D58D2\n\nLogon Type:\t\t\t3\n\nThis event is generated when a logon session is destroyed. It may be positively correlated with a logon event using the Logon ID value. Logon IDs are only unique between reboots on the same computer.",
    "tags": [
        "Windows Server 2016",
        "DP-test",
        "beats_input_codec_plain_applied"
    ],
    "winlog": {
        "api": "wineventlog",
        "channel": "Security",
        "computer_name": "regina.vmware.fekt.cz",
        "event_data": {
            "LogonType": "3",
            "TargetDomainName": "vmware",
            "TargetLogonId": "0x2e5d58d2",
            "TargetUserName": "regina123",
            "TargetUserSid": "S-1-5-18"
        },
        "event_id": "4634",
        "keywords": [
            "Audit Success"
        ],
        "opcode": "Info",
        "process": {
            "pid": 576,
            "thread": {
                "id": 4544
            }
        },
        "provider_guid": "{54849625-5478-4994-A5BA-3E3B0328C30D}",
        "provider_name": "Microsoft-Windows-Security-Auditing",
        "record_id": 6170175,
        "task": "Logoff"
    }
} 

def json_compare(json1, json2):
    #Compare all keys
    for key in json1.keys():
        #if key exist in json2:
        if key in json2.keys():
            #If subjson
            if type(json1[key]) == dict:
                json_compare(json1[key], json2[key])
        else:
            return False
    return True


print(json_compare(json1, json2))