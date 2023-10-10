import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona IN (1, 2, 3)'
            entrada = input('Digite el numero id: ')
            llaves_primarias = (tuple(entrada.split(', ')), )
            cursor.execute(sentencia, llaves_primarias) # asi ejecutamos la sentencia
            registros = cursor.fetchall()  #recuperamos todos los registros que seran una lista
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
