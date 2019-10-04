import numpy as np

rut_pacientes = np.empty(50, dtype='object')
for i in range(0,50):
    rut_pacientes[i] = "Vacio"    #la lista es de 50 , pero se puede cambiar
genero_pacientes = np.empty(50, dtype='object')
nombre_p = np.empty(50, dtype='object')
apeliido_p = np.empty(50, dtype='object')
estadocivil_p = np.empty(50, dtype='object')
domicilio_p = np.empty(50, dtype='object')
fono_p = np.empty(50, dtype='object')
grupo_sanguineo = np.empty(50, dtype='object')
urgencia_nivel = np.empty(50, dtype='object')
edad_pacientes = np.empty(50, dtype='object')
medicamento_pacientes = np.empty(50, dtype='object')


descripcion_paciente = np.empty(5, dtype='object')
                    
n_medic = np.empty(50, dtype='object')
especialidad = np.empty(50, dtype='object')
sintomas_medic = np.empty(50, dtype='object')
asignar_medic = np.empty(50, dtype='object')
                    
nombre_medicamento = np.empty(50, dtype='object')
dosis = np.empty(50, dtype='object')
cantidad_dias = np.empty(50, dtype='object')

diagnostico_1 = np.empty(50, dtype = 'object')
diagnostico_2 = np.empty(50, dtype = 'object')
diagnostico_3 = np.empty(50, dtype = 'object')
diagnostico_4 = np.empty(50, dtype = 'object')
diagnostico_5 = np.empty(50, dtype = 'object')

def MenuPacientes():
    print('''MENU
    1)Ingresar paciente
    2)Buscar Paciente por rut
    3)Buscar medicamentos del paciente
    4)Eliminar ficha de paciente
    5)Lista de pacientes 
    6)Salir\n''')

def AgregarPacientes():
    c = 0
    
    if c >= len(rut_pacientes): #hace el conteo , si excede la cantidad permitida tira el error
        print("Excede la cantidad de personas")
    else:
        disponible = False #buscamos el primer NONE disponible , para que ocupe el lugar desocupado
        for i in range(0,50):
            if rut_pacientes[i] == "Vacio":
                disponible = True #de ser verdadera, ingresaremos los datos
                rut_pacientes[i] = input("Ingrese su rut: ")
                while len(rut_pacientes[i]) <=6 or len(rut_pacientes[i]) >9:
                    rut_pacientes[i] = input(" Ingrese rut valido sin digito verificador y de 8-9 digitos: ")
                nombre_p[i] = input("Ingrese su nombre: ")
                apeliido_p[i] = input("Ingrese el apellido: ")
                estadocivil_p[i] =input("Ingrese el estado civil: ")
                domicilio_p[i] = input("Ingrese el domicilio: ")
                fono_p[i] = input("Ingrese su telefono: ")
                genero_pacientes[i] = input("Ingrese genero f o m: ")
                edad_pacientes[i] = input("Ingrese la edad: ")
                grupo_sanguineo[i] = input("Ingrese el grupo sanguineo: ")
                urgencia_nivel[i] = input("Ingrese el nivel de urgencia: ")
                    ### AGREGAR a numpy

                print("MOTIVO DE CONSULTA")
                descripcion_paciente[i] = input("Descripcion del paciente: ")
                print("INFORMACION DE ATENCION")
                n_medic[i] = input("Nombre medico: ")
                especialidad[i] = input("Especialidad: ")
                sintomas_medic[i] = input("Sintomas detectados: ")
                print("INFORMACION DE MEDICAMENTO")
                diagnostico_1[i] = input("Ingrese diagnostico 1: ")
                diagnostico_2[i] = input("Ingrese diagnostico 2: ")
                diagnostico_3[i] = input("Ingrese diagnostico 3: ")
                diagnostico_4[i] = input("Ingrese diagnostico 4: ")
                diagnostico_5[i] = input("Ingrese diagnostico 5: ")
                asignar_medic = input("Medico asigna medicamentos (SI/NO): ")
                if asignar_medic == "si" or asignar_medic == "SI" or asignar_medic == "s":

                    nombre_medicamento[i] = input("Nombre de los medicamentos: ")
                    dosis[i] = input("Dosis: ")
                    cantidad_dias[i] = input("Cantidad de dias: ")
                else:
                    print("Sin medicamentos")

                c = c + 1
                break;

        if disponible == False:
            print("No hay espacio")

def BuscarPacientes():
    print("MOSTRAR")
    encontrar_rut = input("Numero de rut: ")
    indice = -1
    for i in range(0,50):
        if rut_pacientes[i] == encontrar_rut:
            indice = i 
           
    if indice == -1:
        print("No encontrado")
    else:
        print(f"""
        Rut : {rut_pacientes[indice]} 
        Nombre : {nombre_p[indice]} 
        Apellido : {apeliido_p[indice]} 
        Estado civil : {estadocivil_p[indice]} 
        Domicilio : {domicilio_p[indice]}
        Fono : {fono_p[indice]}
        Genero : {genero_pacientes[indice]}
        Edad : {edad_pacientes[indice]}
        Grupo sanguineo: {grupo_sanguineo[indice]}
        Nivel de urgencia : {urgencia_nivel[indice]} """)

def MedicamentosPaciente():
    print("Buscando rut por paciente") 
    encontrar_rut = input("Numero de rut: ")
    indice = -1
    for i in range(0,50):
        if rut_pacientes[i] == encontrar_rut:
                indice = i 
    if indice == -1:
        print("No encontrado")
    else: 
        print(f"""
        Medicamentos : {nombre_medicamento[indice]}
        Diagnosticos: 
        {diagnostico_1[indice]}
        {diagnostico_2[indice]}
        {diagnostico_3[indice]}
        {diagnostico_4[indice]}
        {diagnostico_5[indice]}
        """)


def EliminarPaciente():
    print("Eliminando")
    encontrar_rut = input("Numero del rut: ")
    indice = -1
    for i in range (0,50):
        if rut_pacientes[i] == encontrar_rut:
            indice = i
    if indice == -1:
        print("No encontrado")
    else: 
        rut_pacientes[indice] = "Vacio"


while True:
    MenuPacientes()
    op = int(input())

    if op == 1:
        AgregarPacientes()
    
    elif op == 2:
        BuscarPacientes()

    elif op == 3:
        MedicamentosPaciente()
    
    elif op == 4:
        EliminarPaciente()  

    elif op == 5:
        print(rut_pacientes)

    elif op == 6:
        print("SALIENDO")
        break
    else:
        print("Porfavor digite una opcion valida (1-6)")
