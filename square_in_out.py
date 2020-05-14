import turtle

t = turtle.Turtle() 

def sqrfunc(size): 
	for i in range(4): 
		t.fd(size) 
		t.left(90) 
		size = size + 5

sqrfunc(6) 
sqrfunc(26) 
sqrfunc(46)
sqrfunc(66) 
sqrfunc(86) 
sqrfunc(106) 
sqrfunc(126) 
sqrfunc(146)

t.goto(80, 80)
t.goto(80, -80)
t.goto(-80, -80)
t.goto(-80, 80)
t.goto(80, -80)

turtle.done()
