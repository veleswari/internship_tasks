from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Register

# Create your views here.

def home(request):
	return HttpResponse("Hi Good Evening to All")

def htmltag(req):
	return HttpResponse("<h2>Hi Welcome</h2>")

def usernameprint(request,uname):
	return HttpResponse("<h2>Hi good evening <span style='color:green'>{}</span></h2>".format(uname))

def usernameage(request,un,ag):
	return HttpResponse("<h3 style='text-align:center'>Hi User <span style='color:yellow'>{}</span> and your agae is: <span style='color:red'>{}</span></h3>".format(un,ag))

def empdetails(request,eid,ename,eage):
	return HttpResponse("<script>alert('Hi welcom {}')</script><h3>Hi Welcome {} and your age is: {} and your id:{}<h3>".format(ename,ename,eage,eid))

def htm(request):
	return render(request,'html/sample.html')

def ytname(request,name):
	return render(request,'html/ytname.html',{'n':name})

def empname(request,id,ename):
	k = {'i':id,'n':ename}
	return render(request,'html/ehtml.html',k)

def studentdetails(request):
	return render(request,'html/std.html')

def myform(req):
	if req.method == "POST":
		#print(req.POST)
		uname = req.POST['uname']
		rollno = req.POST['rollno']
		email = req.POST.get('email')
		#print(uname,rollno,email)
		data = {'username':uname,'rno':rollno,'emailId':email}
		return render(req, 'html/display.html',data)
	

	return render(req,'html/myform.html')

def task(requ):
	if requ.method == "POST":
		fname = requ.POST['fname']
		lname = requ.POST['lname']
		pno = requ.POST['pno']
		gender = requ.POST['gender']
		email = requ.POST['email']
		address = requ.POST['address']
		lang = requ.POST.getlist('check')

		data = {'fname':fname,'lname':lname,'pno':pno,'gender':gender,'email':email,'address':address,'lang':lang}
		return render(requ,'html/registered.html',data)

	return render(requ,'html/task.html')

def task2(requ):
	if requ.method == "POST":
		urname = requ.POST['urname']
		pasw = requ.POST['pasw']
		if urname == "asha" and pasw == "12as":
			return render(requ,'html/valid.html')
		else:
			return render(requ,'html/invalid.html')
	return render(requ,'html/task2.html')

def sampleboot(requ):
	return render(requ,'html/sampleboot.html')

def btregi(request):
	return render(request,'html/btregst.html')

def register1(request):
	#name ="siddu"
	#email = "siddu@gmail.com"
	reg  = Register(name ="siddu",email = "siddu@gmail.com")
	reg.save()
	return HttpResponse("data inserted successfully....")

def register2(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		reg = Register(name = name,email = email)
		reg.save()
		return HttpResponse("registered successfully")
	return render(request,"html/register2.html")

def display(request):
	data = Register.objects.all()
	return render(request,'html/display1.html',{'data':data})

def sview(request,y):
	w = Register.objects.get(id=y)
	return render(request,'html/sview.html',{'y':w})
	#return HttpResponse("Your name is: {}".format(w.name))

def supt(request,q):
	t = Register.objects.get(id=q)
	if request.method == "POST":
		na = request.POST['n']
		em = request.POST['e']
		t.name = na
		t.email = em
		t.save()
		return redirect('/display')
	return render(request,'html/supdate.html',{'p':t})

def sudl(request,p):
	b = Register.objects.get(id=p)
	if request.method == "POST":
		b.delete()
		return redirect('/display')
	return render(request,'html/sndtl.html',{'z':b})