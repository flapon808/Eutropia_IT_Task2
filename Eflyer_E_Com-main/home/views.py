from django.shortcuts import render
from itertools import zip_longest
from .models import T_shirt_Cloths,Shirt_Cloths,Women_Cloths,Laptop,Mobile,Computer,Jumkas,Kangans,Necklaces



def index(request):

    #Jewellery Data  fetching from  model
    jumka=Jumkas.objects.all()
    kangan=Kangans.objects.all()
    Necklace=Necklaces.objects.all()

    #Electronics Data  fetching from  model
    computer= Computer.objects.all()
    laptop =Laptop.objects.all()
    mobile = Mobile.objects.all()

    #Clothes Data  fetching from  model
    tcloths =T_shirt_Cloths.objects.all()
    wcloths =Women_Cloths.objects.all()   #here TCloths means Tshirt cloth, SCloths means Shirt cloth, WCloths means Women cloth   
    scloths =Shirt_Cloths.objects.all()                


    fashion = zip_longest(tcloths, scloths,wcloths)
    fashion1 = zip_longest(tcloths, scloths,wcloths)
    electronics=zip_longest(laptop,mobile,computer)
    electronics1=zip_longest(laptop,mobile,computer)
    Jewellery =zip_longest(jumka,Necklace,kangan)
    Jewellery1 =zip_longest(jumka,Necklace,kangan)

    context = {
        "fashion":fashion,
        "fashion1":fashion1,
        "electronics":electronics,
        "electronics1":electronics1,
        "Jewellery":Jewellery,
        "Jewellery1":Jewellery1 

    }
    return render(request, 'index.html', context=context)

