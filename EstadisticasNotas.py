#Dados los números de alumnos con suspenso, aprobados, notables y sobresalientes, sacar el porcentaje
#a)El tanto de alumnos que han superado la asignatura
#b)El porcentajes de alumnos que han suspendido, aprobado, con notables y con sobresalientes por serapado.
print ("Creado por Daniela Valentina De Nóbrega")
#Introducir los números de cada que desee:
NumSuspensos = 3
NumAprobados = 4
NumNotables = 3
NumSobresalientes = 3
#Número total de alumnos
Total = NumSuspensos + NumAprobados + NumNotables + NumSobresalientes

#a)
#Calculamos el porcentaje
NumAlumAprobados = (( NumAprobados + NumNotables + NumSobresalientes) / Total ) * 100

print ( "Ha superado la asignatura el", round (NumAlumAprobados) , "% de alumnos.")

#b)
PorcenSuspensos = ( NumSuspensos / Total ) * 100
PorcenAProbados =( NumAprobados / Total ) * 100
PorcenNotables = ( NumNotables / Total ) * 100
PorcenSobre = ( NumSobresalientes / Total ) * 100

print ( "Ha suspendido el" , round (PorcenSuspensos ) , "% de alumnos.")
print ( "Ha sacado aprobado el" , round (PorcenAProbados) , "% de alumnos.")
print ( "Ha sacado notable el" , round (PorcenNotables) , "% de alumnos.")
print ( "Ha sacado sobresaliente el" , round (PorcenSobre) , "% de alumnos.")