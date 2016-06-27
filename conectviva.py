import mechanize 
import cookielib

#abro pagina de viva
def realizarconexion():
	br = mechanize.Browser()
	# Se crea la instancia del cookie
	cj = cookielib.LWPCookieJar()
	#Se asocia la instancia del cookie con el navegador
	br.set_cookiejar(cj)
	#Se define que no se maneja robots:
	br.set_handle_robots(False)
	#Se define el tiempo de refrescamiento:
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    #Se definen los encabezados del navegador
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; es-VE; rv:1.9.0.1)Gecko/2008071615 Debian/6.0 Firefox/9')]
	return br
def generararchivo(texto, nombrearchivo):
	archivo = open(nombrearchivo,'a')
	archivo.write(texto)
	archivo.close()




	