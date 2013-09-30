from pylab import *

t = linspace(0,1)
plot(t,t**2)
xlim(0,1)
xlabel("$x$")
ylabel("$x^2$")
savefig("lsg.pdf")
