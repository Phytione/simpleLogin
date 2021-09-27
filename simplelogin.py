sayac=0;
kAd=input("Lütfen kullanıcı adınızı giriniz: ")
sifre=int(input("Lütfen şifrenizi giriniz: "))
print("**********************")
while(kAd=="mcihan" and sifre!="123456" or kAd!="mcihan" and sifre=="123456" or kAd!="mcihan" and sifre!="123456"):
    
    print("Yanlış şifre tekrar deneyiniz....")
    sayac+=1
    if sayac==3:
        print("Sistemden atıldın birader...")
        break;
    kAd=input("Lütfen kullanıcı adınızı giriniz: ")
    sifre=input("Lütfen şifrenizi giriniz: ")
    continue

  
    

    
    
    








