from django.shortcuts import render
from django.shortcuts import HttpResponse
def aboutpage (request):
		#return HttpResponse('hi!im sina')
		return render(request,'about.html')


def homepage(request):
	 #return HttpResponse('wellcome!!')
	 return render(request,'home.html')
