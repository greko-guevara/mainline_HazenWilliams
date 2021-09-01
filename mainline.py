#codigo de entrada
print ("***********************************************************")
print ("Bienvenido al programa para diseño de tuberías principales por el método de Hazen William")
print ("Tomado del escritorio de G_Guevara usando Python 3.9")
Q= float (input("introduzca la Caudal (m3/h): ")) 
L= float (input("introduzca la Longitud (m): "))
HF=float (input("introduzca las pérdidas (mca): "))
C= 150 #rugosidad  
dia=[39.8,45.9,57.38,69.46,84.58,108.72,160.08,208.42,259.75,308.05,369.7] #Tuberia SDR diametro interno

LL=L # de longitud total fija
LLL=0 #longitud 2 del diametro combinado
n=-1 #punto de inicio para el loop que busca el diametro inferior
HF3=HF #valor de inicio para la combinacion de diametros 



for j in dia: #codigo de para calcular el diametro correcto
    HF1= (1.131*10**9*(Q/C)**1.852*L*j**-4.872)
    if j==39.8: #definimos el diametro inferior
        jj=0
    else: #loop del diametro inferior que viene detras del diametro que se calcula
        n+=1
        jj=dia[n]
    
    Area= 3.141516*(j/2000)**2
    Vel=Q/Area/3600    
    tiempo=L/Vel/60
    
    
        #definimos el diametro inferior
    if Vel>3: # prueba para evitar velocidades turbulentas 
        continue   
    if HF1<HF:  #Prueba para saber que es el díametro correcto
        while HF3 >= HF:  #si el diametro es el correcto hace loop para ajustar L combinación de diametros
            Area2= 3.141516*(jj/2000)**2
            Vel2=Q/Area2/3600
            if Vel2>3:  # prueba para evitar velocidades turbulentas en el diametro inferior 
                break
            L-=1
            LLL=LL-L
            HF3=(1.131*10**9*(Q/C)**1.852*L*jj**-4.872)+(1.131*10**9*(Q/C)**1.852*LLL*j**-4.872)
        break
tiempo2=(LLL/Vel+L/Vel2)/60
#Salidas 
 
F1=round(HF1,2)
HF3=round(HF3,2)
L=round(L,2)
LL=round(LL,2)
LLL=round(LLL,2)
Vel=round(Vel,2)
Vel2=round(Vel2,2)   
tiempo=round(tiempo,2)
tiempo2=round(tiempo2,2)



print ("***********************************************************")
print ("***********************************************************")
print ("el diametro sugerido: " + str(j) + " mm")
print ("las perdidas por fricción: " + str(HF1) + " mca")
print ("con una velocidad: " + str(Vel) + " m/s")
print ("con una tiempo de avance: " + str(tiempo) + " minutos")
print ("***********************************************************")
print ("***********************************************************")
if Vel2<3:
    print ("también puedes combinar el dimétro  "+str(j)+" mm x "+str(LLL)+" m y " +str(jj)+" mm x "+str(L)+" m")
    print ("las pérdidas son de "+str(HF3)+" mca")
    print ("las velocidades son =  "+str(Vel)+" m/s x "+str(j)+" mm y " +str(Vel2)+" m/s x "+str(jj)+" mm")
    print ("con una tiempo de avance: " + str(tiempo2) + " minutos")
else:
    print ("no se recomienda combinar diámetros, diámetro menor tendría una velocidad mayor a 3.0 m/s ")




###### aca prácticamos los principios de manejo de listas de datos y la función de For j para evaluar

