
import numpy
import matplotlib.pyplot
import glob

print('Analyse My Data')

#----------------------------------------------------------
def analyse(filename):
    '''
    here is the documentation string for analyse() it is useful
    '''
    data = numpy.loadtxt(fname=filename, delimiter=',')

    fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

    # make three spots for graphs to go into
    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(numpy.mean(data, axis=0))

    axes2.set_ylabel('max')
    axes2.plot(numpy.max(data, axis=0))

    axes3.set_ylabel('min')
    axes3.plot(numpy.min(data, axis=0))

    fig.tight_layout()
    matplotlib.pyplot.show()
#----------------------------------------------------------
def detect_problems(filename):

    data = numpy.loadtxt(fname=filename, delimiter=',')

    if numpy.max(data, axis=0)[0] == 0 and numpy.max(data, axis=0)[20] == 20:
        print('Suspicious looking maxima!')
    elif numpy.sum(numpy.min(data, axis=0)) == 0:
        print('Minima add up to zero!')
    else:
        print('Seems OK!')
#----------------------------------------------------------
def centre(data, desired=0):
    're-centres data around the desired value'
    return (data - numpy.mean(data)) + desired
#----------------------------------------------------------

#z = numpy.zeros((2,2))
#z[0,0] = 4
#print(z)
#print(centre(z,3))

filenames = glob.glob('../data/inflammation-*.csv')

for file in filenames[:3]:
    print(file)
    detect_problems(file)
    analyse(file)


#detect_problems('../data/inflammation-02.csv')
#analyse('../data/inflammation-02.csv')




