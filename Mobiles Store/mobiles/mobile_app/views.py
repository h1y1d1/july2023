from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from mobile_app.models import Useradd,Contact
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def home(request):
    return render(request,"base.html")

def products(request):
    return render(request,"products.html")





#1
#HONOR
response=requests.get("https://www.flipkart.com/search?q=honor%20mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist1=zip(name,
price,
rate,
image,
link
)



def honor(request):
    return render(request,"honor.html",{'mylist1':mylist1})

#2
#REDMI
response=requests.get("https://www.flipkart.com/search?q=redmi+mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_9_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_9_na_na_ps&as-pos=2&as-type=RECENT&suggestionId=redmi+mobile%7CMobiles&requestId=db13d847-ce69-456b-91d6-8b0943cccfc0&as-searchtext=redmi%20mob")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist2=zip(name,
price,
rate,
image,
link
)

def redmi(request):
    return render(request,"redmi.html",{'mylist2':mylist2})

# mobiles_rating=pandas.DataFrame()
# mobiles_rating['Ratings']=Rating
# print(mobiles_rating)
# mobiles_rating.to_csv('moblies_rating.csv')


#3
#OPPO
response=requests.get("https://www.flipkart.com/search?q=realme%20mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist3=zip(name,
price,
rate,
image,
link
)

def oppo(request):
    return render(request,"oppo.html",{"mylist3":mylist3})


#4
#SAMSUNG
response=requests.get("https://www.flipkart.com/search?q=samsung%20mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist4=zip(name,
price,
rate,
image,
link
)


def samsung(request):
    return render(request,"samsung.html",{'mylist4':mylist4})

#5
# VIVO
response=requests.get("https://www.flipkart.com/search?q=vivo%20mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist5=zip(name,
price,
rate,
image,
link
)

def vivo(request):
    return render(request,"vivo.html",{'mylist5':mylist5})

#6
#REALME

response=requests.get("https://www.flipkart.com/search?q=realme%20mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist6=zip(name,
rate,
price,
image,
link
)

def realme(request):
    return render(request,"realme.html",{'mylist6':mylist6})


#7
#POCO

response=requests.get("https://www.flipkart.com/search?q=pocomobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist7=zip(name,
rate,
price,
image,
link
)

def poco(request):
    return render(request,"poco.html",{'mylist7':mylist7})

#8
#IQOO

response=requests.get("https://www.flipkart.com/search?q=iqoo%20mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist8=zip(name,
rate,
price,
image,
link
)

def iqoo(request):
    return render(request,"iqoo.html",{'mylist8':mylist8})

#9
#ONE_PLUS

response=requests.get("https://www.flipkart.com/search?q=one+plus+mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=one+plus+mobile%7CMobiles&requestId=734bcf9f-5404-4760-baa3-a64f909bad0b&as-searchtext=one%20mobile")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist9=zip(name,
rate,
price,
image,
link
)

def oneplus(request):
    return render(request,"oneplus.html",{'mylist9':mylist9})

#10
#LENOVO

response=requests.get("https://www.flipkart.com/search?q=lenovo%20%20mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist10=zip(name,
rate,
price,
image,
link
)

def lenovo(request):
    return render(request,"lenovo.html",{'mylist10':mylist10})

#11
#NOKIA

response=requests.get("https://www.flipkart.com/search?q=nokia%20smart%20mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist11=zip(name,
rate,
price,
image,
link
)

def nokia(request):
    return render(request,"nokia.html",{'mylist11':mylist11})


#12
#HUAWEI

response=requests.get("https://www.flipkart.com/search?q=huawei+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_12_sc_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_12_sc_na_na&as-pos=1&as-type=RECENT&suggestionId=huawei+mobiles%7CMobiles&requestId=6816feb6-3a7f-49e4-933b-846502cedf34&as-backfill=on")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist12=zip(name,
rate,
price,
image,
link
)

def huawei(request):
    return render(request,"huawei.html",{'mylist12':mylist12})


def login_user(request):
    if request.method=="POST":
        username=request.POST.get("username")# read 
        password=request.POST.get("password")# read
        user= authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
        return redirect("home")
    return render(request,"login.html")




def register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        email=request.POST.get("email")
        c = User.objects.create_user(username=username,email=email,password=password)
        c.save()
        return redirect("login")
    
    return render(request,"register.html")



def logout_user(request):
    logout(request)
    return redirect("login")




def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        


        c=Contact(name=name,email=email,message=message)
        c.save()
        return redirect("home")

    return render(request,"contact.html")

       