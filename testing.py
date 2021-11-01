import MonteCarloParalelo, MonteCarloSerie

tiemposP=[]
tiemposS=[]
N=[]
csv = ["N,t Paralelo [ms],t Serie [ms]\n"]

if __name__=='__main__':
    for x in range(8):
        n= 10**x
        pi, tiempoP = MonteCarloParalelo.mc_paralelo(n)
        pi, tiempoS = MonteCarloSerie.mc_serie(n)
        csv.append("")
        csv[x] += str(n)+","+str(tiempoP)+","+str(tiempoS)+"\n"

    f = open("montecarlo.csv", "w")
    for i in range(8):
        f.write(csv[i])
    f.close()
