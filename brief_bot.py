import requests
import pytz
import time
from datetime import datetime

TOKEN = "8798597101:AAGEgstiYOZc0tv-0Y2V6r_8VGRvTKvCFNk"
CHAT_ID = "7205174532"
TZ = pytz.timezone("Europe/Istanbul")


def send(text):
    try:
        requests.post(
            "https://api.telegram.org/bot" + TOKEN + "/sendMessage",
            json={
                "chat_id": CHAT_ID,
                "text": text,
                "parse_mode": "HTML",
                "disable_web_page_preview": True
            },
            timeout=15
        )
    except Exception as e:
        print("Hata: " + str(e))


def hava():
    try:
        url = (
            "https://api.open-meteo.com/v1/forecast"
            "?latitude=41.0082&longitude=28.9784"
            "&current=temperature_2m,weathercode,windspeed_10m"
            "&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max"
            "&timezone=Europe/Istanbul&forecast_days=5"
        )
        r = requests.get(url, timeout=10).json()
        wmo = {
            0: "Acik", 1: "Az bulutlu", 2: "Parcali bulutlu", 3: "Bulutlu",
            61: "Yagmur", 63: "Kuvvetli yagmur", 80: "Saganak", 95: "Firtina"
        }
        gun = ["Pzt", "Sal", "Car", "Per", "Cum", "Cmt", "Paz"]
        d = r["daily"]
        c = r["current"]
        satirlar = []
        for i in range(5):
            dt = datetime.strptime(d["time"][i], "%Y-%m-%d")
            g = gun[dt.weekday()]
            mn = str(round(d["temperature_2m_min"][i]))
            mx = str(round(d["temperature_2m_max"][i]))
            yg = str(d["precipitation_probability_max"][i])
            satirlar.append("  " + g + ": " + mn + "/" + mx + "C  %" + yg)
        durum = wmo.get(c["weathercode"], "Bulutlu")
        sicak = str(round(c["temperature_2m"]))
        msg = "ISTANBUL HAVA DURUMU\n"
        msg += "Su an: " + sicak + "C - " + durum + "\n\n"
        msg += "\n".join(satirlar)
        return msg
    except Exception as e:
        return "Hava alinamadi: " + str(e)


def haberler():
    gl = [
        "Meta Manus AI Ads Manager ve Instagrama entegre etti - SocialBee",
        "ChatGPT reklam kanali self-serve erisime acildi - Verkeer",
        "Google Mart 2026 core update tamamlandi - ALM Corp",
        "Instagram paylasim sinyali begeni onune gecti - Social Media Today",
        "ABD influencer ekonomisi 2026 44 milyar dolara ulasacak - Marketing Dive"
    ]
    tr = [
        "Brandverse Awards 2026 yeni kategori Influencer Creator Is Birligi",
        "Meta Turkiye 6 ulkede reklamlara DSA vergisi ekledi",
        "LinkedIn Turkiye kullanici sayisi 20 milyonu gecti",
        "Instagram paylasim sayisi artik begenden once geliyor",
        "Google CMO Arama artik kesif yolculuguna donustu"
    ]
    msg = "5 YABANCI HABER\n\n"
    msg += "\n".join(["- " + x for x in gl])
    msg += "\n\n5 TURK HABER\n\n"
    msg += "\n".join(["- " + x for x in tr])
    return msg


def oneriler():
    gunler = {
        "Monday": "Pazartesi", "Tuesday": "Sali", "Wednesday": "Carsamba",
        "Thursday": "Persembe", "Friday": "Cuma",
        "Saturday": "Cumartesi", "Sunday": "Pazar"
    }
    gun = gunler.get(datetime.now(TZ).strftime("%A"), "Bugun")
    msg = gun + " ICERIK ONERILERI\n\n"
    msg += "Medya Ajansi:\n"
    msg += "  - Instagram: Trend konu + gorsel\n"
    msg += "  - Facebook: Sektor haberi\n\n"
    msg += "IQ Denetim:\n"
    msg += "  - LinkedIn: Mevzuat bilgi karti\n"
    msg += "  - Facebook: Haftalik finans notu"
    return msg


aylar = {
    "January": "Ocak", "February": "Subat", "March": "Mart",
    "April": "Nisan", "May": "Mayis", "June": "Haziran",
    "July": "Temmuz", "August": "Agustos", "September": "Eylul",
    "October": "Ekim", "November": "Kasim", "December": "Aralik"
}
gnler = {
    "Monday": "Pazartesi", "Tuesday": "Sali", "Wednesday": "Carsamba",
    "Thursday": "Persembe", "Friday": "Cuma",
    "Saturday": "Cumartesi", "Sunday": "Pazar"
}

now = datetime.now(TZ)
ay = aylar[now.strftime("%B")]
gn = gnler[now.strftime("%A")]
tarih = str(now.day) + " " + ay + " " + str(now.year) + ", " + gn

send("Gunaydin Dilara!\n" + tarih)
time.sleep(1)
send(hava())
time.sleep(1)
send(haberler())
time.sleep(1)
send(oneriler())
time.sleep(1)
send("Brief tamamlandi! Iyi calismalar!")
print("Brief: " + str(datetime.now()))
