import random
import math

class Neuronio():
    def __init(self):
        self.aleatorizar()

    def aleatorizar(self, ilustrativo = False):
        if ilustrativo:
            limite = 5
            self.w1 = random.random()*limite
            self.w2 = random.random()*limite
            self.w3 = random.random()*limite
            self.b = random.random()*limite

        else:
            self.w1 = random.random()
            self.w2 = random.random()
            self.w3 = random.random()
            self.b = random.random()

    def novos_valores(self):
        limite = 40
        self.x = []
        self.yreal = []
        for i in range(3):
            e = []
            for j in range(3):
                e.append((random.random()-0.5)*limite)

            self.x.append(e)

            self.yreal.append(1 if e[0] + e[1] + e[2] >= 20 else 0)
        
        self.feed_forward()

    def sigmoid(self, x):
        return 1/(1+math.exp(-x))

    def dw(self, x, y, yreal): #derivada do custo em relação a w
        return (y - yreal)*x*y*(1-y)

    def db(self, y, yreal): #derivada do custo em relação a b
        return (y - yreal)*y*(1-y)

    def custo(self, y, yreal):
        # somatoria (y-yreal)^2  / 2
        return ((y - yreal)**2)/2

    def feed_forward(self):
        self.z = []
        self.a = []
        for i in range(3):
            self.z.append(self.w1*self.x[i][0] + self.w2*self.x[i][1] + self.w3*self.x[i][2] + self.b)
            self.a.append(self.sigmoid(self.z[i]))

    def treinar(self, n=0.1, epoch=1):
        
        for i in range(epoch):
            custo_m = 0
            self.feed_forward()

            deltas = [0,0,0,0]
            
            for j in range(3):
                custo_m += self.custo(self.a[j], self.yreal[j])
                deltas[0] += n*self.dw(self.x[j][0], self.a[j], self.yreal[j])
                deltas[1] += n*self.dw(self.x[j][1], self.a[j], self.yreal[j])
                deltas[2] += n*self.dw(self.x[j][2], self.a[j], self.yreal[j])
                deltas[3] += n*self.db(self.a[j], self.yreal[j])

            # Subtrai os detas dos parâmetros, pois a rede quer a inclinação negativa
            self.w1 -= deltas[0]

            self.w2 -= deltas[1]

            self.w3 -= deltas[2]

            self.b -= deltas[3]
            
            print("Epoch %d/%d - Custo Medio= %.2f"%(i+1, epoch, custo_m/3))
