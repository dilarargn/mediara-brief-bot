import requests, pytz, time
from datetime import datetime

TOKEN = "8798597101:AAGEgstiYOZc0tv-0Y2V6r_8VGRvTKvCFNk"
CHAT_ID = "7205174532"
TZ = pytz.timezone("Europe/Istanbul")

def send(text):
    try:
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            json={"chat_id":CHAT_ID,"text":text,"parse_mode":"HTML","disable_web_page_preview":True},timeout=15)
    except Exception as e:
        print(f"Hata: {e}")

def hava():
    try:
        r = requests.get("https://api.open-meteo.com/v1/forecast?latitude=41.0082&longitude=28.9784&current=temperature_2m,weathercode,windspeed_10m&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max&timezone=Europe/Istanbul&forecast_days=5",timeout=10).json()
        wmo={0:"Acik",1:"Az bulutlu",2:"Parcali bulutlu",3:"Bulutlu",61:"Yagmur",80:"Saganak",95:"Firtina"}
        gun=["Pzt","Sal","Car","Per","Cum","Cmt","Paz"]
        d=r["daily"]; c=r["current"]
        hafta="\n".join([f"  {gun[datetime.strptime(d['time'][i],'%Y-%m-%d').weekday()]}: {round(d['temperature_2m_min'][i])}/{round(d['temperature_2m_max'][i])}C  %{d['precipitation_probability_max'][i]}" for i in range(5)])
        return f"<b>Istanbul Hava</b>\nSu an: {round(c['temperature_2m'])}C - {wmo.get(c['weathercode'],'Bulutlu')}\n\n<b>5 Gunluk:</b>\n{hafta}"
    except:
        return "Hava durumu alinamadi."

def haberler():
    gl=["Meta Manus AI Ads Manager ve Instagram entegre - SocialBee","ChatGPT reklam kanali self-serve acildi - Verkeer","Google Mart core update tamamlandi - ALM Corp","Instagram paylasim sinyali begeni onune gecirdi - SMToday","ABD influencer ekonomisi 2026 44 milyar dolar - Mktg Dive"]
    tr=["Brandverse Awards 2026 yeni kategori Influencer Creator - MktgTR","Meta Turkiye 6 ulkede DSA vergisi ekledi - SocialBee","LinkedIn Turkiye 20 milyonu gecti - Growth TR","Instagram paylasim sayisi artik begenden once - Growth TR","Google CMO: Arama kesif yolculuguna donustu - MediaCat"]
    return "<b>5 Yabanci Haber</b>\n\n"+"
".join(["- "+x for x in gl])+"\n\n<b>5 Turk Haber</b>\n\n"+"
".join(["- "+x for x in tr])

def oneriler():
    g={"Monday":"Pazartesi","Tuesday":"Sali","Wednesday":"Carsamba","Thursday":"Persembe","Friday":"Cuma","Saturday":"Cumartesi","Sunday":"Pazar"}
    return f"<b>{g.get(datetime.now(TZ).strftime('%A'),'Bugun')} Icerik Onerileri</b>\n\nMedya Ajansi:\n - Instagram: Trend konu + gorsel\n - Facebook: Sektor haberi\n\nIQ Denetim:\n - LinkedIn: Mevzuat bilgi karti\n - Facebook: Haftalik finans notu"

ay={"January":"Ocak","February":"Subat","March":"Mart","April":"Nisan","May":"Mayis","June":"Haziran","July":"Temmuz","August":"Agustos","September":"Eylul","October":"Ekim","November":"Kasim","December":"Aralik"}
gn={"Monday":"Pazartesi","Tuesday":"Sali","Wednesday":"Carsamba","Thursday":"Persembe","Friday":"Cuma","Saturday":"Cumartesi","Sunday":"Pazar"}
now=datetime.now(TZ)
tarih=f"{now.day} {ay[now.strftime('%B')]} {now.year}, {gn[now.strftime('%A')]}"
send(f"Gunaydin Dilara!\n{tarih}\n")
time.sleep(1); send(hava())
time.sleep(1); send(haberler())
time.sleep(1); send(oneriler())
time.sleep(1); send("Brief tamamlandi! Iyi calismalar!")
print(f"Brief: {datetime.now()}")
