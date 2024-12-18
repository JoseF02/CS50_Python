def main():
    #Ask the user for the Mass(m)
    m = int(input("m: "))
    e = einsteinCalc(m)
    print(e)

def einsteinCalc(m):
    #Apply the Einstein formula
    return m*(300000000**2)

main()

