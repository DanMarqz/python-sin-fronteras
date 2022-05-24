cosasEnCasa = 'Actualmente tenemos en casa:\n'
listaDeCosas = ['Pollo','Pechuga','Atun','Chuleta','Guisar','Mechada']
listaEnString = ', '.join([str(item) for item in listaDeCosas])
accion = '\nIndique que desea agregar: '

mensajeParaUsuario = cosasEnCasa + listaEnString + accion 

cosa = input( mensajeParaUsuario )

if listaDeCosas.count(cosa) > 0:
    print(cosa + ' ya se encuentra en las cosas que tenemos.')
else: 
    listaDeCosas.append(cosa)
    print('Se agrego '+ cosa +' a la lista. Ahora tenemos:\n' + str(listaDeCosas))