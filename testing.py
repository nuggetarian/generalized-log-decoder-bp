from modules.beautify import Beautify
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
import json
from log_array import LogArray

PATH = 'D:\\BakalarskaPraca\\bakalarska-praca\\generalized-log-decoder-bp\\'

# read json
file = 'log.json'


def beautify_test():
    const_log = b'{"host":{"os":{"version":"10.0","kernel":"10.0.14393.693 (rs1_release.161220-1747)","platform":"windows","build":"14393.693","type":"windows","name":"Windows Server 2016 Standard Evaluation","family":"windows"},"ip":["10.50.64.2","fe80::5efe:a32:4002","fe80::ffff:ffff:fffe"],"mac":["00:0c:29:5e:62:96","00:00:00:00:00:00:00:e0","00:00:00:00:00:00:00:e0"],"hostname":"regina","name":"regina.vmware.fekt.cz","architecture":"x86_64","id":"449dafd7-34fb-460e-babb-70a78ed83d18"},"event":{"action":"Logoff","outcome":"success","original":"<Event xmlns=\'http://schemas.microsoft.com/win/2004/08/events/event\'><System><Provider Name=\'Microsoft-Windows-Security-Auditing\' Guid=\'{54849625-5478-4994-A5BA-3E3B0328C30D}\'/><EventID>4634</EventID><Version>0</Version><Level>0</Level><Task>12545</Task><Opcode>0</Opcode><Keywords>0x8020000000000000</Keywords><TimeCreated SystemTime=\'2022-11-25T20:10:35.544859500Z\'/><EventRecordID>6170175</EventRecordID><Correlation/><Execution ProcessID=\'576\' ThreadID=\'4544\'/><Channel>Security</Channel><Computer>regina.vmware.fekt.cz</Computer><Security/></System><EventData><Data Name=\'TargetUserSid\'>S-1-5-18</Data><Data Name=\'TargetUserName\'>REGINA$</Data><Data Name=\'TargetDomainName\'>vmware</Data><Data Name=\'TargetLogonId\'>0x2e5d58d2</Data><Data Name=\'LogonType\'>3</Data></EventData><RenderingInfo Culture=\'en-US\'><Message>An account was logged off.\\r\\n\\r\\nSubject:\\r\\n\\tSecurity ID:\\t\\tS-1-5-18\\r\\n\\tAccount Name:\\t\\tREGINA$\\r\\n\\tAccount Domain:\\t\\tvmware\\r\\n\\tLogon ID:\\t\\t0x2E5D58D2\\r\\n\\r\\nLogon Type:\\t\\t\\t3\\r\\n\\r\\nThis event is generated when a logon session is destroyed. It may be positively correlated with a logon event using the Logon ID value. Logon IDs are only unique between reboots on the same computer.</Message><Level>Information</Level><Task>Logoff</Task><Opcode>Info</Opcode><Channel>Security</Channel><Provider>Microsoft Windows security auditing.</Provider><Keywords><Keyword>Audit Success</Keyword></Keywords></RenderingInfo></Event>","kind":"event","code":"4634","created":"2022-11-25T20:10:37.342Z","provider":"Microsoft-Windows-Security-Auditing"},"agent":{"version":"8.1.1","type":"winlogbeat","id":"9e448ec3-a416-4bce-bc2a-73bed1c4ec85","ephemeral_id":"7be1585c-a6b3-42f4-9f89-3941f0cb582b","name":"winlogbeat-shipper"},"message":"An account was logged off.\\n\\nSubject:\\n\\tSecurity ID:\\t\\tS-1-5-18\\n\\tAccount Name:\\t\\tREGINA$\\n\\tAccount Domain:\\t\\tvmware\\n\\tLogon ID:\\t\\t0x2E5D58D2\\n\\nLogon Type:\\t\\t\\t3\\n\\nThis event is generated when a logon session is destroyed. It may be positively correlated with a logon event using the Logon ID value. Logon IDs are only unique between reboots on the same computer.","log":{"level":"information"},"winlog":{"api":"wineventlog","task":"Logoff","computer_name":"regina.vmware.fekt.cz","event_data":{"TargetLogonId":"0x2e5d58d2","TargetUserSid":"S-1-5-18","TargetUserName":"REGINA$","TargetDomainName":"vmware","LogonType":"3"},"opcode":"Info","provider_guid":"{54849625-5478-4994-A5BA-3E3B0328C30D}","event_id":"4634","record_id":6170175,"channel":"Security","provider_name":"Microsoft-Windows-Security-Auditing","keywords":["Audit Success"],"process":{"pid":576,"thread":{"id":4544}}},"@timestamp":"2022-11-25T20:10:35.544Z","@version":"1","tags":["Windows Server 2016","DP-test","beats_input_codec_plain_applied"],"ecs":{"version":"8.0.0"}}'
    beauty = Beautify()
    normalized = beauty.beautify(const_log)
    print(normalized.rstrip())

def beautify_file_test():
    const_log = b'{"host":{"os":{"version":"10.0","kernel":"10.0.14393.693 (rs1_release.161220-1747)","platform":"windows","build":"14393.693","type":"windows","name":"Windows Server 2016 Standard Evaluation","family":"windows"},"ip":["10.50.64.2","fe80::5efe:a32:4002","fe80::ffff:ffff:fffe"],"mac":["00:0c:29:5e:62:96","00:00:00:00:00:00:00:e0","00:00:00:00:00:00:00:e0"],"hostname":"regina","name":"regina.vmware.fekt.cz","architecture":"x86_64","id":"449dafd7-34fb-460e-babb-70a78ed83d18"},"event":{"action":"Logoff","outcome":"success","original":"<Event xmlns=\'http://schemas.microsoft.com/win/2004/08/events/event\'><System><Provider Name=\'Microsoft-Windows-Security-Auditing\' Guid=\'{54849625-5478-4994-A5BA-3E3B0328C30D}\'/><EventID>4634</EventID><Version>0</Version><Level>0</Level><Task>12545</Task><Opcode>0</Opcode><Keywords>0x8020000000000000</Keywords><TimeCreated SystemTime=\'2022-11-25T20:10:35.544859500Z\'/><EventRecordID>6170175</EventRecordID><Correlation/><Execution ProcessID=\'576\' ThreadID=\'4544\'/><Channel>Security</Channel><Computer>regina.vmware.fekt.cz</Computer><Security/></System><EventData><Data Name=\'TargetUserSid\'>S-1-5-18</Data><Data Name=\'TargetUserName\'>REGINA$</Data><Data Name=\'TargetDomainName\'>vmware</Data><Data Name=\'TargetLogonId\'>0x2e5d58d2</Data><Data Name=\'LogonType\'>3</Data></EventData><RenderingInfo Culture=\'en-US\'><Message>An account was logged off.\\r\\n\\r\\nSubject:\\r\\n\\tSecurity ID:\\t\\tS-1-5-18\\r\\n\\tAccount Name:\\t\\tREGINA$\\r\\n\\tAccount Domain:\\t\\tvmware\\r\\n\\tLogon ID:\\t\\t0x2E5D58D2\\r\\n\\r\\nLogon Type:\\t\\t\\t3\\r\\n\\r\\nThis event is generated when a logon session is destroyed. It may be positively correlated with a logon event using the Logon ID value. Logon IDs are only unique between reboots on the same computer.</Message><Level>Information</Level><Task>Logoff</Task><Opcode>Info</Opcode><Channel>Security</Channel><Provider>Microsoft Windows security auditing.</Provider><Keywords><Keyword>Audit Success</Keyword></Keywords></RenderingInfo></Event>","kind":"event","code":"4634","created":"2022-11-25T20:10:37.342Z","provider":"Microsoft-Windows-Security-Auditing"},"agent":{"version":"8.1.1","type":"winlogbeat","id":"9e448ec3-a416-4bce-bc2a-73bed1c4ec85","ephemeral_id":"7be1585c-a6b3-42f4-9f89-3941f0cb582b","name":"winlogbeat-shipper"},"message":"An account was logged off.\\n\\nSubject:\\n\\tSecurity ID:\\t\\tS-1-5-18\\n\\tAccount Name:\\t\\tREGINA$\\n\\tAccount Domain:\\t\\tvmware\\n\\tLogon ID:\\t\\t0x2E5D58D2\\n\\nLogon Type:\\t\\t\\t3\\n\\nThis event is generated when a logon session is destroyed. It may be positively correlated with a logon event using the Logon ID value. Logon IDs are only unique between reboots on the same computer.","log":{"level":"information"},"winlog":{"api":"wineventlog","task":"Logoff","computer_name":"regina.vmware.fekt.cz","event_data":{"TargetLogonId":"0x2e5d58d2","TargetUserSid":"S-1-5-18","TargetUserName":"REGINA$","TargetDomainName":"vmware","LogonType":"3"},"opcode":"Info","provider_guid":"{54849625-5478-4994-A5BA-3E3B0328C30D}","event_id":"4634","record_id":6170175,"channel":"Security","provider_name":"Microsoft-Windows-Security-Auditing","keywords":["Audit Success"],"process":{"pid":576,"thread":{"id":4544}}},"@timestamp":"2022-11-25T20:10:35.544Z","@version":"1","tags":["Windows Server 2016","DP-test","beats_input_codec_plain_applied"],"ecs":{"version":"8.0.0"}}'
    beauty = Beautify()
    finished = beauty.beautify(const_log)
    print(finished)
    file_object = open('exported_files\\txt_log_document.json', 'a')
    file_object.write(str(finished))

def pandas_test():
    with open('D:\\BakalarskaPraca\\bakalarska-praca\\generalized-log-decoder-bp\\log.json') as project_file:    
        data = json.load(project_file)  

    df = pd.json_normalize(data)
    print(df)
    


def pandas_object_test():
    data = json.loads('{"host":{"os":{"version":"10.0","kernel":"10.0.14393.693 (rs1_release.161220-1747)","platform":"windows","build":"14393.693","type":"windows","name":"Windows Server 2016 Standard Evaluation","family":"windows"},"ip":["10.50.64.2","fe80::5efe:a32:4002","fe80::ffff:ffff:fffe"],"mac":["00:0c:29:5e:62:96","00:00:00:00:00:00:00:e0","00:00:00:00:00:00:00:e0"],"hostname":"regina","name":"regina.vmware.fekt.cz","architecture":"x86_64","id":"449dafd7-34fb-460e-babb-70a78ed83d18"},"event":{"action":"Logoff","outcome":"success","original":"<Event xmlns=\'http://schemas.microsoft.com/win/2004/08/events/event\'><System><Provider Name=\'Microsoft-Windows-Security-Auditing\' Guid=\'{54849625-5478-4994-A5BA-3E3B0328C30D}\'/><EventID>4634</EventID><Version>0</Version><Level>0</Level><Task>12545</Task><Opcode>0</Opcode><Keywords>0x8020000000000000</Keywords><TimeCreated SystemTime=\'2022-11-25T20:10:35.544859500Z\'/><EventRecordID>6170175</EventRecordID><Correlation/><Execution ProcessID=\'576\' ThreadID=\'4544\'/><Channel>Security</Channel><Computer>regina.vmware.fekt.cz</Computer><Security/></System><EventData><Data Name=\'TargetUserSid\'>S-1-5-18</Data><Data Name=\'TargetUserName\'>REGINA$</Data><Data Name=\'TargetDomainName\'>vmware</Data><Data Name=\'TargetLogonId\'>0x2e5d58d2</Data><Data Name=\'LogonType\'>3</Data></EventData><RenderingInfo Culture=\'en-US\'><Message>An account was logged off.\\r\\n\\r\\nSubject:\\r\\n\\tSecurity ID:\\t\\tS-1-5-18\\r\\n\\tAccount Name:\\t\\tREGINA$\\r\\n\\tAccount Domain:\\t\\tvmware\\r\\n\\tLogon ID:\\t\\t0x2E5D58D2\\r\\n\\r\\nLogon Type:\\t\\t\\t3\\r\\n\\r\\nThis event is generated when a logon session is destroyed. It may be positively correlated with a logon event using the Logon ID value. Logon IDs are only unique between reboots on the same computer.</Message><Level>Information</Level><Task>Logoff</Task><Opcode>Info</Opcode><Channel>Security</Channel><Provider>Microsoft Windows security auditing.</Provider><Keywords><Keyword>Audit Success</Keyword></Keywords></RenderingInfo></Event>","kind":"event","code":"4634","created":"2022-11-25T20:10:37.342Z","provider":"Microsoft-Windows-Security-Auditing"},"agent":{"version":"8.1.1","type":"winlogbeat","id":"9e448ec3-a416-4bce-bc2a-73bed1c4ec85","ephemeral_id":"7be1585c-a6b3-42f4-9f89-3941f0cb582b","name":"winlogbeat-shipper"},"message":"An account was logged off.\\n\\nSubject:\\n\\tSecurity ID:\\t\\tS-1-5-18\\n\\tAccount Name:\\t\\tREGINA$\\n\\tAccount Domain:\\t\\tvmware\\n\\tLogon ID:\\t\\t0x2E5D58D2\\n\\nLogon Type:\\t\\t\\t3\\n\\nThis event is generated when a logon session is destroyed. It may be positively correlated with a logon event using the Logon ID value. Logon IDs are only unique between reboots on the same computer.","log":{"level":"information"},"winlog":{"api":"wineventlog","task":"Logoff","computer_name":"regina.vmware.fekt.cz","event_data":{"TargetLogonId":"0x2e5d58d2","TargetUserSid":"S-1-5-18","TargetUserName":"REGINA$","TargetDomainName":"vmware","LogonType":"3"},"opcode":"Info","provider_guid":"{54849625-5478-4994-A5BA-3E3B0328C30D}","event_id":"4634","record_id":6170175,"channel":"Security","provider_name":"Microsoft-Windows-Security-Auditing","keywords":["Audit Success"],"process":{"pid":576,"thread":{"id":4544}}},"@timestamp":"2022-11-25T20:10:35.544Z","@version":"1","tags":["Windows Server 2016","DP-test","beats_input_codec_plain_applied"],"ecs":{"version":"8.0.0"}}')
    
    df = pd.json_normalize(data)
    print(df)

    df.to_csv(r'exported_files\\csv_log_document.csv', mode='a', index = None)
    #df.to_csv('log_document.csv', mode='a', sep="\t", index=False, header=False)

def pandas_object_orientation_test():
    data = json.loads('{"host":{"os":{"version":"10.0","kernel":"10.0.14393.693 (rs1_release.161220-1747)","platform":"windows","build":"14393.693","type":"windows","name":"Windows Server 2016 Standard Evaluation","family":"windows"},"ip":["10.50.64.2","fe80::5efe:a32:4002","fe80::ffff:ffff:fffe"],"mac":["00:0c:29:5e:62:96","00:00:00:00:00:00:00:e0","00:00:00:00:00:00:00:e0"],"hostname":"regina","name":"regina.vmware.fekt.cz","architecture":"x86_64","id":"449dafd7-34fb-460e-babb-70a78ed83d18"},"event":{"action":"Logoff","outcome":"success","original":"<Event xmlns=\'http://schemas.microsoft.com/win/2004/08/events/event\'><System><Provider Name=\'Microsoft-Windows-Security-Auditing\' Guid=\'{54849625-5478-4994-A5BA-3E3B0328C30D}\'/><EventID>4634</EventID><Version>0</Version><Level>0</Level><Task>12545</Task><Opcode>0</Opcode><Keywords>0x8020000000000000</Keywords><TimeCreated SystemTime=\'2022-11-25T20:10:35.544859500Z\'/><EventRecordID>6170175</EventRecordID><Correlation/><Execution ProcessID=\'576\' ThreadID=\'4544\'/><Channel>Security</Channel><Computer>regina.vmware.fekt.cz</Computer><Security/></System><EventData><Data Name=\'TargetUserSid\'>S-1-5-18</Data><Data Name=\'TargetUserName\'>REGINA$</Data><Data Name=\'TargetDomainName\'>vmware</Data><Data Name=\'TargetLogonId\'>0x2e5d58d2</Data><Data Name=\'LogonType\'>3</Data></EventData><RenderingInfo Culture=\'en-US\'><Message>An account was logged off.\\r\\n\\r\\nSubject:\\r\\n\\tSecurity ID:\\t\\tS-1-5-18\\r\\n\\tAccount Name:\\t\\tREGINA$\\r\\n\\tAccount Domain:\\t\\tvmware\\r\\n\\tLogon ID:\\t\\t0x2E5D58D2\\r\\n\\r\\nLogon Type:\\t\\t\\t3\\r\\n\\r\\nThis event is generated when a logon session is destroyed. It may be positively correlated with a logon event using the Logon ID value. Logon IDs are only unique between reboots on the same computer.</Message><Level>Information</Level><Task>Logoff</Task><Opcode>Info</Opcode><Channel>Security</Channel><Provider>Microsoft Windows security auditing.</Provider><Keywords><Keyword>Audit Success</Keyword></Keywords></RenderingInfo></Event>","kind":"event","code":"4634","created":"2022-11-25T20:10:37.342Z","provider":"Microsoft-Windows-Security-Auditing"},"agent":{"version":"8.1.1","type":"winlogbeat","id":"9e448ec3-a416-4bce-bc2a-73bed1c4ec85","ephemeral_id":"7be1585c-a6b3-42f4-9f89-3941f0cb582b","name":"winlogbeat-shipper"},"message":"An account was logged off.\\n\\nSubject:\\n\\tSecurity ID:\\t\\tS-1-5-18\\n\\tAccount Name:\\t\\tREGINA$\\n\\tAccount Domain:\\t\\tvmware\\n\\tLogon ID:\\t\\t0x2E5D58D2\\n\\nLogon Type:\\t\\t\\t3\\n\\nThis event is generated when a logon session is destroyed. It may be positively correlated with a logon event using the Logon ID value. Logon IDs are only unique between reboots on the same computer.","log":{"level":"information"},"winlog":{"api":"wineventlog","task":"Logoff","computer_name":"regina.vmware.fekt.cz","event_data":{"TargetLogonId":"0x2e5d58d2","TargetUserSid":"S-1-5-18","TargetUserName":"REGINA$","TargetDomainName":"vmware","LogonType":"3"},"opcode":"Info","provider_guid":"{54849625-5478-4994-A5BA-3E3B0328C30D}","event_id":"4634","record_id":6170175,"channel":"Security","provider_name":"Microsoft-Windows-Security-Auditing","keywords":["Audit Success"],"process":{"pid":576,"thread":{"id":4544}}},"@timestamp":"2022-11-25T20:10:35.544Z","@version":"1","tags":["Windows Server 2016","DP-test","beats_input_codec_plain_applied"],"ecs":{"version":"8.0.0"}}')
    
    df = pd.json_normalize(data)
    df = df.transpose()
    print(df)

    df.to_csv(r'exported_files\\csv_log_document.csv', mode='a', index = None)

def pandas_from_csv():
    df = pd.read_csv('exported_files\\csv_log_document.csv')

    print(df.to_string())
    
def convert_to_dataframe():
    data = r'{"host":{"os":{"version":"10.0","kernel":"10.0.14393.693 (rs1_release.161220-1747)","platform":"windows","build":"14393.693","type":"windows","name":"Windows Server 2016 Standard Evaluation","family":"windows"},"ip":["10.50.64.2","fe80::5efe:a32:4002","fe80::ffff:ffff:fffe"],"mac":["00:0c:29:5e:62:96","00:00:00:00:00:00:00:e0","00:00:00:00:00:00:00:e0"],"hostname":"regina","name":"regina.vmware.fekt.cz","architecture":"x86_64","id":"449dafd7-34fb-460e-babb-70a78ed83d18"},"event":{"action":"Logoff","outcome":"success","original":"<Event xmlns=\'http://schemas.microsoft.com/win/2004/08/events/event\'><System><Provider Name=\'Microsoft-Windows-Security-Auditing\' Guid=\'{54849625-5478-4994-A5BA-3E3B0328C30D}\'/><EventID>4634</EventID><Version>0</Version><Level>0</Level><Task>12545</Task><Opcode>0</Opcode><Keywords>0x8020000000000000</Keywords><TimeCreated SystemTime=\'2022-11-25T20:10:35.544859500Z\'/><EventRecordID>6170175</EventRecordID><Correlation/><Execution ProcessID=\'576\' ThreadID=\'4544\'/><Channel>Security</Channel><Computer>regina.vmware.fekt.cz</Computer><Security/></System><EventData><Data Name=\'TargetUserSid\'>S-1-5-18</Data><Data Name=\'TargetUserName\'>REGINA$</Data><Data Name=\'TargetDomainName\'>vmware</Data><Data Name=\'TargetLogonId\'>0x2e5d58d2</Data><Data Name=\'LogonType\'>3</Data></EventData><RenderingInfo Culture=\'en-US\'><Message>An account was logged off.\\r\\n\\r\\nSubject:\\r\\n\\tSecurity ID:\\t\\tS-1-5-18\\r\\n\\tAccount Name:\\t\\tREGINA$\\r\\n\\tAccount Domain:\\t\\tvmware\\r\\n\\tLogon ID:\\t\\t0x2E5D58D2\\r\\n\\r\\nLogon Type:\\t\\t\\t3\\r\\n\\r\\nThis event is generated when a logon session is destroyed. It may be positively correlated with a logon event using the Logon ID value. Logon IDs are only unique between reboots on the same computer.</Message><Level>Information</Level><Task>Logoff</Task><Opcode>Info</Opcode><Channel>Security</Channel><Provider>Microsoft Windows security auditing.</Provider><Keywords><Keyword>Audit Success</Keyword></Keywords></RenderingInfo></Event>","kind":"event","code":"4634","created":"2022-11-25T20:10:37.342Z","provider":"Microsoft-Windows-Security-Auditing"},"agent":{"version":"8.1.1","type":"winlogbeat","id":"9e448ec3-a416-4bce-bc2a-73bed1c4ec85","ephemeral_id":"7be1585c-a6b3-42f4-9f89-3941f0cb582b","name":"winlogbeat-shipper"},"message":"An account was logged off.\\n\\nSubject:\\n\\tSecurity ID:\\t\\tS-1-5-18\\n\\tAccount Name:\\t\\tREGINA$\\n\\tAccount Domain:\\t\\tvmware\\n\\tLogon ID:\\t\\t0x2E5D58D2\\n\\nLogon Type:\\t\\t\\t3\\n\\nThis event is generated when a logon session is destroyed. It may be positively correlated with a logon event using the Logon ID value. Logon IDs are only unique between reboots on the same computer.","log":{"level":"information"},"winlog":{"api":"wineventlog","task":"Logoff","computer_name":"regina.vmware.fekt.cz","event_data":{"TargetLogonId":"0x2e5d58d2","TargetUserSid":"S-1-5-18","TargetUserName":"REGINA$","TargetDomainName":"vmware","LogonType":"3"},"opcode":"Info","provider_guid":"{54849625-5478-4994-A5BA-3E3B0328C30D}","event_id":"4634","record_id":6170175,"channel":"Security","provider_name":"Microsoft-Windows-Security-Auditing","keywords":["Audit Success"],"process":{"pid":576,"thread":{"id":4544}}},"@timestamp":"2022-11-25T20:10:35.544Z","@version":"1","tags":["Windows Server 2016","DP-test","beats_input_codec_plain_applied"],"ecs":{"version":"8.0.0"}}'
    
    
    # df = pd.json_normalize(data)
    # df = df.explode('properties.features')
    # df = pd.concat([df.drop('properties.features', axis=1).reset_index(drop=True),
    #                 pd.json_normalize(df['properties.features']).add_prefix('properties.features.')], axis=1)
    # df = df.explode('properties.features.features')
    # df = pd.concat([df.drop('properties.features.features', axis=1).reset_index(drop=True),
    #                 pd.json_normalize(df['properties.features.features']).add_prefix('properties.features.features.')], axis=1)
    
    #beauty = Beautify()
    #normalized = beauty.beautify(data)
    
    print(data)
    
    with open('exported_files\\new_file.json', 'a') as f:
        json.dump(data, f)
    
    
    

#pandas_object_test()
#beautify_test()
#pandas_test()
#beautify_file_test()
#pandas_beautify_test()
#pandas_object_orientation_test()
#pandas_from_csv()
#convert_to_dataframe()

def testing():
    data = {
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
        "original": "<Event xmlns='http://schemas.microsoft.com/win/2004/08/events/event'><System><Provider Name='Microsoft-Windows-Security-Auditing' Guid='{54849625-5478-4994-A5BA-3E3B0328C30D}'/><EventID>4634</EventID><Version>0</Version><Level>0</Level><Task>12545</Task><Opcode>0</Opcode><Keywords>0x8020000000000000</Keywords><TimeCreatedSystemTime='2022-11-25T20:10:35.544859500Z'/><EventRecordID>6170175</EventRecordID><Correlation/><Execution ProcessID='576' ThreadID='4544'/><Channel>Security</Channel><Computer>regina.vmware.fekt.cz</Computer><Security/></System><EventData><Data Name='TargetUserSid'>S-1-5-18</Data><Data Name='TargetUserName'>REGINA$</Data><Data Name='TargetDomainName'>vmware</Data><Data Name='TargetLogonId'>0x2e5d58d2</Data><Data Name='LogonType'>3</Data></EventData><RenderingInfo Culture='en-US'><Message>An account was logged off.\r\n\r\nSubject:\r\n\tSecurity ID:\t\tS-1-5-18\r\n\tAccount Name:\t\tREGINA$\r\n\tAccount Domain:\t\tvmware\r\n\tLogon ID:\t\t0x2E5D58D2\r\n\r\nLogon Type:\t\t\t3\r\n\r\nThis event is generated when a logon session is destroyed. It may be positively correlated with a logon event using the Logon ID value. Logon IDs are only unique between reboots on the same computer.</Message><Level>Information</Level><Task>Logoff</Task><Opcode>Info</Opcode><Channel>Security</Channel><Provider>Microsoft Windows security auditing.</Provider><Keywords><Keyword>Audit Success</Keyword></Keywords></RenderingInfo></Event>",
        "outcome": "success",
        "provider": "Microsoft-Windows-Security-Auditing"
    },
    "host": {
        "architecture": "x86_64",
        "hostname": "regina",
        "id": "449dafd7-34fb-460e-babb-70a78ed83d18",
        "ip": [
            "10.50.64.2",
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
    "message": "An account was logged off.\n\nSubject:\n\tSecurity ID:\t\tS-1-5-18\n\tAccount Name:\t\tREGINA$\n\tAccount Domain:\t\tvmware\n\tLogon ID:\t\t0x2E5D58D2\n\nLogon Type:\t\t\t3\n\nThis event is generated when a logon session is destroyed. It may be positively correlated with a logon event using the Logon ID value. Logon IDs are only unique between reboots on the same computer.",
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
            "TargetUserName": "REGINA$",
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
    
    arrayLog = LogArray()
    arrayLog.saveLogs()
