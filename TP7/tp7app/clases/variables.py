
#Estados Zapatero

libre = "L"
atendiendo_pedido = "AP"
atendiendo_retiro = "AR"
reparando = "R"

#Estados cliente

siendo_at_pedido = "SAP"
siendo_at_retiro = "SAR"
esperando_retiro = "EPR"
esperando_pedido = "EPP"
abandono_sin_zapato = "ASZ"
abandono_cierre_local = "ACL"


#Estados Zapatos

siendo_reparados = "SR"
reparados = "RL"  #Reparacion Lista
esperando_reanudacion_reparacion = "ERR"
esperando_reparo = "ER"



#Estado cuando se van del sistema

fuera_sistema = "-"


#Acciones del cliente

retirar = "Retirar"
pedido = "Pedido"


#Nombre eventos

eventoInicializacion = "#######inicializacion#######"
eventoLlegadaClientes = "llegada_cliente"
eventoFinAtencionCliente = "fin_atencion_cliente"
eventoFinReparacion = "fin_reparacion"
eventoLlegadaInterrupcion = "#CIERRE#_zapateria"
eventoFinInterrupcion = "#APERTURA#_zapateria"