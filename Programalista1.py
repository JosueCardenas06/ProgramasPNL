semana_laboral=["Lunes","Martes","Miercoles","Jueves","Viernes"]
print("semana_laboral=", semana_laboral)
print("Dia 1=",semana_laboral[4])
semana_laboral[4]="Sabado"
print("semana_laboral=", semana_laboral)
semana_laboral[4]="Viernes"
longitud_lista=len(semana_laboral)
print("longitud= ",longitud_lista)
posicion=semana_laboral.index("Miercoles")
print("posicion de Miercoles= ", posicion)
semana_laboral.append("Sabado")

