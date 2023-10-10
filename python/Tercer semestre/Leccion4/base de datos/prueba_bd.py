import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'  #Placeholder
            id_persona = input('digite un numero para el id_persona: ')
            cursor.execute(sentencia, (id_persona,)) # asi ejecutamos la sentencia
            registros = cursor.fetchall()  #recuperamos todos los registros que seran una lista
            print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
