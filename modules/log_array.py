import json
from config import BATCH_SIZE

#data = {"host":{"os":{"version":"10.0","kernel":"10.0.14393.693 (rs1_release.161220-1747)","platform":"windows","build":"14393.693","type":"windows","name":"Windows Server 2016 Standard Evaluation","family":"windows"},"ip":["10.50.64.2","fe80::5efe:a32:4002","fe80::ffff:ffff:fffe"],"mac":["00:0c:29:5e:62:96","00:00:00:00:00:00:00:e0","00:00:00:00:00:00:00:e0"],"hostname":"regina","name":"regina.vmware.fekt.cz","architecture":"x86_64","id":"449dafd7-34fb-460e-babb-70a78ed83d18"},"event":{"action":"Logoff","outcome":"success","original":"<Event xmlns=\'http://schemas.microsoft.com/win/2004/08/events/event\'><System><Provider Name=\'Microsoft-Windows-Security-Auditing\' Guid=\'{54849625-5478-4994-A5BA-3E3B0328C30D}\'/><EventID>4634</EventID><Version>0</Version><Level>0</Level><Task>12545</Task><Opcode>0</Opcode><Keywords>0x8020000000000000</Keywords><TimeCreated SystemTime=\'2022-11-25T20:10:35.544859500Z\'/><EventRecordID>6170175</EventRecordID><Correlation/><Execution ProcessID=\'576\' ThreadID=\'4544\'/><Channel>Security</Channel><Computer>regina.vmware.fekt.cz</Computer><Security/></System><EventData><Data Name=\'TargetUserSid\'>S-1-5-18</Data><Data Name=\'TargetUserName\'>REGINA$</Data><Data Name=\'TargetDomainName\'>vmware</Data><Data Name=\'TargetLogonId\'>0x2e5d58d2</Data><Data Name=\'LogonType\'>3</Data></EventData><RenderingInfo Culture=\'en-US\'><Message>An account was logged off.\\r\\n\\r\\nSubject:\\r\\n\\tSecurity ID:\\t\\tS-1-5-18\\r\\n\\tAccount Name:\\t\\tREGINA$\\r\\n\\tAccount Domain:\\t\\tvmware\\r\\n\\tLogon ID:\\t\\t0x2E5D58D2\\r\\n\\r\\nLogon Type:\\t\\t\\t3\\r\\n\\r\\nThis event is generated when a logon session is destroyed. It may be positively correlated with a logon event using the Logon ID value. Logon IDs are only unique between reboots on the same computer.</Message><Level>Information</Level><Task>Logoff</Task><Opcode>Info</Opcode><Channel>Security</Channel><Provider>Microsoft Windows security auditing.</Provider><Keywords><Keyword>Audit Success</Keyword></Keywords></RenderingInfo></Event>","kind":"event","code":"4634","created":"2022-11-25T20:10:37.342Z","provider":"Microsoft-Windows-Security-Auditing"},"agent":{"version":"8.1.1","type":"winlogbeat","id":"9e448ec3-a416-4bce-bc2a-73bed1c4ec85","ephemeral_id":"7be1585c-a6b3-42f4-9f89-3941f0cb582b","name":"winlogbeat-shipper"},"message":"An account was logged off.\\n\\nSubject:\\n\\tSecurity ID:\\t\\tS-1-5-18\\n\\tAccount Name:\\t\\tREGINA$\\n\\tAccount Domain:\\t\\tvmware\\n\\tLogon ID:\\t\\t0x2E5D58D2\\n\\nLogon Type:\\t\\t\\t3\\n\\nThis event is generated when a logon session is destroyed. It may be positively correlated with a logon event using the Logon ID value. Logon IDs are only unique between reboots on the same computer.","log":{"level":"information"},"winlog":{"api":"wineventlog","task":"Logoff","computer_name":"regina.vmware.fekt.cz","event_data":{"TargetLogonId":"0x2e5d58d2","TargetUserSid":"S-1-5-18","TargetUserName":"REGINA$","TargetDomainName":"vmware","LogonType":"3"},"opcode":"Info","provider_guid":"{54849625-5478-4994-A5BA-3E3B0328C30D}","event_id":"4634","record_id":6170175,"channel":"Security","provider_name":"Microsoft-Windows-Security-Auditing","keywords":["Audit Success"],"process":{"pid":576,"thread":{"id":4544}}},"@timestamp":"2022-11-25T20:10:35.544Z","@version":"1","tags":["Windows Server 2016","DP-test","beats_input_codec_plain_applied"],"ecs":{"version":"8.0.0"}}

class LogArray:
    logArray = []
    size = 0
    nameNumber = 1

    def arrayAppend(self, data):
        self.logArray.append(json.loads(data))
        
    def getArray(self):
        return self.logArray
        
    def dumpLogs(self, number):
        with open(f'data{number}.json', 'w') as f:
            json.dump(self.getArray(), f)
            
    def getSize(self):
        return self.size 
        
    def getNameNumber(self):
        return self.nameNumber  
    
    def saveLogs(self, data):
        if self.size >= BATCH_SIZE:
            self.arrayAppend(data)
            self.size = self.size + 1
            print("Success?" + str(self.size))
        else:
            self.arrayAppend(data)
            self.dumpLogs(self.getNameNumber())
            self.nameNumber += 1
            self.size = 0
            # Logger = logs were exported with a batch size of BATCH_SIZE
        # NEFUNGUJE INKREMENTACIA...






