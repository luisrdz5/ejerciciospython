import conectviva


br = conectviva.realizarconexion()
respuesta = br.open('https://www.vivaaerobus.com/mx')
conectviva.generararchivo(respuesta.read(),'prueba1.txt')
#obtengo la forma
br.select_form(nr=0)
print br.form
#print br.form['DepartureCity']

#control = br.form["DepartureCity"]



#for item in control.items:
#	print item.name

#obtengo el campo de origen


#obtengo el campo destino 

#cierro conexion
br.close()

