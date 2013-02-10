import numpy
import pylab

select = 2

if select == 1:
    x = [0.5, 1, 2, 3, 4, 6, 8, 10, 15];
    y = [63.2, 58, 55.27, 53, 45.5, 41.7, 38.4, 29.8, 22];
    xl = 'Maximum Allowed Interrupt Rate (in KHz)'
    yl = 'Tx packet rate (in Kpps)'
    t = 'Tx packet rate as a function of the MAIR'

elif select == 2:
    x = [0.5, 1, 2, 3, 4, 6, 8, 9, 12, 15];
    y = [150, 182, 205, 185, 156, 110, 77, 59, 31, 14];
    xl = 'Maximum Allowed Interrupt Rate (in KHz)'
    yl = 'Rx critical rate (in Kpps)'
    t = 'Rx critical rate as a function of the MAIR'

pylab.plot(x,y)

pylab.xlabel(xl)
pylab.ylabel(yl)
pylab.title(t)
pylab.grid(True)
#pylab.savefig('simple_plot')
 
pylab.show()
