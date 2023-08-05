import requests
from datetime import datetime
from twilio.rest import Client
import json
import random
dosya_yolu = 'rid.json'
eklenecek_karakter = "*"

def bilmeceleri_oku(dosya_yolu):
    with open(dosya_yolu, 'r') as dosya:
        return json.load(dosya)
bilmeceler_listesi = bilmeceleri_oku(dosya_yolu)

def save():
    with open(dosya_yolu, 'w') as dosya:
        json.dump(bilmeceler_listesi, dosya, indent=4)

# JSON manupilation

def cevabi_bul():
    for i in bilmeceler_listesi:
        if i["riddle"][0] == "*":
            return i["answer"]
        save()

def karakter_sil(args):
    for i in args:
        if i["riddle"][0] == "*":
            i["riddle"] = i["riddle"][1:]
        save()

def soru():
    for i in bilmeceler_listesi:
        if i["riddle"][0] == "*":
            return i["riddle"][1:]
        save()

def karakter_ekle(bilmeceler_listesi, eklenecek_karakter):
    index=random.randint(0, len(bilmeceler_listesi)-1)
    bilmeci=bilmeceler_listesi[index]
    bilmeci["riddle"] = eklenecek_karakter + bilmeci["riddle"]
    save()
    return bilmeceler_listesi


# Run the functions
def sa():
    x=str(cevabi_bul())
    y="Last riddles answer: "+x
    karakter_sil(bilmeceler_listesi)
    karakter_ekle(bilmeceler_listesi, eklenecek_karakter)
    a=str(soru())
    b="New riddle: "+a
    return y,b
def getWeather():
    que,ans=sa()
    url = "https://api.openweathermap.org/data/3.0/onecall?lat=39.77673824449652&lon=39.471621794944205&exclude=daily&units=metric&lang=tr&appid=***"
    response = requests.get(url)
    data = response.json()
    tarih=str(datetime.fromtimestamp(data["current"]["dt"]))
    message= "Date: "+tarih+ "\n"+"Weather: " + data["current"]["weather"][0]["description"] + "\n" +que+"\n"+ans+"\n"+ "Temp. : " + str(data["current"]["temp"]) + " C"
    return message

def sms():
    account_sid = '**************'
    auth_token = '**************'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='**************',
        body=getWeather(),
        to='**************'
    )
if __name__ == "__main__":
    sms()