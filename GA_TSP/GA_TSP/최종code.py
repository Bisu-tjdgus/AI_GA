import math, random
import cv2
import csv
import time
import datetime

class City:
    def __init__(self,number=None, x=None, y=None):
        self.x = None
        self.y = None
        self.number =None
        if x is not None:
            self.x = x
        else:
            self.x = int(random.random() * 200)
        if y is not None:
            self.y = y
        else:
            self.y = int(random.random() * 200)
        if number is not None:
            self.number = number
        else:
            self.number = int(random.random() * 1000)

    def getX(self):
        return self.x

    def getNumber(self):
        return self.number
    def getY(self):
        return self.y

    def distanceTo(self, city):
        xDistance = abs(self.getX() - city.getX())
        yDistance = abs(self.getY() - city.getY())
        distance = math.sqrt((xDistance * xDistance) + (yDistance * yDistance))
        return distance

    def __repr__(self):                                         ## 도시 출력 방식 선택
        ##return str(self.getX()) + ", " + str(self.getY())     ## 좌표 출력
        return str(self.getNumber())                            ## 도시 번호 출력

class TourManager:
    destinationCities = []

    def addCity(self, city):
        self.destinationCities.append(city)

    def getCity(self, index):
        return self.destinationCities[index]

    def numberOfCities(self):
        return len(self.destinationCities)


class Tour:
    def __init__(self, tourmanager, tour=None):
        self.tourmanager = tourmanager
        self.tour = []
        self.fitness = 0.0
        self.distance = 0
        if tour is not None:
            self.tour = tour
        else:
            for i in range(0, self.tourmanager.numberOfCities()):
                self.tour.append(None)

    def __len__(self):
        return len(self.tour)

    def __getitem__(self, index):
        return self.tour[index]

    def __setitem__(self, key, value):
        self.tour[key] = value

    def __repr__(self):
        geneString = 'Start -> '
        for i in range(0, self.tourSize()):
            geneString += str(self.getCity(i)) + ' -> '
        geneString += 'End'
        return geneString

    def generateIndividual(self):
        for cityIndex in range(0, self.tourmanager.numberOfCities()):
            self.setCity(cityIndex, self.tourmanager.getCity(cityIndex))
        random.shuffle(self.tour)

    def getCity(self, tourPosition):
        return self.tour[tourPosition]

    def setCity(self, tourPosition, city):
        self.tour[tourPosition] = city
        self.fitness = 0.0
        self.distance = 0

    def getFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.getDistance())
        return self.fitness

    def getDistance(self):
        if self.distance == 0:
            tourDistance = 0
            for cityIndex in range(0, self.tourSize()):
                fromCity = self.getCity(cityIndex)
                destinationCity = None
                if cityIndex + 1 < self.tourSize():
                    destinationCity = self.getCity(cityIndex + 1)
                else:
                    destinationCity = self.getCity(0)
                tourDistance += fromCity.distanceTo(destinationCity)
            self.distance = tourDistance
        return self.distance

    def tourSize(self):
        return len(self.tour)

    def containsCity(self, city):
        return city in self.tour


class Population:
    def __init__(self, tourmanager, populationSize, initialise):
        self.tours = []
        for i in range(0, populationSize):
            self.tours.append(None)

        if initialise:
            for i in range(0, populationSize):
                newTour = Tour(tourmanager)
                newTour.generateIndividual()
                self.saveTour(i, newTour)

    def __setitem__(self, key, value):
        self.tours[key] = value

    def __getitem__(self, index):
        return self.tours[index]

    def saveTour(self, index, tour):
        self.tours[index] = tour

    def getTour(self, index):
        return self.tours[index]

    def getFittest(self):
        fittest = self.tours[0]
        for i in range(0, self.populationSize()):
            if fittest.getFitness() <= self.getTour(i).getFitness():
                fittest = self.getTour(i)
        return fittest

    def getFittest2(self):
        fittest = self.tours[0]
        max = self.getFittest().getFitness()
        for i in range(0, self.populationSize()):
            if (max - fittest.getFitness()) >= (max - self.getTour(i).getFitness()) > 0:
                fittest = self.getTour(i)
        return fittest

    def getFittest3(self):
        fittest = self.tours[0]
        max = self.getFittest2().getFitness()
        for i in range(0, self.populationSize()):
            if (max - fittest.getFitness()) >= (max - self.getTour(i).getFitness()) > 0:
                fittest = self.getTour(i)
        return fittest

    def getFittest4(self):
        fittest = self.tours[0]
        max = self.getFittest3().getFitness()
        for i in range(0, self.populationSize()):
            if (max - fittest.getFitness()) >= (max - self.getTour(i).getFitness()) > 0:
                fittest = self.getTour(i)
        return fittest

    def getFittest5(self):
        fittest = self.tours[0]
        max = self.getFittest4().getFitness()
        for i in range(0, self.populationSize()):
            if (max - fittest.getFitness()) >= (max - self.getTour(i).getFitness()) > 0:
                fittest = self.getTour(i)
        return fittest

    def getFittest6(self):
        fittest = self.tours[0]
        max = self.getFittest5().getFitness()
        for i in range(0, self.populationSize()):
            if (max - fittest.getFitness()) >= (max - self.getTour(i).getFitness()) > 0:
                fittest = self.getTour(i)
        return fittest

    def getFittest7(self):
        fittest = self.tours[0]
        max = self.getFittest6().getFitness()
        for i in range(0, self.populationSize()):
            if (max - fittest.getFitness()) >= (max - self.getTour(i).getFitness()) > 0:
                fittest = self.getTour(i)
        return fittest

    def getFittest8(self):
        fittest = self.tours[0]
        max = self.getFittest7().getFitness()
        for i in range(0, self.populationSize()):
            if (max - fittest.getFitness()) >= (max - self.getTour(i).getFitness()) > 0:
                fittest = self.getTour(i)
        return fittest

    def getFittest9(self):
        fittest = self.tours[0]
        max = self.getFittest8().getFitness()
        for i in range(0, self.populationSize()):
            if (max - fittest.getFitness()) >= (max - self.getTour(i).getFitness()) > 0:
                fittest = self.getTour(i)
        return fittest

    def getFittest10(self):
        fittest = self.tours[0]
        max = self.getFittest9().getFitness()
        for i in range(0, self.populationSize()):
            if (max - fittest.getFitness()) >= (max - self.getTour(i).getFitness()) > 0:
                fittest = self.getTour(i)
        return fittest


    def populationSize(self):
        return len(self.tours)

                                     ##mutaion확률, tornament 크기, eltisim 갯수 선택
class GA:
    def __init__(self, tourmanager, mutationRate=0.025, tournamentSize=8, elitism=3):
        self.tourmanager = tourmanager
        self.mutationRate = mutationRate
        self.tournamentSize = tournamentSize
        self.elitism = elitism

    def evolvePopulation(self, pop):
        newPopulation = Population(self.tourmanager, pop.populationSize(), False)
        elitismOffset = 0
        if self.elitism > 0:
            if self.elitism == 1:
                newPopulation.saveTour(elitismOffset, pop.getFittest())
                elitismOffset = 1
            elif self.elitism == 2:
                newPopulation.saveTour(elitismOffset, pop.getFittest())
                elitismOffset = 1
                newPopulation.saveTour(elitismOffset, pop.getFittest2())
                elitismOffset = 2
            elif self.elitism == 3:
                newPopulation.saveTour(elitismOffset, pop.getFittest())
                elitismOffset = 1
                newPopulation.saveTour(elitismOffset, pop.getFittest2())
                elitismOffset = 2
                newPopulation.saveTour(elitismOffset, pop.getFittest3())
                elitismOffset = 3
            elif self.elitism == 4:
                newPopulation.saveTour(elitismOffset, pop.getFittest())
                elitismOffset = 1
                newPopulation.saveTour(elitismOffset, pop.getFittest2())
                elitismOffset = 2
                newPopulation.saveTour(elitismOffset, pop.getFittest3())
                elitismOffset = 3
                newPopulation.saveTour(elitismOffset, pop.getFittest4())
                elitismOffset = 4
            elif self.elitism == 5:
                newPopulation.saveTour(elitismOffset, pop.getFittest())
                elitismOffset = 1
                newPopulation.saveTour(elitismOffset, pop.getFittest2())
                elitismOffset = 2
                newPopulation.saveTour(elitismOffset, pop.getFittest3())
                elitismOffset = 3
                newPopulation.saveTour(elitismOffset, pop.getFittest4())
                elitismOffset = 4
                newPopulation.saveTour(elitismOffset, pop.getFittest5())
                elitismOffset = 5
            elif self.elitism == 6:
                newPopulation.saveTour(elitismOffset, pop.getFittest())
                elitismOffset = 1
                newPopulation.saveTour(elitismOffset, pop.getFittest2())
                elitismOffset = 2
                newPopulation.saveTour(elitismOffset, pop.getFittest3())
                elitismOffset = 3
                newPopulation.saveTour(elitismOffset, pop.getFittest4())
                elitismOffset = 4
                newPopulation.saveTour(elitismOffset, pop.getFittest5())
                elitismOffset = 5
                newPopulation.saveTour(elitismOffset, pop.getFittest6())
                elitismOffset = 6
            elif self.elitism == 7:
                newPopulation.saveTour(elitismOffset, pop.getFittest())
                elitismOffset = 1
                newPopulation.saveTour(elitismOffset, pop.getFittest2())
                elitismOffset = 2
                newPopulation.saveTour(elitismOffset, pop.getFittest3())
                elitismOffset = 3
                newPopulation.saveTour(elitismOffset, pop.getFittest4())
                elitismOffset = 4
                newPopulation.saveTour(elitismOffset, pop.getFittest5())
                elitismOffset = 5
                newPopulation.saveTour(elitismOffset, pop.getFittest6())
                elitismOffset = 6
                newPopulation.saveTour(elitismOffset, pop.getFittest7())
                elitismOffset = 7
            elif self.elitism == 8:
                newPopulation.saveTour(elitismOffset, pop.getFittest())
                elitismOffset = 1
                newPopulation.saveTour(elitismOffset, pop.getFittest2())
                elitismOffset = 2
                newPopulation.saveTour(elitismOffset, pop.getFittest3())
                elitismOffset = 3
                newPopulation.saveTour(elitismOffset, pop.getFittest4())
                elitismOffset = 4
                newPopulation.saveTour(elitismOffset, pop.getFittest5())
                elitismOffset = 5
                newPopulation.saveTour(elitismOffset, pop.getFittest6())
                elitismOffset = 6
                newPopulation.saveTour(elitismOffset, pop.getFittest7())
                elitismOffset = 7
                newPopulation.saveTour(elitismOffset, pop.getFittest8())
                elitismOffset = 8
            elif self.elitism == 9:
                newPopulation.saveTour(elitismOffset, pop.getFittest())
                elitismOffset = 1
                newPopulation.saveTour(elitismOffset, pop.getFittest2())
                elitismOffset = 2
                newPopulation.saveTour(elitismOffset, pop.getFittest3())
                elitismOffset = 3
                newPopulation.saveTour(elitismOffset, pop.getFittest4())
                elitismOffset = 4
                newPopulation.saveTour(elitismOffset, pop.getFittest5())
                elitismOffset = 5
                newPopulation.saveTour(elitismOffset, pop.getFittest6())
                elitismOffset = 6
                newPopulation.saveTour(elitismOffset, pop.getFittest7())
                elitismOffset = 7
                newPopulation.saveTour(elitismOffset, pop.getFittest8())
                elitismOffset = 8
                newPopulation.saveTour(elitismOffset, pop.getFittest9())
                elitismOffset = 9
            else:
                newPopulation.saveTour(elitismOffset, pop.getFittest())
                elitismOffset = 1
                newPopulation.saveTour(elitismOffset, pop.getFittest2())
                elitismOffset = 2
                newPopulation.saveTour(elitismOffset, pop.getFittest3())
                elitismOffset = 3
                newPopulation.saveTour(elitismOffset, pop.getFittest4())
                elitismOffset = 4
                newPopulation.saveTour(elitismOffset, pop.getFittest5())
                elitismOffset = 5
                newPopulation.saveTour(elitismOffset, pop.getFittest6())
                elitismOffset = 6
                newPopulation.saveTour(elitismOffset, pop.getFittest7())
                elitismOffset = 7
                newPopulation.saveTour(elitismOffset, pop.getFittest8())
                elitismOffset = 8
                newPopulation.saveTour(elitismOffset, pop.getFittest9())
                elitismOffset = 9
                newPopulation.saveTour(elitismOffset, pop.getFittest10())
                elitismOffset = 10


        for i in range(elitismOffset, newPopulation.populationSize()):
            parent1 = self.tournamentSelection(pop)
            parent2 = self.tournamentSelection(pop)
            child = self.crossover2(parent1, parent2)                       ##crossover방식 1,2,3 중 선택
            newPopulation.saveTour(i, child)

        for i in range(elitismOffset, newPopulation.populationSize()):
            self.mutate(newPopulation.getTour(i))

        return newPopulation

    def crossover1(self, parent1, parent2):                                  ##3분할 crossover
        child = Tour(self.tourmanager)

        startPos = int(random.random() * parent1.tourSize())
        endPos = int(random.random() * parent1.tourSize())

        for i in range(0, child.tourSize()):
            if startPos < endPos and i > startPos and i < endPos:
                child.setCity(i, parent1.getCity(i))
            elif startPos > endPos:
                if not (i < startPos and i > endPos):
                    child.setCity(i, parent1.getCity(i))

        for i in range(0, parent2.tourSize()):
            if not child.containsCity(parent2.getCity(i)):
                for ii in range(0, child.tourSize()):
                    if child.getCity(ii) == None:
                        child.setCity(ii, parent2.getCity(i))
                        break
        return child

    def crossover2(self, parent1, parent2, ):                           ##11분할 crossover
        child = Tour(self.tourmanager)

        my_lst = list(random.sample(range(1, 100), 10))
        my_lst.sort()

        for i in range(0, child.tourSize()):
            if i < my_lst[0]:
                child.setCity(i, parent1.getCity(i))

            elif my_lst[1] <= i < my_lst[2]:
                child.setCity(i, parent1.getCity(i))

            elif my_lst[3] <= i < my_lst[4]:
                child.setCity(i, parent1.getCity(i))

            elif my_lst[5] <= i < my_lst[6]:
                child.setCity(i, parent1.getCity(i))

            elif my_lst[7] <= i < my_lst[8]:
                child.setCity(i, parent1.getCity(i))

            elif my_lst[9] <= i:
                child.setCity(i, parent1.getCity(i))

        for i in range(0, parent2.tourSize()):
            if not child.containsCity(parent2.getCity(i)):
                for ii in range(0, child.tourSize()):
                    if child.getCity(ii) == None:
                        child.setCity(ii, parent2.getCity(i))
                        break

    def crossover3(self, parent1, parent2):                              ## order crossover(순서 교차)
        child = Tour(self.tourmanager)

        startPos = int(random.random() * parent1.tourSize())
        endPos = int(random.random() * parent1.tourSize())

        for i in range(0, child.tourSize()):
            if startPos < endPos and i > startPos and i < endPos:
                child.setCity(i, parent1.getCity(i))
            elif startPos > endPos:
                if not (i < startPos and i > endPos):
                    child.setCity(i, parent1.getCity(i))

        for i in range(0, parent2.tourSize()):
            i2 = i + endPos
            if (i2 >= parent2.tourSize()):
                i2 = i2 - parent2.tourSize()
            if not child.containsCity(parent2.getCity(i2)):
                for ii in range(0, child.tourSize()):
                    ii = ii + i2
                    if (ii >= child.tourSize()):
                        ii = ii - child.tourSize()
                    if child.getCity(ii) == None:
                        child.setCity(ii, parent2.getCity(i2))
                        break



    def mutate(self, tour):
        for tourPos1 in range(0, tour.tourSize()):
            if random.random() < self.mutationRate:
                tourPos2 = int(tour.tourSize() * random.random())

                city1 = tour.getCity(tourPos1)
                city2 = tour.getCity(tourPos2)

                tour.setCity(tourPos2, city1)
                tour.setCity(tourPos1, city2)

    def tournamentSelection(self, pop):
        tournament = Population(self.tourmanager, self.tournamentSize, False)
        for i in range(0, self.tournamentSize):
            randomId = int(random.random() * pop.populationSize())
            tournament.saveTour(i, pop.getTour(randomId))
        fittest = tournament.getFittest()
        return fittest


if __name__ == '__main__':
    n_cities = 1000
    population_size = 10                                               ##population 수 선택
    n_generations = 1000                                                ##세대 수 선택

    f = open("TSP.csv", "r")
    reader= csv.reader(f)
    # Load the map
    map_original = cv2.imread('map.jpg')

    # Setup cities and tour
    tourmanager = TourManager()

    cites_number =0
    for line in reader:
        x = float(line[0])
        y = float(line[1])

        print(x)
        print(y,"\n")

        tourmanager.addCity(City(number=cites_number,x=x, y=y))
        cv2.circle(map_original, center=(int(9*x), int(9*y)), radius=1, color=(0, 0, 255), thickness=-1, lineType=cv2.LINE_AA)
        cites_number=cites_number+1

    cv2.imshow('map', map_original)
    cv2.waitKey(0)

    # Initialize population
    print("pop 시작!")
    starttime = time.time()
    pop = Population(tourmanager, populationSize=population_size, initialise=True)
    print("Initial distance: " + str(pop.getFittest().getDistance()))

    # Evolve population
    ga = GA(tourmanager)

    for i in range(n_generations):

        pop = ga.evolvePopulation(pop)

        fittest = pop.getFittest()

        map_result = map_original.copy()

        for j in range(1, n_cities):
            cv2.line(
                map_result,
                pt1=(int(9*fittest[j - 1].x), int(9*fittest[j - 1].y)),
                pt2=(int(9*fittest[j].x), int(9*fittest[j].y)),
                color=(((i%2))*200, 0, ((i+1)%2)*200),
                thickness=1,
                lineType=cv2.LINE_AA
            )
        cv2.line(
            map_result,
            pt1=(int(9 * fittest[99].x), int(9 * fittest[99].y)),
            pt2=(int(9 * fittest[0].x), int(9 * fittest[0].y)),
            color=(((i % 2)) * 200, 0, ((i + 1) % 2) * 200),
            thickness=1,
            lineType=cv2.LINE_AA
        )

        cv2.putText(map_result, org=(10, 920), text='Generation: %d' % (i + 1), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.7, color=0, thickness=1, lineType=cv2.LINE_AA)
        cv2.putText(map_result, org=(10, 950), text='Distance: %.2f' % fittest.getDistance(),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.7, color=0, thickness=1, lineType=cv2.LINE_AA)
        cv2.putText(map_result, org=(750, 920), text='Group 3',
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=0, thickness=1, lineType=cv2.LINE_AA)
        currenttime = time.time()
        sec = currenttime - starttime
        times = str(datetime.timedelta(seconds=sec)).split(".")
        cv2.putText(map_result, org=(10, 980), text='Time: %s' %times, fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.7, color=0, thickness=1, lineType=cv2.LINE_AA)
        cv2.imshow('map', map_result)
        if cv2.waitKey(100) == ord('q'):
            break

        if i%50 == 0:
            print(i, "번째 세대 : cost : %d" % fittest.getDistance())

    # Print final results
    print("Finished")
    print("Final distance: " + str(pop.getFittest().getDistance()))
    endtime = time.time()
    sec = endtime - starttime
    times = str(datetime.timedelta(seconds=sec)).split(".")
    times = times[0]
    print("Time : " + times)
    print("Solution:")
    print(pop.getFittest())

    cv2.waitKey(0)