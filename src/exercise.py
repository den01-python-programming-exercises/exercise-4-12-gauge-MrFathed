from gauge import Gauge

def main():
    #write your code below this line
    g = Gauge(0)

    while not g.full():
        print("Not full! Value: " + str(g.value))
        g.increase()

    print("Full! Value: " + str(g.value))
    g.decrease()
    print("Not full! Value: " + str(g.value))

if __name__ == '__main__':
    main()
