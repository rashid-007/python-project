from django.shortcuts import render

# Create your views here.
def MoviesInfo(request):
    my_dict={
        'head_msg': 'Movies Information.',
        'sub_msg1': 'Sonali getting cured slowly.',
        'sub_msg2': 'Bahubali-3 is just being planned.',
        'sub_msg3': 'Salman Khan ready to marry.',
    }
    return render(request,'news.html',context=my_dict)
def SportsInfo(request):
    my_dict={
        'head_msg':'Sports Information',
        'sub_msg1':'Anushka Sharma firing like anything',
        'sub_msg2':'Kohli updating in game, anything can happen',
        'sub_msg3':'Worst performance by India-Sehwag'
    }
    return render(request,'news.html',context=my_dict)
def PoliticsInfo(request):
    my_dict={
        'head_msg': 'Politics Information',
        'sub_msg1': 'Achhe din aa gaye',
        'sub_msg2': 'rupee value now $1:70rs',
        'sub_msg3': 'In India single paisa black money no more'
    }
    return render(request,'news.html',context=my_dict)
def index(request):
    return render(request,'index.html')