# I have create this file first.
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import BadHeaderError, EmailMessage

def index(request):
	parms = {"name":"Ashish", "place": "India"}
	return render(request, "index.html", parms)
 	# return HttpResponse("<h1>Home Page will be publish soon.</h1>")

def about(request):
	return render(request, "about.html")

def contact(request):
	return render(request, "contact.html")

def remove_punc(request, text):
	punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
	analyzed_text = ""
	for char in text:
		if char not in punctuations:
			analyzed_text = analyzed_text + char

	parms = {"purpose": "Remove Punctuation", "analyzed_text": analyzed_text }
	return render(request, "analyze.html", parms)

def Capatalize(request, text):
	analyzed_text = ""
	for char in text:
		analyzed_text = analyzed_text + char.upper()

	parms = {"purpose": "Capatalize", "analyzed_text": analyzed_text }
	return render(request, "analyze.html", parms)

def new_line_remove(request, text):
	analyzed_text = ""
	for char in text:
		analyzed_text = analyzed_text + char

	parms = {"purpose": "New Line Remove", "analyzed_text": analyzed_text }
	return render(request, "analyze.html", parms)

def char_counter(request, text):
	analyzed_text = 0
	for char in text:
		analyzed_text = analyzed_text + 1
	parms = {"purpose": "Number of Characters", "analyzed_text": analyzed_text }
	return render(request, "analyze.html", parms)

def analyze(request):
	text = request.POST.get("string", "")
	purpose = request.POST.get("purpose", None)

	if purpose == "remove_punc":
		return remove_punc(request, text)
	elif purpose == "fullcaps":
		return Capatalize(request, text)
	elif purpose == "new_line_remover":
		return new_line_remove(request, text)
	elif purpose == "no_of_char":
		return char_counter(request, text)
	else:
		return HttpResponse('''<b>Something went wrong.</b><br><a href="/" style="float: right;">go to previous page</a>''')

def send_msg(request):
	name = request.POST.get("txtName", "")
	email = request.POST.get("txtEmail", None)
	phone = request.POST.get("txtPhone", None)
	msg = request.POST.get("txtMsg", None)
	result = '''<h1>Dear Ashish </h1>'''+ name + ''' has been submitted following details:- <br>'''
	result = result + "<b>Name :</b> "+ name +"<br>"
	result = result + "<b>Email :</b> "+ email +"<br>"
	result = result + "<b>Phone :</b> "+ phone +"<br>"
	result = result + "<b>Message :</b> "+ msg +"<br><br><br>"
	result = result + "<b>Thanks & Regards</b><br>"
	result = result + "Text Utils Team<br>"

	subject ="Contact Submitted"
	from_email = "sender@gmail.com"

	try:
		email = EmailMessage(subject, result, from_email, ['reciever@gmail.com'])
		email.content_subtype = "html"
		res = email.send()
		#send_mail(subject, result, from_email, ['reciever@gmail.com'])
	except BadHeaderError:
		return HttpResponse('Invalid header found.')
	return HttpResponse('''Information submitted successfully!<br><a href="/contact">go back</a>''')