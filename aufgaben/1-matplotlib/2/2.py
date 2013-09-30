from pylab import *
x= linspace(0,1)
plot(x,x**2,"b-",label=r"$x^2$")
plot(x,x**5,"gx", label=r"$x^5$")
xlabel("$x$")
legend(loc="best")
show()
