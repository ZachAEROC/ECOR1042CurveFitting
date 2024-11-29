import matplotlib.pyplot as plt
import numpy

def load_data(file: str) -> list[dict]:
    in_file = open(file, 'r')
    header = True
    data = []
    
    for line in in_file:

        if header:
            categories = line.strip().split(', ')
            header = False

        else:
            point = {}
            values = line.strip(' ').strip('\n').split(', ')

            for key_idx in range(len(categories)):
                point[categories[key_idx]] = float(values[key_idx])
                
            data.append(point)

    in_file.close()
    return data


def scatter_data(data) -> None:
    """
    Data in the form [{'Frequency(dec)': 0.03333, 'Gain(dB)': -0.00391}, ...]
    """
    x = []
    y = []
    
    for point in data:
        x.append(point['Frequency(dec)'])
        y.append(point['Gain(dB)'])

    return x, y
    

def poly(x, c) -> float:
    result = 0
    
    for i in range(len(c)):
        result += c[i] * x ** (len(c) - (i + 1))

    return result


def curve_fit(data, points: tuple, degree) -> list[int]:
    """
    Points: Lower included, Upper Discluded
    """
    
    x = []
    y = []
    
    for point in data:
        x.append(point['Frequency(dec)'])
        y.append(point['Gain(dB)'])

    x = x[points[0]: points[1]]
    y = y[points[0]: points[1]]
    c = list(numpy.polyfit(x, y, degree))

    x_e = numpy.linspace(x[0], x[-1], 50)
    y_e = []

    for x_ei in x_e:
        y_e.append(poly(x_ei, c))

    xscatter, yscatter = scatter_data(data)
    
    fig = plt.figure()
    plt.title('Bode plot for a low pass RC filter')
    plt.xlabel('Frequency(dec)')
    plt.ylabel('Gain(dB)')
    plt.scatter(xscatter, yscatter)
    plt.plot(x_e, y_e, 'r-')
    plt.show()

    return c
    
