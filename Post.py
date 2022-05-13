def pop_solver(dominos,liczba_elementow,iteracje):
    rozwiazania = []
    for i in range(liczba_elementow):
        wi = dominos[i][0]
        xi = dominos[i][1]
        if (wi == xi):
            return dominos[i]
        if (len(wi) < len(xi)):
            if (xi[:len(wi)] == wi):
                rozwiazania.append([dominos[i]])
        if (len(xi) < len(wi)):
            if (wi[:len(xi)] == xi):
                rozwiazania.append([dominos[i]])
    for i in range(iteracje):
        nowe_rozwiazania = []
        for rozw in rozwiazania:
            for j in range(liczba_elementow):
                new_rozw = list(rozw)
                new_rozw.append([dominos[j][0], dominos[j][1]])
                wlist = ""
                xlist = ""
                for domino in new_rozw:
                    wlist += domino[0]
                    xlist += domino[1]
                if(len(wlist) == len(xlist)):
                    if (wlist == xlist):
                        nowe_rozwiazania += [new_rozw]
                if (len(wlist) < len(xlist)):
                    if (xlist[:len(wlist)] == wlist):
                        nowe_rozwiazania += [new_rozw]
                if (len(xlist) < len(wlist)):
                    if (wlist[:len(xlist)] == xlist):
                        nowe_rozwiazania += [new_rozw]
        if (nowe_rozwiazania == []):
            return []
        wlength = 0
        xlength = 0
        for rozw in nowe_rozwiazania:
            wlength = 0
            xlength = 0
            for domino in rozw:
                wlength += len(domino[0])
                xlength += len(domino[1])
            if (wlength == xlength):
                return rozw
        rozwiazania = list(nowe_rozwiazania)
    return []
if __name__=="__main__":
    print("Program rozwiazujacy Problem odpowiedzialnosci Posta")
    print("--------------------------------------------------------------------------------------")
    liczba_elementow=int(input("Prosze podac z ilu lancuchow beda skladac sie listy A i B:"))
    print("--------------------------------------------------------------------------------------")
    listaA=[]
    for i in range(liczba_elementow):
        listaA.append(str(input("Prosze podac "+str(i+1)+" lancuch listy A:")))
        print("--------------------------------------------------------------------------------------")
    print("Wprowadzono nastepujaca liste A:"+str(listaA))
    print("\nZakonczono wpisywanie lancuchow liczby A\n")
    print("--------------------------------------------------------------------------------------")
    listaB=[]
    for i in range(liczba_elementow):
        listaB.append(str(input("Prosze podac "+str(i+1)+" lancuch listy B:")))
        print("--------------------------------------------------------------------------------------")
    print("Wprowadzono nastepujaca liste B:"+str(listaB))
    print("\nZakonczono wpisywanie lancuchow liczby B\n")
    print("--------------------------------------------------------------------------------------")
    jak=int(input("Jesli program ma szukac rozwiazania POP automatycznie prosze wcisnac 1(w przeciwnym przypadku program poprosi o manualne dobieranie indeksow):"))
    if(jak==1):
        print("--------------------------------------------------------------------------------------")
        iteracje=int(input("Prosze podac ilosc iteracji, ktora program ma wykonac w celu znalezienia rozwiazania POP(sugerowane 1000):"))
        print("--------------------------------------------------------------------------------------")
        dominium=[]
        for i in range(0,liczba_elementow,1):
            dominium.append([listaA[i],listaB[i]])
        rozwiazania=[]
        rozwiazania=pop_solver(dominium,liczba_elementow,iteracje)
        if(rozwiazania!=[]):
            indeksy=[]
            rozw=""
            for dom in rozwiazania:
                rozw+=dom[0]
                indeksy.append(dominium.index(dom)+1)
            print("W znalezionym rozwiazaniu POP zostaly uzyte nastepujace indeksy:"+str(indeksy))
            print("Rozwiazanie podanego POP: "+rozw)
            print("--------------------------------------------------------------------------------------")
            print("Koncze prace-znalazlem rozwiazanie")
        else:
            if(iteracje<=1000):
                print("Program nie znalzal rozwiazania dla POP-prosze sprobowac wiecej iteracji:(")
                print("Koncze prace")
            else:
                print("Podany POP nie ma rozwiazania:(")
                print("Koncze prace")
    else:
        print("--------------------------------------------------------------------------------------")
        print("Rozpoczynam szukanie manualne rozwiazania")
        print("--------------------------------------------------------------------------------------")
        znaleziony=0
        while(znaleziony==0):
            rozw=[]
            liczba=int(input("Prosze podac z ilu indeksow bedzie skladac sie rozwiazanie POP:"))
            print("--------------------------------------------------------------------------------------")
            ciagA=""
            ciagB=""
            print("--------------------------------------------------------------------------------------")
            for i in range (liczba):
                index=int(input("Prosze podac "+str(i+1)+" indeks:"))
                print("--------------------------------------------------------------------------------------")
                ciagA+=listaA[index-1]
                ciagB+=listaB[index-1]
                rozw.append(index)
            if(ciagA==ciagB):
                print("Wykrylem rozwiazanie dla podanego POP!")
                print("W znalezionym rozwiazaniu POP zostaly uzyte nastepujace indeksy:"+str(rozw))
                print("Rozwiazanie podanego POP: "+ciagA)
                print("--------------------------------------------------------------------------------------")
                print("Koncze prace-znalazlem rozwiazanie")
                znaleziony=1
            else:
                print("Podane indeksy nie sa rozwiazaniem dla danego POP")
                print("--------------------------------------------------------------------------------------")
                p=int(input("Jesli chcesz wyjsc z programu nacisnij 1:"))
                print("--------------------------------------------------------------------------------------")
                if(p==1):
                    print("--------------------------------------------------------------------------------------")
                    print("Koncze prace!")
                    znaleziony=1
