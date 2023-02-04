def controlador_de_vias():
    '''
    Funcion que CONTRALA LAS VIAS ABRIENDOLAS Y CERRANDOLAS
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
    if(estado_inicial=='Q' or estado_inicial=='q'):      
        estado_objetivo=input("Ingrese la via que quiere llegar \n(C:CHONE,L:LORENA,P:PILATON),\nElija una opcion:")
    if(estado_inicial=='C' or estado_inicial=='c'):      
        estado_objetivo=input("Ingrese la via que quiere llegar \n(Q:Quito,L:LORENA,P:PILATON),\nElija una opcion:")
    if(estado_inicial=='L' or estado_inicial=='l'):      
        estado_objetivo=input("Ingrese la via que quiere llegar \n(Q:Quito,C:CHONE,P:PILATON),\nElija una opcion:")
    if(estado_inicial=='P' or estado_inicial=='p'):      
        estado_objetivo=input("Ingrese la via que quiere llegar \n(Q:Quito,C:CHONE,L:LORENA),\nElija una opcion:")

    if(estado_inicial=='Q' or estado_inicial=='q'):
        if(estado_objetivo=='C' or estado_objetivo=='c'):
            if(estado_meta["Quito"]==1 and estado_meta["Chone"]==1):
                print("Via Quito Y chone Cerradas")
                print("Abriendo Vias...")
                print("Las vias han sido abiertas puede viajar sin problema")
                costo=costo+2
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
            if(estado_meta["Quito"]==0 and estado_meta["Chone"]==0):
                print("Las vias se encuentran abiertas, puede viajar sin problema")
                costo=costo+0

        if(estado_objetivo=='L' or estado_objetivo=='l'):
            if(estado_meta["Quito"]==1 and estado_meta["Lorena"]==1):
                print("Via Quito Y Lorena Cerradas")
                print("Abriendo Vias...")
                print("Las vias han sido abiertas puede viajar sin problema")
                costo=costo+2
            if(estado_meta["Quito"]==0 and estado_meta["Lorena"]==1):
                print("Via Lorena Cerrada")
                print("Abriendo Via...")
                print("Las via Lorena ha sido abierta puede viajar sin problema")
                costo=costo+1
            if(estado_meta["Quito"]==1 and estado_meta["Lorena"]==0):
                print("Via Quito Cerrada")
                print("Abriendo Via...")
                print("Las via Quito ha sido abierta puede viajar sin problema")
                costo=costo+1
            if(estado_meta["Quito"]==0 and estado_meta["Lorena"]==0):
                print("Las vias se encuentran abiertas, puede viajar sin problema")
                costo=costo+0
        if(estado_objetivo=='P' or estado_objetivo=='p'):
            if(estado_meta["Quito"]==1 and estado_meta["Pilaton"]==1):
                print("Via Quito Y Pilaton Cerradas")
                print("Abriendo Vias...")
                print("Las vias han sido abiertas puede viajar sin problema")
                costo=costo+2
            if(estado_meta["Quito"]==0 and estado_meta["Pilaton"]==1):
                print("Via Pilaton Cerrada")
                print("Abriendo Via...")
                print("Las via Pilaton ha sido abierta puede viajar sin problema")
                costo=costo+1
            if(estado_meta["Quito"]==1 and estado_meta["Pilaton"]==0):
                print("Via Quito Cerrada")
                print("Abriendo Via...")
                print("Las via Quito ha sido abierta puede viajar sin problema")
                costo=costo+1
            if(estado_meta["Quito"]==0 and estado_meta["Pilaton"]==0):
                print("Las vias se encuentran abiertas, puede viajar sin problema")
                costo=costo+0
    if(estado_inicial=='C' or estado_inicial=='c'):
        if(estado_objetivo=='Q' or estado_objetivo=='q'):
            if(estado_meta["Chone"]==1 and estado_meta["Quito"]==1):
                print("Via Chone Y Quito Cerradas")
                print("Abriendo Vias...")
                print("Las vias han sido abiertas puede viajar sin problema")
                costo=costo+2
            if(estado_meta["Chone"]==0 and estado_meta["Quito"]==1):
                print("Via Quito Cerrada")
                print("Abriendo Via...")
                print("Las via Quito ha sido abierta puede viajar sin problema")
                costo=costo+1
            if(estado_meta["Chone"]==1 and estado_meta["Quito"]==0):
                print("Via Chone Cerrada")
                print("Abriendo Via...")
                print("Las via Chone ha sido abierta puede viajar sin problema")
                costo=costo+1
            if(estado_meta["Chone"]==0 and estado_meta["Quito"]==0):
                print("Las vias se encuentran abiertas, puede viajar sin problema")
                costo=costo+0
        if(estado_objetivo=='L' or estado_objetivo=='l'):
            if(estado_meta["Chone"]==1 and estado_meta["Lorena"]==1):
                print("Via Chone Y Quito Cerradas")
                print("Abriendo Vias...")
                print("Las vias han sido abiertas puede viajar sin problema")
                costo=costo+2
            if(estado_meta["Chone"]==0 and estado_meta["Lorena"]==1):
                print("Via Lorena Cerrada")
                print("Abriendo Via...")
                print("Las via Lorena ha sido abierta puede viajar sin problema")
                costo=costo+1
            if(estado_meta["Chone"]==1 and estado_meta["Lorena"]==0):
                print("Via Chone Cerrada")
                print("Abriendo Via...")
                print("Las via Chone ha sido abierta puede viajar sin problema")
                costo=costo+1
            if(estado_meta["Chone"]==0 and estado_meta["Lorena"]==0):
                print("Las vias se encuentran abiertas, puede viajar sin problema")
                costo=costo+0
        if(estado_objetivo=='P' or estado_objetivo=='p'):
            if(estado_meta["Chone"]==1 and estado_meta["Pilaton"]==1):
                print("Via Chone Y Pilaton Cerradas")
                print("Abriendo Vias...")
                print("Las vias han sido abiertas puede viajar sin problema")
                costo=costo+2
            if(estado_meta["Chone"]==0 and estado_meta["Pilaton"]==1):
                print("Via Pilaton Cerrada")
                print("Abriendo Via...")
                print("Las via Pilaton ha sido abierta puede viajar sin problema")
                costo=costo+1
            if(estado_meta["Chone"]==1 and estado_meta["Pilaton"]==0):
                print("Via Chone Cerrada")
                print("Abriendo Via...")
                print("Las via Chone ha sido abierta puede viajar sin problema")
                costo=costo+1
            if(estado_meta["Chone"]==0 and estado_meta["Pilaton"]==0):
                print("Las vias se encuentran abiertas, puede viajar sin problema")
                costo=costo+0
    
    if(estado_inicial=='L' or estado_inicial=='l'):
        if(estado_objetivo=='Q' or estado_objetivo=='q'):
            if(estado_meta["Lorena"]==1 and estado_meta["Quito"]==1):
                print("Via Lorena Y Quito Cerradas")
                print("Abriendo Vias...")
                print("Las vias han sido abiertas puede viajar sin problema")
                costo=costo+2
            if(estado_meta["Lorena"]==0 and estado_meta["Quito"]==1):
                print("Via Quito Cerrada")
                print("Abriendo Via...")
                print("Las via Quito ha sido abierta puede viajar sin problema")
                costo=costo+1
            if(estado_meta["Lorena"]==1 and estado_meta["Quito"]==0):
                print("Via Lorena Cerrada")
                print("Abriendo Via...")
                print("Las via Lorena ha sido abierta puede viajar sin problema")
                costo=costo+1
            if(estado_meta["Lorena"]==0 and estado_meta["Quito"]==0):
                print("Las vias se encuentran abiertas, puede viajar sin problema")
                costo=costo+0
        if(estado_objetivo=='C' or estado_objetivo=='c'):
            if(estado_meta["Lorena"]==1 and estado_meta["Chone"]==1):
                print("Via Lorena Y Chone Cerradas")
                print("Abriendo Vias...")
                print("Las vias han sido abiertas puede viajar sin problema")
                costo=costo+2
            if(estado_meta["Lorena"]==0 and estado_meta["Chone"]==1):
                print("Via Chone Cerrada")
                print("Abriendo Via...")
                print("Las via Chone ha sido abierta puede viajar sin problema")
                costo=costo+1
            if(estado_meta["Lorena"]==1 and estado_meta["Chone"]==0):
                print("Via Lorena Cerrada")
                print("Abriendo Via...")
                print("Las via Lorena ha sido abierta puede viajar sin problema")
                costo=costo+1
            if(estado_meta["Lorena"]==0 and estado_meta["Chone"]==0):
                print("Las vias se encuentran abiertas, puede viajar sin problema")
                costo=costo+0
        if(estado_objetivo=='P' or estado_objetivo=='p'):
            if(estado_meta["Lorena"]==1 and estado_meta["Pilaton"]==1):
                print("Via Lorena Y Pilaton Cerradas")
                print("Abriendo Vias...")
                print("Las vias han sido abiertas puede viajar sin problema")
                costo=costo+2
            if(estado_meta["Lorena"]==0 and estado_meta["Pilaton"]==1):
                print("Via Pilaton Cerrada")
                print("Abriendo Via...")
                print("Las via Pilaton ha sido abierta puede viajar sin problema")
                costo=costo+1
            if(estado_meta["Lorena"]==1 and estado_meta["Pilaton"]==0):
                print("Via Lorena Cerrada")
                print("Abriendo Via...")
                print("Las via Lorena ha sido abierta puede viajar sin problema")
                costo=costo+1
            if(estado_meta["Lorena"]==0 and estado_meta["Pilaton"]==0):
                print("Las vias se encuentran abiertas, puede viajar sin problema")
                costo=costo+0
    if(estado_inicial=='p' or estado_inicial=='p'):
        if(estado_objetivo=='Q' or estado_objetivo=='q'):
            if(estado_meta["Pilaton"]==1 and estado_meta["Quito"]==1):
                print("Via Pilaton Y Quito Cerradas")
                print("Abriendo Vias...")
                print("Las vias han sido abiertas puede viajar sin problema")
                costo=costo+2
            if(estado_meta["Pilaton"]==0 and estado_meta["Quito"]==1):
                print("Via Quito Cerrada")
                print("Abriendo Via...")
                print("Las via Quito ha sido abierta puede viajar sin problema")
                costo=costo+1
            if(estado_meta["Pilaton"]==1 and estado_meta["Quito"]==0):
                print("Via Pilaton Cerrada")
                print("Abriendo Via...")
                print("Las via Pilaton ha sido abierta puede viajar sin problema")
                costo=costo+1
            if(estado_meta["Pilaton"]==0 and estado_meta["Quito"]==0):
                print("Las vias se encuentran abiertas, puede viajar sin problema")
                costo=costo+0
        if(estado_objetivo=='C' or estado_objetivo=='c'):
            if(estado_meta["Pilaton"]==1 and estado_meta["Chone"]==1):
                print("Via Pilaton Y Chone Cerradas")
                print("Abriendo Vias...")
                print("Las vias han sido abiertas puede viajar sin problema")
                costo=costo+2
            if(estado_meta["Pilaton"]==0 and estado_meta["Chone"]==1):
                print("Via Chone Cerrada")
                print("Abriendo Via...")
                print("Las via Chone ha sido abierta puede viajar sin problema")
                costo=costo+1
            if(estado_meta["Pilaton"]==1 and estado_meta["Chone"]==0):
                print("Via Pilaton Cerrada")
                print("Abriendo Via...")
                print("Las via Pilaton ha sido abierta puede viajar sin problema")
                costo=costo+1
            if(estado_meta["Pilaton"]==0 and estado_meta["Chone"]==0):
                print("Las vias se encuentran abiertas, puede viajar sin problema")
                costo=costo+0
        if(estado_objetivo=='L' or estado_objetivo=='l'):
            if(estado_meta["Pilaton"]==1 and estado_meta["Lorena"]==1):
                print("Via Pilaton Y Lorena Cerradas")
                print("Abriendo Vias...")
                print("Las vias han sido abiertas puede viajar sin problema")
                costo=costo+2
            if(estado_meta["Pilaton"]==0 and estado_meta["Lorena"]==1):
                print("Via Lorena Cerrada")
                print("Abriendo Via...")
                print("Las via Lorena ha sido abierta puede viajar sin problema")
                costo=costo+1
            if(estado_meta["Pilaton"]==1 and estado_meta["Lorena"]==0):
                print("Via Pilaton Cerrada")
                print("Abriendo Via...")
                print("Las via Pilaton ha sido abierta puede viajar sin problema")
                costo=costo+1
            if(estado_meta["Pilaton"]==0 and estado_meta["Lorena"]==0):
                print("Las vias se encuentran abiertas, puede viajar sin problema")
                costo=costo+0
    print("El costo por abrir la via es ",costo)
if __name__ == '__main__':
    controlador_de_vias()