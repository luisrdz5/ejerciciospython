import conectviva


br = conectviva.realizarconexion()
respuesta = br.open('https://www.vivaaerobus.com/mx')
conectviva.generararchivo(respuesta.read(),'prueba1.txt')
#obtengo la forma
#for form in br.forms():
#	print form
forma=br.select_form(nr=0)
print forma.name

#obtengo el campo de origen


#obtengo el campo destino 

#cierro conexion
br.close()

