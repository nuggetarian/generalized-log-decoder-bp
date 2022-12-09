# Postup spustenia aplikácie

## Prvý krok - konfigurácia zdrojov logov

V prvom kroku je potrebné nakonfigurovať zdroje záznamov, aby odosielali záznamy na zvolenú inštanciu logstash.

### Windows logy

Pri windows systémoch sa používa software _winlogbeat_, určený pre zmenu módu windows logov z pull na push. 
Inštalácia pozostáva z nasledujúcich krokov[^1]:

- Stiahnutie zip súboru
- Rozbalenie do C:\Program Files
- Premenovanie _winlogbeat-<version>_ priečinku na _Winlogbeat_
- Powershell príkaz na inštaláciu:
```shell
.\install-service-winlogbeat.ps1
```

V konfiguračnom súbore winlogbeat.yml sa nastaví výstup na logstash s ľubovoľnou adresou:

```
output.logstash:
  hosts: ["127.0.0.1:5044"]
```

Winlogbeat sa spustí príkazom:
```shell
winlogbeat.exe -c winlogbeat.yml
```
  
### Syslog

Pre nastavenie daemona rsyslog na automatické odosielanie logov:
```shell
nano /etc/rsyslog.conf
```
  
V súbore je možné zvoliť spôsob odosielania - TCP alebo UDP. Žiadúci spôsob stačí odkomentovať.
  
Následne sa zvolí, aké typy logov budú prichádzať, na akú adresu a na akom porte, napríklad:
```
auth.* @127.0.0.1:514
authpriv.* @127.0.0.1:514
kern.* @127.0.0.1:514
*.emerg @127.0.0.1:514
```

Po reštarte daemona by mala byť funkcia zapnutá:
```shell
service rsyslog restart
```
  
## Druhý krok - spustenie Logstash

Po nainštalovaní ELK stack sa konfiguračný súbor nachádza v priečinku config v priečinku Logstash.
Na spustenie _Logstash pipeline_ s konfiguráciou sa používa nasledujúci príkaz: 
```shell
./bin/logstash -f config/logstash-sample.conf --config.reload.automatic
```  
Ukážka konfigurácie je dostupná [tu](/logstash-sample.conf)
  
## Tretí krok - Spustenie API
Na spustenie je potrebné nainštalovať flask:
```shell
pip install flask
``` 
API sa spúšťa cez hlavný súbor **app.py**.
  
Konfigurácia množstva záznamov uložených do súborov sa vykonáva úpravou premennej BATCH_SIZE, v súbore **config.py**.


[^1]: Dostupné [tu](https://www.elastic.co/guide/en/beats/winlogbeat/current/winlogbeat-installation-configuration.html)
