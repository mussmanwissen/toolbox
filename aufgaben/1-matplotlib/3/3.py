from pylab import *

x,y = loadtxt("3.txt",unpack="true")

subplot(1,2,1)
plot(x,y,"r+")
xlabel("$x$")
ylabel("$y$")
subplot(1,2,2)
plot(x,y, "r+")
yscale("log")
xlabel("$x$")
ylabel("$y$")
show()
