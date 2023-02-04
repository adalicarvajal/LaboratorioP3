def controlador_de_vias():
    '''
    Funcion:
        Controla lo de las vias cerradas o abiertas 
    Parametros:
        Esta funcion no tiene parametros
    Retorna: 
        Esta funcion no retorna nada
    '''

    #Variable objetivo 
    estado_meta = {'Quito': '0', 'Chone': '0','Lorena': '0','Pilaton': '0'}
    #Defino el costo por abir vias
    costo=0
    #estado vias
    estado_meta["Quito"]=int(input("Ingrese el estado de la via Quito 0:abierto 1:cerrado : "))
    estado_meta["Chone"]=int(input("Ingrese el estado de la via Chone 0:abierto 1:cerrado : "))
    estado_meta["Lorena"]=int(input("Ingrese el estado de la via Lorena 0:abierto 1:cerrado : "))
    estado_meta["Pilaton"]=int(input("Ingrese el estado de la via Pilatonito 0:abierto 1:cerrado : "))
    #Estado inicial
    estado_inicial=input("Ingrese la via de donde inicia el recorrido\n(Q:Quito,C:CHONE,L:LORENA,P:PILATON),\nElija una opcion: ")
    #Esta es una pequeña porción de un código en Python. En cada línea de "if" se está evaluando si la variable "estado_inicial" 
    # es igual a una de las cuatro opciones posibles ("Q", "q", "C", "c", "L", "l", "P" o "p").
    if(estado_inicial=='Q' or estado_inicial=='q'):      
        estado_objetivo=input("Ingrese la via que quiere llegar \n(C:CHONE,L:LORENA,P:PILATON),\nElija una opcion:")
    #La primera sección de cuatro líneas de "if" establece una entrada de usuario que le pide al usuario 
    # que especifique el destino que desea alcanzar. La entrada de usuario es almacenada en la variable "estado_objetivo".
    if(estado_inicial=='C' or estado_inicial=='c'):      
        estado_objetivo=input("Ingrese la via que quiere llegar \n(Q:Quito,L:LORENA,P:PILATON),\nElija una opcion:")
    if(estado_inicial=='L' or estado_inicial=='l'):      
        estado_objetivo=input("Ingrese la via que quiere llegar \n(Q:Quito,C:CHONE,P:PILATON),\nElija una opcion:")
    if(estado_inicial=='P' or estado_inicial=='p'):      
        estado_objetivo=input("Ingrese la via que quiere llegar \n(Q:Quito,C:CHONE,L:LORENA),\nElija una opcion:")
    #La segunda sección de "if" evalúa el estado inicial y el estado objetivo y determina si las vías correspondientes están abiertas o cerradas (basadas en la variable "estado_meta")
    #Si alguna de las vías está cerrada, se muestra un mensaje indicando que la vía está cerrada y se está abriendo. 
    if(estado_inicial=='Q' or estado_inicial=='q'):
        if(estado_objetivo=='C' or estado_objetivo=='c'):
            if(estado_meta["Quito"]==1 and estado_meta["Chone"]==1):
                print("Via Quito Y chone Cerradas")
                print("Abriendo Vias...")
                print("Las vias han sido abiertas puede viajar sin problema")
                costo=costo+2
            # Si ambas vías están cerradas, se muestra un mensaje indicando que ambas vías están cerradas y se están abriendo. 
            # Si ambas vías están abiertas, se muestra un mensaje indicando que ambas vías están abiertas y se puede viajar sin problemas
            if(estado_meta["Quito"]==0 and estado_meta["Chone"]==1):
                print("Via chone Cerrada")
                print("Abriendo Via...")
                print("Las via Chone ha sido abierta puede viajar sin problema")
                costo=costo+1
            if(estado_meta["Quito"]==1 and estado_meta["Chone"]==0):
                print("Via Quito Cerrada")
                print("Abriendo Via...")
                print("Las via Quito ha sido abierta puede viajar sin problema")
                costo=costo+1
            # Además, la variable "costo" se actualiza en función de la cantidad de vías abiertas o cerradas.
            if(estado_meta["Quito"]==0 and estado_meta["Chone"]==0):
                print("Las vias se encuentran abiertas, puede viajar sin problema")
                costo=costo+0
       #El código chequea el estado inicial y objetivo de un viaje y verifica 
       # el estado de las vías intermedias "Quito", "Lorena", "Pilaton" y "Chone" en un diccionario llamado "estado_meta". 
        if(estado_objetivo=='L' or estado_objetivo=='l'):
            if(estado_meta["Quito"]==1 and estado_meta["Lorena"]==1):
                print("Via Quito Y Lorena Cerradas")
                print("Abriendo Vias...")
                print("Las vias han sido abiertas puede viajar sin problema")
                costo=costo+2
        #Si alguna de las vías está cerrada, se imprimen mensajes indicando la vía cerrada y que se está abriendo, y se aumenta el costo del viaje.
            if(estado_meta["Quito"]==0 and estado_meta["Lorena"]==1):
                print("Via Lorena Cerrada")
                print("Abriendo Via...")
                print("Las via Lorena ha sido abierta puede viajar sin problema")
                costo=costo+1
        #Si ambas vías están cerradas, se imprime un mensaje indicando que ambas vías están cerradas y que se están abriendo, y se aumenta el costo en 2. 
            if(estado_meta["Quito"]==1 and estado_meta["Lorena"]==0):
                print("Via Quito Cerrada")
                print("Abriendo Via...")
                print("Las via Quito ha sido abierta puede viajar sin problema")
                costo=costo+1
            if(estado_meta["Quito"]==0 and estado_meta["Lorena"]==0):
                print("Las vias se encuentran abiertas, puede viajar sin problema")
                costo=costo+0
        #Si ambas vías están abiertas, se imprime un mensaje indicando que se puede viajar sin problemas y no se aumenta el costo.
        if(estado_objetivo=='P' or estado_objetivo=='p'):
            if(estado_meta["Quito"]==1 and estado_meta["Pilaton"]==1):
                print("Via Quito Y Pilaton Cerradas")
                print("Abriendo Vias...")
                print("Las vias han sido abiertas puede viajar sin problema")
                costo=costo+2
        #Si es así, se entra al siguiente bloque de código que comprueba si el valor de estado_objetivo es igual a 'Q' o 'q'.
            if(estado_meta["Quito"]==0 and estado_meta["Pilaton"]==1):
                print("Via Pilaton Cerrada")
                print("Abriendo Via...")
                print("Las via Pilaton ha sido abierta puede viajar sin problema")
                costo=costo+1
        #Si es así, se entra en el siguiente bloque de código que verifica
        #  el valor de estado_meta["Chone"] y estado_meta["Quito"] para determinar si las vías Chone y Quito están cerradas o no    
            if(estado_meta["Quito"]==1 and estado_meta["Pilaton"]==0):
                print("Via Quito Cerrada")
                print("Abriendo Via...")
                print("Las via Quito ha sido abierta puede viajar sin problema")
                costo=costo+1
        #si ambas vías están cerradas, se imprime un mensaje indicando que las vías están cerradas y se están abriendo, y se aumenta el valor de costo en 2    
            if(estado_meta["Quito"]==0 and estado_meta["Pilaton"]==0):
                print("Las vias se encuentran abiertas, puede viajar sin problema")
                costo=costo+0
#Si solo la vía Quito está cerrada, se imprime un mensaje
#  indicando que solo la vía Quito está cerrada y se está abriendo, y se aumenta el valor de costo en 1
    if(estado_inicial=='C' or estado_inicial=='c'):
        #Si el valor de estado_objetivo no es igual a 'Q' o 'q', se entra en el siguiente bloque de código que verifica
        #  el valor de estado_meta["Chone"] y estado_meta["Lorena"] para determinar si las vías Chone y Lorena están cerradas o no
        if(estado_objetivo=='Q' or estado_objetivo=='q'):
            #Si solo la vía Chone está cerrada, se imprime un mensaje indicando que solo 
            # la vía Chone está cerrada y se está abriendo, y se aumenta el valor de costo en 1
            if(estado_meta["Chone"]==1 and estado_meta["Quito"]==1):
                print("Via Chone Y Quito Cerradas")
                print("Abriendo Vias...")
                print("Las vias han sido abiertas puede viajar sin problema")
                costo=costo+2
            #i ambas vías están abiertas, se imprime un mensaje indicando que ambas vías
            #  están abiertas y se puede viajar sin problemas, y el valor de costo no se modifica.
            if(estado_meta["Chone"]==0 and estado_meta["Quito"]==1):
                print("Via Quito Cerrada")
                print("Abriendo Via...")
                print("Las via Quito ha sido abierta puede viajar sin problema")
                costo=costo+1
            #Si ambas vías están cerradas, se imprime un mensaje indicando que las vías están cerradas y se están abriendo, y se aumenta el valor de costo en 2
            if(estado_meta["Chone"]==1 and estado_meta["Quito"]==0):
                print("Via Chone Cerrada")
                print("Abriendo Via...")
                print("Las via Chone ha sido abierta puede viajar sin problema")
                costo=costo+1
            #Si solo la vía Lorena está cerrada, se imprime un mensaje indicando que solo la vía Lorena está cerrada y se está abriendo, y se aumenta el valor de costo en 1
            if(estado_meta["Chone"]==0 and estado_meta["Quito"]==0):
                print("Las vias se encuentran abiertas, puede viajar sin problema")
                costo=costo+0
        #Si solo la vía Chone está cerrada, se imprime un mensaje indicando que solo la vía Chone está cerrada y se está abriendo, y se aumenta el valor de costo en 1.
        if(estado_objetivo=='L' or estado_objetivo=='l'):
            if(estado_meta["Chone"]==1 and estado_meta["Lorena"]==1):
                print("Via Chone Y Quito Cerradas")
                print("Abriendo Vias...")
                print("Las vias han sido abiertas puede viajar sin problema")
                costo=costo+2
            #Si ambas vías están abiertas, se imprime un mensaje indicando que ambas vías están abiertas y se puede viajar sin problemas, y el valor de costo no se modifica.
            if(estado_meta["Chone"]==0 and estado_meta["Lorena"]==1):
                print("Via Lorena Cerrada")
                print("Abriendo Via...")
                print("Las via Lorena ha sido abierta puede viajar sin problema")
                costo=costo+1
            #i ambas vías están abiertas, se imprime un mensaje indicando que ambas vías están abiertas
            if(estado_meta["Chone"]==1 and estado_meta["Lorena"]==0):
                print("Via Chone Cerrada")
                print("Abriendo Via...")
                print("Las via Chone ha sido abierta puede viajar sin problema")
                costo=costo+1
            #i ambas vías están abiertas, se imprime un mensaje indicando que ambas vías están abiertas
            if(estado_meta["Chone"]==0 and estado_meta["Lorena"]==0):
                print("Las vias se encuentran abiertas, puede viajar sin problema")
                costo=costo+0
        #Este if verifica si el estado objetivo es 'P' o 'p'. Si es así, entra en el bloque de código.
        if(estado_objetivo=='P' or estado_objetivo=='p'):
            #Este if verifica si las vías Chone y Pilaton están cerradas (valor 1 en el diccionario estado_meta). Si ambas vías están cerradas, entra en este bloque de código.
            if(estado_meta["Chone"]==1 and estado_meta["Pilaton"]==1):
                #Este comando imprime en la consola "Via Chone Y Pilaton Cerradas".
                print("Via Chone Y Pilaton Cerradas")
                #Este comando imprime en la consola "Abriendo Vias...".
                print("Abriendo Vias...")
                #Este comando imprime en la consola "Las vias han sido abiertas puede viajar sin problema".
                print("Las vias han sido abiertas puede viajar sin problema")
                #Este comando aumenta el valor de costo en 2.
                costo=costo+2
            #Este if verifica si la vía Chone está abierta (valor 0 en el diccionario estado_meta) y la vía Pilaton está cerrada. Si ambas condiciones son verdaderas, entra en este bloque de código.
            if(estado_meta["Chone"]==0 and estado_meta["Pilaton"]==1):
                print("Via Pilaton Cerrada")
                print("Abriendo Via...")
                print("Las via Pilaton ha sido abierta puede viajar sin problema")
                costo=costo+1
            #Este if verifica si la vía Chone está abierta (valor 0 en el diccionario estado_meta) y la vía Pilaton está cerrada. Si ambas condiciones son verdaderas, entra en este bloque de código.
            if(estado_meta["Chone"]==1 and estado_meta["Pilaton"]==0):
                print("Via Chone Cerrada")
                print("Abriendo Via...")
                print("Las via Chone ha sido abierta puede viajar sin problema")
                costo=costo+1
            #Este if verifica si la vía Chone está cerrada y la vía Pilaton está abierta. Si ambas condiciones son verdaderas, entra en este bloque de código.
            if(estado_meta["Chone"]==0 and estado_meta["Pilaton"]==0):
                print("Las vias se encuentran abiertas, puede viajar sin problema")
                costo=costo+0
    #La primera linea verifica si el estado inicial es "L" o "l".
    if(estado_inicial=='L' or estado_inicial=='l'):
        #Si es así, se entra al siguiente bloque de codigo.
        if(estado_objetivo=='Q' or estado_objetivo=='q'):
            #La segunda linea verifica si el estado objetivo es "Q" o "q".
            if(estado_meta["Lorena"]==1 and estado_meta["Quito"]==1):
                print("Via Lorena Y Quito Cerradas")
                print("Abriendo Vias...")
                print("Las vias han sido abiertas puede viajar sin problema")
                costo=costo+2
            #Si es así, se entra al siguiente bloque de codigo.
            if(estado_meta["Lorena"]==0 and estado_meta["Quito"]==1):
                print("Via Quito Cerrada")
                print("Abriendo Via...")
                print("Las via Quito ha sido abierta puede viajar sin problema")
                costo=costo+1
            #Las siguientes 4 lineas comparan los valores de los atributos "Lorena" y "Quito" en el diccionario "estado_meta".
            if(estado_meta["Lorena"]==1 and estado_meta["Quito"]==0):
                print("Via Lorena Cerrada")
                print("Abriendo Via...")
                print("Las via Lorena ha sido abierta puede viajar sin problema")
                costo=costo+1
            #Según la combinación de estos valores, se imprimen diferentes mensajes, tales como si la(s) via(s) está(n) cerrada(s) o abierta(s), y si se deben abrir o no.
            if(estado_meta["Lorena"]==0 and estado_meta["Quito"]==0):
                print("Las vias se encuentran abiertas, puede viajar sin problema")
                costo=costo+0
        #Esta sección del código se encarga de evaluar el estado del viaje en función del origen y destino deseados. Se comprueba si la ciudad de origen es "Lorena" (independientemente 
        # de que la letra sea mayúscula o minúscula) y luego se evalúan los diferentes destinos posibles ("Chone", "Pilaton" o "Quito").
        if(estado_objetivo=='C' or estado_objetivo=='c'):
            #Si el destino es "Chone".
            if(estado_meta["Lorena"]==1 and estado_meta["Chone"]==1):
                print("Via Lorena Y Chone Cerradas")
                print("Abriendo Vias...")
                print("Las vias han sido abiertas puede viajar sin problema")
                costo=costo+2
            #Si tanto Lorena como Chone están cerradas.
            if(estado_meta["Lorena"]==0 and estado_meta["Chone"]==1):
                print("Via Chone Cerrada")
                print("Abriendo Via...")
                print("Las via Chone ha sido abierta puede viajar sin problema")
                costo=costo+1
            #Los demás if tienen una lógica similar, solo que se evalúan diferentes combinaciones de cierre o apertura de las vías.
            if(estado_meta["Lorena"]==1 and estado_meta["Chone"]==0):
                print("Via Lorena Cerrada")
                print("Abriendo Via...")
                print("Las via Lorena ha sido abierta puede viajar sin problema")
                costo=costo+1
            if(estado_meta["Lorena"]==0 and estado_meta["Chone"]==0):
                print("Las vias se encuentran abiertas, puede viajar sin problema")
                costo=costo+0
        # Este if comprueba si el estado objetivo es "P" o "p".
        if(estado_objetivo=='P' or estado_objetivo=='p'):
            #: Este if comprueba si las vías "Lorena" y "Pilaton" están cerradas.
            if(estado_meta["Lorena"]==1 and estado_meta["Pilaton"]==1):
                print("Via Lorena Y Pilaton Cerradas")
                print("Abriendo Vias...")
                print("Las vias han sido abiertas puede viajar sin problema")
                costo=costo+2
            #Este if comprueba si la vía "Pilaton" está cerrada y la vía "Lorena" está abierta.
            if(estado_meta["Lorena"]==0 and estado_meta["Pilaton"]==1):
                print("Via Pilaton Cerrada")
                print("Abriendo Via...")
                print("Las via Pilaton ha sido abierta puede viajar sin problema")
                costo=costo+1
            # Este if comprueba si la vía "Pilaton" está cerrada y la vía "Lorena" está abierta.
            if(estado_meta["Lorena"]==1 and estado_meta["Pilaton"]==0):
                print("Via Lorena Cerrada")
                print("Abriendo Via...")
                print("Las via Lorena ha sido abierta puede viajar sin problema")
                costo=costo+1
            # Este if comprueba si la vía "Lorena" está cerrada y la vía "Pilaton" está abierta.
            if(estado_meta["Lorena"]==0 and estado_meta["Pilaton"]==0):
                print("Las vias se encuentran abiertas, puede viajar sin problema")
                costo=costo+0
    # comprueba si el valor de estado_inicial es igual a 'p' o 'P'. Esta linea es incorrecta ya que hay dos veces la comparación con 'p'.
    if(estado_inicial=='p' or estado_inicial=='p'):
        # Este if comprueba si el valor de estado_objetivo es igual a 'Q' o 'q'.
        if(estado_objetivo=='Q' or estado_objetivo=='q'):
            #Este if comprueba si tanto la via "Pilaton" como la via "Quito" estan cerradas (1 significa cerrada y 0 significa abierta).
            if(estado_meta["Pilaton"]==1 and estado_meta["Quito"]==1):
                print("Via Pilaton Y Quito Cerradas")
                print("Abriendo Vias...")
                print("Las vias han sido abiertas puede viajar sin problema")
                costo=costo+2
            #Este if comprueba si la via "Pilaton" esta abierta y la via "Quito" esta cerrada.
            if(estado_meta["Pilaton"]==0 and estado_meta["Quito"]==1):
                print("Via Quito Cerrada")
                print("Abriendo Via...")
                print("Las via Quito ha sido abierta puede viajar sin problema")
                costo=costo+1
            #Este if comprueba si la via "Pilaton" esta cerrada y la via "Quito" esta abierta.
            if(estado_meta["Pilaton"]==1 and estado_meta["Quito"]==0):
                print("Via Pilaton Cerrada")
                print("Abriendo Via...")
                print("Las via Pilaton ha sido abierta puede viajar sin problema")
                costo=costo+1
            # Este if comprueba si tanto la via "Pilaton" como la via "Quito" estan abiertas.
            if(estado_meta["Pilaton"]==0 and estado_meta["Quito"]==0):
                print("Las vias se encuentran abiertas, puede viajar sin problema")
                costo=costo+0
        #El primer if evalúa si el estado objetivo es 'C' o 'c'. Si es verdadero, entra en el siguiente bloque de if anidado.
        if(estado_objetivo=='C' or estado_objetivo=='c'):
            #os siguientes tres if anidados evalúan el estado de las vías "Pilaton" y "Chone" a través de estado_meta["Pilaton"] y estado_meta["Chone"]
            if(estado_meta["Pilaton"]==1 and estado_meta["Chone"]==1):
                print("Via Pilaton Y Chone Cerradas")
                print("Abriendo Vias...")
                print("Las vias han sido abiertas puede viajar sin problema")
                costo=costo+2
            #Si ambas vías están cerradas, se imprime un mensaje de que ambas vías están cerradas y se informa que se están abriendo. 
            if(estado_meta["Pilaton"]==0 and estado_meta["Chone"]==1):
                print("Via Chone Cerrada")
                print("Abriendo Via...")
                print("Las via Chone ha sido abierta puede viajar sin problema")
                costo=costo+1
            #Si solo una vía está cerrada, se imprime un mensaje sobre la vía cerrada y se informa que se está abriendo.
            if(estado_meta["Pilaton"]==1 and estado_meta["Chone"]==0):
                print("Via Pilaton Cerrada")
                print("Abriendo Via...")
                print("Las via Pilaton ha sido abierta puede viajar sin problema")
                costo=costo+1
            #Si solo una vía está cerrada, se imprime un mensaje sobre la vía cerrada y se informa que se está abriendo.
            if(estado_meta["Pilaton"]==0 and estado_meta["Chone"]==0):
                print("Las vias se encuentran abiertas, puede viajar sin problema")
                costo=costo+0
        #se imprime un mensaje indicando que ambas vías están cerradas y se abren. El costo de viaje se incrementa en 2.
        if(estado_objetivo=='L' or estado_objetivo=='l'):
            #Si solo la vía Lorena está cerrada (estado_meta["Pilaton"] = 0 y estado_meta["Lorena"] = 1), se imprime un mensaje indicando que solo la vía Lorena está cerrada y se abre.
            if(estado_meta["Pilaton"]==1 and estado_meta["Lorena"]==1):
                print("Via Pilaton Y Lorena Cerradas")
                print("Abriendo Vias...")
                print("Las vias han sido abiertas puede viajar sin problema")
                costo=costo+2
            #El costo de viaje se incrementa en 1. Si solo la vía Pilatón está cerrada (estado_meta["Pilaton"] = 1 y estado_meta["Lorena"] = 0), se imprime un mensaje indicando que solo la vía Pilatón está cerrada y se abre
            if(estado_meta["Pilaton"]==0 and estado_meta["Lorena"]==1):
                print("Via Lorena Cerrada")
                print("Abriendo Via...")
                print("Las via Lorena ha sido abierta puede viajar sin problema")
                costo=costo+1
            #El costo de viaje se incrementa en 1. Si ambas vías están abiertas (estado_meta["Pilaton"] = 0 y estado_meta["Lorena"] = 0)
            if(estado_meta["Pilaton"]==1 and estado_meta["Lorena"]==0):
                print("Via Pilaton Cerrada")
                print("Abriendo Via...")
                print("Las via Pilaton ha sido abierta puede viajar sin problema")
                costo=costo+1
            #se imprime un mensaje indicando que ambas vías están abiertas y el costo de viaje no se incrementa.
            if(estado_meta["Pilaton"]==0 and estado_meta["Lorena"]==0):
                print("Las vias se encuentran abiertas, puede viajar sin problema")
                costo=costo+0
    #mensaje del costo que se va apagar por abrir la via
    print("El costo por abrir la via es ",costo)
if __name__ == '__main__':
    #llamamos a la funcio 
    controlador_de_vias()