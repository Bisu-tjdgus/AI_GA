import math, random
import cv2
import csv
import time
import datetime

greedy_city = [964, 512, 926, 341, 970, 555, 676, 776, 204, 39, 369,
                   384, 682, 984, 678, 48, 722, 186, 613, 176, 248, 321,
                   998, 340, 44, 163, 536, 42, 668, 385, 232, 287, 41,
                   211, 695, 714, 835, 660, 247, 643, 392, 567, 174, 763,
                   252, 257, 178, 527, 223, 710, 742, 539, 217, 632, 281,
                   272, 10, 648, 893, 989, 586, 707, 418, 851, 417, 103,
                   627, 303, 925, 973, 561, 594, 449, 690, 188, 19, 238,
                   554, 17, 638, 772, 540, 829, 773, 464, 796, 440, 125,
                   734, 708, 137, 344, 821, 741, 205, 66, 793, 335, 675,
                   146, 435, 356, 147, 657, 916, 610, 593, 696, 488, 81,
                   78, 993, 751, 836, 218, 58, 482, 144, 994, 520, 941,
                   764, 816, 155, 865, 100, 166, 114, 262, 713, 135, 420,
                   336, 9, 422, 91, 241, 40, 661, 814, 504, 895, 77, 86,
                   559, 845, 126, 471, 229, 608, 334, 838, 971, 351, 338,
                   84, 452, 466, 428, 425, 268, 830, 353, 721, 493, 359, 140,
                   769, 212, 639, 584, 743, 111, 873, 937, 902, 802, 933,
                   755, 270, 315, 533, 69, 615, 570, 339, 202, 421, 427,
                   666, 558, 924, 47, 251, 815, 896, 588, 316, 297, 899,
                   831, 543, 85, 430, 477, 906, 187, 371, 383, 614, 105,
                   26, 264, 129, 580, 854, 850, 537, 565, 391, 549, 963,
                   206, 481, 794, 762, 152, 915, 959, 654, 552, 372, 254,
                   386, 149, 758, 852, 462, 930, 944, 702, 193, 628, 389,
                   280, 228, 302, 362, 154, 189, 746, 777, 442, 663, 803,
                   704, 349, 808, 275, 250, 128, 23, 45, 106, 113, 57, 826,
                   124, 190, 312, 492, 955, 208, 429, 976, 387, 500, 686,
                   310, 255, 582, 912, 123, 328, 55, 967, 164, 51, 122, 669,
                   863, 65, 744, 541, 546, 712, 393, 780, 192, 416, 368, 740,
                   600, 130, 94, 278, 877, 291, 988, 28, 602, 768, 898, 585,
                   995, 16, 757, 911, 674, 571, 355, 611, 607, 363, 597, 394,
                   157, 577, 949, 216, 913, 209, 191, 282, 945, 260, 807, 465,
                   523, 521, 410, 756, 381, 279, 33, 604, 526, 692, 817, 501,
                   266, 801, 379, 1, 450, 631, 770, 313, 856, 227, 475, 900,
                   408, 325, 789, 622, 197, 629, 307, 304, 560, 982, 461, 409,
                   738, 919, 889, 731, 503, 380, 601, 691, 799, 748, 655, 210,
                   646, 134, 448, 511, 986, 701, 667, 716, 891, 161, 810, 882,
                   22, 107, 531, 446, 636, 929, 120, 237, 469, 849, 940, 679,
                   0, 318, 438, 529, 5, 999, 361, 290, 494, 784, 684, 800, 922,
                   346, 104, 939, 881, 12, 276, 749, 618, 365, 491, 74, 460, 29,
                   703, 841, 670, 778, 80, 987, 975, 474, 550, 798, 735, 727, 118,
                   437, 958, 273, 508, 952, 765, 979, 53, 785, 151, 443, 847, 960,
                   745, 177, 93, 333, 298, 413, 633, 548, 534, 62, 117, 842, 578,
                   214, 991, 688, 872, 165, 75, 903, 18, 505, 295, 519, 249, 787,
                   683, 728, 985, 603, 687, 198, 215, 305, 766, 288, 650, 996, 969,
                   880, 599, 553, 259, 244, 173, 591, 463, 705, 411, 557, 904, 473,
                   412, 846, 532, 472, 299, 640, 514, 405, 407, 317, 400, 935, 109,
                   136, 806, 883, 839, 243, 89, 809, 509, 366, 820, 99, 59, 200, 583,
                   32, 71, 162, 423, 180, 936, 625, 24, 236, 649, 681, 63, 36, 795,
                   551, 453, 234, 436, 138, 102, 485, 441, 885, 326, 314, 292, 240,
                   587, 378, 459, 977, 910, 175, 858, 871, 34, 374, 870, 145, 133,
                   637, 116, 235, 253, 119, 954, 169, 203, 239, 990, 859, 867, 490,
                   256, 457, 458, 21, 31, 7, 917, 524, 635, 30, 869, 54, 612, 95, 729,
                   88, 49, 908, 733, 329, 630, 834, 390, 267, 909, 907, 720, 901, 434,
                   414, 544, 516, 760, 56, 689, 957, 294, 920, 286, 730, 2, 569, 285,
                   184, 868, 980, 406, 342, 956, 141, 840, 968, 812, 222, 398, 142, 782,
                   767, 844, 354, 382, 201, 76, 196, 499, 753, 624, 96, 97, 358, 572, 61,
                   150, 495, 771, 357, 672, 673, 207, 225, 918, 131, 717, 306, 581, 127,
                   887, 73, 52, 888, 886, 323, 352, 404, 723, 277, 258, 284, 327, 4, 562,
                   343, 700, 245, 271, 823, 950, 13, 439, 468, 737, 879, 617, 658, 866,
                   828, 367, 921, 890, 848, 590, 293, 476, 525, 350, 563, 8, 518, 331, 965,
                   415, 857, 11, 289, 566, 783, 220, 347, 538, 467, 932, 680, 938, 719, 864,
                   265, 641, 759, 855, 399, 15, 732, 974, 195, 388, 715, 320, 875, 697, 224,
                   445, 517, 486, 694, 480, 168, 444, 931, 484, 171, 606, 337, 332, 402, 50,
                   231, 230, 170, 269, 6, 515, 301, 645, 14, 665, 726, 664, 671, 112, 547, 897,
                   160, 121, 659, 348, 143, 575, 426, 923, 487, 598, 804, 43, 824, 261, 981, 942,
                   653, 108, 822, 156, 545, 132, 79, 308, 3, 226, 324, 609, 115, 953, 983, 213,
                   779, 792, 373, 978, 775, 319, 37, 322, 576, 644, 158, 626, 70, 620, 662, 311,
                   568, 592, 221, 805, 972, 709, 774, 483, 159, 510, 616, 832, 496, 786, 992, 370,
                   489, 542, 419, 46, 621, 455, 623, 837, 651, 818, 642, 183, 811, 619, 574, 60, 813,
                   685, 83, 819, 884, 153, 634, 397, 966, 167, 433, 401, 997, 962, 914, 699, 376, 360,
                   456, 528, 927, 182, 98, 447, 300, 64, 677, 139, 20, 194, 946, 68, 454, 750,
                   825, 263, 579, 878, 513, 652, 535, 396, 718, 345, 179, 479, 27, 961, 502,
                   25, 736, 246, 377, 706, 791, 781, 754, 110, 876, 522, 797, 219, 330,
                   199, 752, 82, 724, 860, 948, 843, 90, 951, 296, 72, 309, 101, 233,
                   185, 432, 87, 827, 596, 739, 589, 242, 283, 790, 35, 874, 833, 67,
                   395, 573, 747, 861, 507, 943, 928, 905, 424, 530, 498, 403, 788,
                   725, 478, 892, 693, 274, 375, 647, 656, 431, 92, 711, 497, 181, 862,
                   506, 947, 364, 605, 38, 934, 761, 470, 698, 451, 853, 894, 595, 148, 556, 172, 564]

class City:
    def __init__(self, x=None, y=None):
        self.x = None
        self.y = None
        if x is not None:
            self.x = x
        else:
            self.x = int(random.random() * 200)
        if y is not None:
            self.y = y
        else:
            self.y = int(random.random() * 200)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceTo(self, city):
        xDistance = abs(self.getX() - city.getX())
        yDistance = abs(self.getY() - city.getY())
        distance = math.sqrt((xDistance * xDistance) + (yDistance * yDistance))
        return distance

    def __repr__(self):
        return str(self.getX()) + ", " + str(self.getY())


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
            if (max - fittest.getFitness()) >= (max - self.getTour(i).getFitness()):
                fittest = self.getTour(i)
        return fittest



    def populationSize(self):
        return len(self.tours)


class GA:
    def __init__(self, tourmanager, mutationRate=0.025, tournamentSize=75, elitism=True):
        self.tourmanager = tourmanager
        self.mutationRate = mutationRate
        self.tournamentSize = tournamentSize
        self.elitism = elitism

    def evolvePopulation(self, pop):
        newPopulation = Population(self.tourmanager, pop.populationSize(), False)
        elitismOffset = 0
        if self.elitism:
            newPopulation.saveTour(0, pop.getFittest())
            elitismOffset = 1
            #newPopulation.saveTour(1, pop.getFittest2())
            #elitismOffset = 2


        for i in range(elitismOffset, newPopulation.populationSize()):
            parent1 = self.tournamentSelection(pop)
            parent2 = self.tournamentSelection(pop)
            child = self.crossover(parent1, parent2)
            newPopulation.saveTour(i, child)

        for i in range(elitismOffset, newPopulation.populationSize()):
            self.mutate(newPopulation.getTour(i))

        return newPopulation

    def crossover(self, parent1, parent2):
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
    population_size = 100
    n_generations = 1000




    f = open("TSP.csv", "r")
    reader= csv.reader(f)
    # Load the map
    map_original = cv2.imread('map.jpg')

    # Setup cities and tour
    tourmanager = TourManager()

    for line in reader:
        x = float(line[0])
        y = float(line[1])

        print(x)
        print(y,"\n")

        tourmanager.addCity(City(x=x, y=y))
        cv2.circle(map_original, center=(int(9*x), int(9*y)), radius=1, color=(0, 0, 255), thickness=-1, lineType=cv2.LINE_AA)

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

        cv2.putText(map_result, org=(10, 25), text='Generation: %d' % (i + 1), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.7, color=0, thickness=1, lineType=cv2.LINE_AA)
        cv2.putText(map_result, org=(10, 50), text='Distance: %.2f' % fittest.getDistance(),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.7, color=0, thickness=1, lineType=cv2.LINE_AA)
        cv2.putText(map_result, org=(10, 950), text='CSI',
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=0, thickness=1, lineType=cv2.LINE_AA)
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