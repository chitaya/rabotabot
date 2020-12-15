#made by mike mikulin
######################################################################################################


brandlist = ["пятерочка", "четверть", "один", "один", "два", "шесть"]
citylist = ["москва", "севастополь", "владивосток", "новосибирск", "пермь", "владивосток"]
positionlist = ["кассир", "менеджер", "шлюх", "попаверт", "кто-то", "шлюх"]
zplist = ["120", "120","120", "120","120", "120"]
phonelist = ["+7777777","+7777777","+7777777","+7777777","+7777777","+7777777",]
emaillist = ["lol@mail.ru","lol@mail.ru","lol@mail.ru","lol@mail.ru","lol@mail.ru","lol@mail.ru", ]
aplid = len(brandlist)

######################################################################################################

def add_apl(aplid, brand, city, position, zp, phone, email):
    apl = Apl( aplid, brand, city, position, zp, phone, email)
    apl.apl_info()
    brandlist.append(brand.lower())
    citylist.append(city.lower())
    positionlist.append(position.lower())
    zplist.append(zp.lower())
    phonelist.append(phone.lower())
    emaillist.append(email.lower())

######################################################################################################

def searchres(i):
    
    print("id - " , i,"|", "компания - " ,brandlist[i],"|","город - " ,citylist[i],"|","должность - " , positionlist[i],"|","зп - ",zplist[i], "тыш", "|","tel - " ,phonelist[i],"|","e-mail - ", emaillist[i])

######################################################################################################

class Apl:
    def __init__(self, aplid, brand, city, position, zp, phone, email):
        self.aplid = aplid
        self.brand = brand
        self.city = city
        self.position = position
        self.zp = zp
        self.phone = phone
        self.email = email

    def apl_info(self):
        print("id - " , self.aplid,"|", "компания - " , self.brand,"|","город - " , self.city,"|","должность - " , self.position,"|","зп - " , self.zp,"|","tel - " , self.phone,"|","e-mail - ", self.email)

########################################################################################################   

def adding(aplid):
    brand = str(input("ваша компания: "))
    city = str(input("город: "))
    position = str(input("должность: "))
    zp = str(input("зп (тыщ руб): "))
    phone = str(input("ваш номер :"))
    email = str(input("ваш e-mail: "))
    
  
    add_apl(aplid, brand, city, position, zp, phone, email)
         
######################################################################################################

while True:
    comand = str(input("введите команду: "))
    comand = comand.lower()
    if comand == "add":
        adding(aplid)
        aplid += 1
    
    else:
        print("найдено по запросу - {}:".format(comand))
        for i in range (len(brandlist)):
            if comand == brandlist[i]:
                searchres(i)
            elif comand == citylist[i]:
                searchres(i)
            elif comand == positionlist[i]:
                searchres(i)



######################################################################################################