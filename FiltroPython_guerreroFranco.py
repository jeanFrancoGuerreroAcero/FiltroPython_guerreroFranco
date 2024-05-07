import json

def abrirArchivo():
    with open("clientes.json","r") as openfile:##CREO LA FUNCION DE ABRIR EL JSON
        jsoon=[]
        jsoon=json.load(openfile)
        return jsoon
    
def guardarArchivo(miData):
    with open("clientes.json","w") as outfile:##CREO LA FUNCION DE GUARDAR ARCHIVOS DENTRO DEL JSON
        json.dump(miData,outfile)

hola=True
while hola:
    print("--------------------------------")##bienvenida al usuario
    print(" BIENVENIDO AL SERVICIO MOVISTAR")
    print("--------------------------------")
    print("")

    print("ESCOGE LA OPCION ENUMERADA")
    queRol=input("que rol cumples dentro de movistas\n1.administrador\n2.cliente :")##pregunto que rol desea utilizar
    if queRol=="1":
        jsoon=abrirArchivo()
        print("-------------------------")
        print(" BIENVENIDO ADMINISTRADOR")
        print("-------------------------")        
        print("")
        print("1.ingresar un nuevo cliente")
        print("2.ver reportes")
        queopcio=input("que opcion desea realizar :")
        if queopcio=="1":
            jsoon=abrirArchivo()
            print("")
            print("-----------------------------------------------------")
            print(" LISTA DE CLIENTES QUE SE DESEAN ADQUIRIR EL SERVICIO")
            print("-----------------------------------------------------")        
            for i in jsoon[0]["posiblesCli"]:
                contador=0
                print("id :",i["id"])
                print("nombre :",i["nombre"])
                print("apellido :",i["apellido"])
                print("cedula :",i["cedula"])
                print("numero de telefono :",i["numero"])
                print("años desea :",i["desea"])
                print("")
                queCliente=int(input("que cliente va a revisar :"))
                print("un año de plan tiene un valor de 20.000$$")
                print("el cliente desea adquirir in plan de:",i["desea"])

                cancelo=input("el cliente ya pago el tiempo que desea adquirir el servicio si/no? :")
                if cancelo=="si":
                    jsoon=abrirArchivo()
                    nuevoEstado="en servicio"
                    jsoon[0]["posiblesCli"][cliente-1]["estado"] = nuevoEstado
                    guardarArchivo()

                elif cancelo=="no":
                    jsoon=abrirArchivo()
                    nuevoEstado="no disponible"
                    jsoon[0]["posiblesCli"][cliente-1]["estado"] = nuevoEstado
                    guardarArchivo()
            
        if queopcio=="2":
            print("")
            print("----------------------------------")
            print(" LISTA DE REPORTES DE LOS CLIENTES")
            print("----------------------------------") 
            print("")  
            print("INGRESE LA OPCION ENUMERADA")
            queReportes=input("1.ver clientes que desean adquirir servicios\n2.ver clientes que tienes quejas\n3.clientes con bajo uso del servicio :")  
            if queReportes=="1":
                jsoon=abrirArchivo()
                print("")
                print("------------------------------------------")
                print(" CLIENTES QUE QUIEREN ADQUIRIR EL SERVICIO")
                print("-------------------------------------------") 
                print("")  
                for i in jsoon[0]["posiblesCli"]:
                    print("id :",i["id"])
                    print("nombre :",i["nombre"])
                    print("apellido :",i["apellido"])
                    print("cedula :",i["cedula"])
                    print("numero de telefono :",i["numero"])
                    print("años desea :",i["desea"])
                    print("")
            if queReportes=="2":
                jsoon=abrirArchivo()
                print("")
                print("---------------------------")
                print(" CLIENTES QUE TIENEN QUEJAS")
                print("---------------------------") 
                print("")  
                
                deQuetipo=input("de que tipo de cliente \n1.cliente nuevo\n2.cliente con tiempo\n3.cliente antiguo :")
                if deQuetipo=="1":
                    jsoon=abrirArchivo()
                    for i in jsoon[0]["posiblesCli"]:
                        print("id :",i["id"])
                        print("nombre :",i["nombre"])
                        print("apellido :",i["apellido"])
                        print("cedula :",i["cedula"])
                        print("numero de telefono :",i["numero"])
                        print("quejas :",i["queja"])
                        print("")
                if deQuetipo=="2":
                    jsoon=abrirArchivo()
                    for i in jsoon[1]["clientes"]:
                        print("id :",i["id"])
                        print("nombre :",i["nombre"])
                        print("apellido :",i["apellido"])
                        print("cedula :",i["cedula"])
                        print("numero de telefono :",i["numero"])
                        print("quejas :",i["queja"])
                        print("")
                if deQuetipo=="3":
                     jsoon=abrirArchivo()
                     for i in jsoon[2]["clientes"]:
                        print("id :",i["id"])
                        print("nombre :",i["nombre"])
                        print("apellido :",i["apellido"])
                        print("cedula :",i["cedula"])
                        print("numero de telefono :",i["numero"])
                        print("quejas :",i["queja"])
                        print("")

            if queReportes=="3":
                print("")
                print("-----------------------------------")
                print(" CLIENTES QUE USAN POCO EL SERVIVIO")
                print("-----------------------------------")     
                print("")

                deQuetipo=input("de que tipo de cliente \n1.cliente nuevo\n2.cliente con tiempo\n3.cliente antiguo :")
                if deQuetipo=="1":
                     jsoon=abrirArchivo()
                     for i in jsoon[0]["posiblesCli"]:
                        print("id :",i["id"])
                        print("nombre :",i["nombre"])
                        print("apellido :",i["apellido"])
                        print("cedula :",i["cedula"])
                        print("numero de telefono :",i["numero"])
                        print("uso :",i["uso"])
                        print("")
                        print("INGRESE LA OPCION ENUMERADA")
                        uso=input("que uso tiene el cliente 1.poco\n2.buen uso")
                        if uso=="1":
                            print("")
                            print("LLAMANDO AL CLIENTE")
                            print("")
                            print("#protoclo de llamda")
                            print("saludalo y dile que ofresele el plan")
                            queeee=input("que cliente si quiso que se le aplicara el plan si/no :")

                            if queeee=="si":
                                planNuevo="mejorado"
                                jsoon[0]["posiblesCli"][cliente-1]["plan"] = planNuevo
                                guardarArchivo()
                            if queeee=="no":
                                print("")
                        if uso=="2":
                            print("siguele monitoriando el uso para que no baje")

                if deQuetipo=="2":
                     jsoon=abrirArchivo()
                     for i in jsoon[1]["clientes"]:
                        print("id :",i["id"])
                        print("nombre :",i["nombre"])
                        print("apellido :",i["apellido"])
                        print("cedula :",i["cedula"])
                        print("numero de telefono :",i["numero"])
                        print("uso :",i["uso"])
                        print("")
                        print("INGRESE LA OPCION ENUMERADA")
                        uso=input("que uso tiene el cliente 1.poco\n2.buen uso")
                        if uso=="1":
                            print("")
                            print("LLAMANDO AL CLIENTE")
                            print("")
                            print("#protoclo de llamda")
                            print("saludalo y dile que ofresele el plan")
                            queeee=input("que cliente si quiso que se le aplicara el plan si/no :")

                            if queeee=="si":
                                planNuevo="mejorado"
                                jsoon[1]["clientes"][cliente-1]["plan"] = planNuevo
                                guardarArchivo()
                            if queeee=="no":
                                print("")
                        if uso=="2":
                            print("siguele monitoriando el uso para que no baje")

                if deQuetipo=="3":
                     jsoon=abrirArchivo()
                     for i in jsoon[2]["clientes"]:
                        print("id :",i["id"])
                        print("nombre :",i["nombre"])
                        print("apellido :",i["apellido"])
                        print("cedula :",i["cedula"])
                        print("numero de telefono :",i["numero"])
                        print("uso :",i["uso"])
                        print("")

                        print("INGRESE LA OPCION ENUMERADA")
                        uso=input("que uso tiene el cliente 1.poco\n2.buen uso")
                        if uso=="1":
                            print("")
                            print("LLAMANDO AL CLIENTE")
                            print("")
                            print("#protoclo de llamda")
                            print("saludalo y dile que ofresele el plan")
                            queeee=input("que cliente si quiso que se le aplicara el plan si/no :")

                            if queeee=="si":
                                planNuevo="mejorado"
                                jsoon[2]["clientes"][cliente-1]["plan"] = planNuevo###################
                                guardarArchivo()
                            if queeee=="no":
                                print("")
                        if uso=="2":
                            print("siguele monitoriando el uso para que no baje")

    if queRol=="2":
        print("")
        print("-------------------")
        print(" BIENVENIDO CLIENTE")
        print("-------------------")     
        print("")
        siNo=input("tienes alguna queja con el servivio ofrecido si/no :")

        if siNo=="si":
            jsoon=abrirArchivo()
            print("")
            print("INGRESE LA OPCIO ENUMERADA")
            queTiempo=input("que tipo de cliente eres \n1.cliente nuevo\n2.cliente con tiempo\n3.cliente antiguo :")
            if queTiempo=="1":
                jsoon=abrirArchivo()
                print("wow")
                print("eres un cliente nuevo")
                print("")
                
                contador=0
                for i in jsoon[0]["posiblesCli"]:
                    print("id :",i["id"])
                    print("nombre :",i["nombre"])
                    print("apellido :",i["apellido"])
                    print("cedula :",i["cedula"])
                    print("numero de telefono :",i["numero"])
                    print("años desea :",i["desea"])
                    print("")
                    
                    esUsted=input("este es usted si/no :")
                    if esUsted=="si":
                        queQueja=input("que queja tiene contra el servicio que se le esta ofreciendo :")
                        jsoon[0]["posiblesCli"][cliente-1]["queja"] = queQueja
                        guardarArchivo()

                    elif esUsted=="no":
                        print("")
            
            if queTiempo=="2":
                jsoon=abrirArchivo()
                print("wow")
                print("eres un cliente con un poco tiempo")
                print("")
                
                contador=0
                for i in jsoon[1]["clientes"]:
                    print("id :",i["id"])
                    print("nombre :",i["nombre"])
                    print("apellido :",i["apellido"])
                    print("cedula :",i["cedula"])
                    print("numero de telefono :",i["numero"])
                    print("años desea :",i["desea"])
                    print("")
                    
                    esUsted=input("este es usted si/no :")
                    if esUsted=="si":
                        queQueja=input("que queja tiene contra el servicio que se le esta ofreciendo :")
                        jsoon[1]["clientes"][cliente-1]["queja"] = queQueja
                        guardarArchivo()

                    elif esUsted=="no":
                        print("")
                        
                if queTiempo=="2":
                    jsoon=abrirArchivo()
                    print("wow")
                    print("eres un cliente antiguo")
                    print("")
                    
                    contador=0
                    for i in jsoon[2]["clientes"]:
                        print("id :",i["id"])
                        print("nombre :",i["nombre"])
                        print("apellido :",i["apellido"])
                        print("cedula :",i["cedula"])
                        print("numero de telefono :",i["numero"])
                        print("años desea :",i["desea"])
                        print("")
                        
                        esUsted=input("este es usted si/no :")
                        if esUsted=="si":
                            queQueja=input("que queja tiene contra el servicio que se le esta ofreciendo :")
                            jsoon[2]["clientes"][cliente-1]["queja"] = queQueja
                            guardarArchivo()

                        elif esUsted=="no":
                            print("")