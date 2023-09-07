import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (('Chewbacca', 'Wookie', 'chewie@gmail.com', 1), ('ghj', 'ghjiy', 'sdfghj@gmail.com', 0))
            cursor.executemany(sentencia, valores)
            registros_act = cursor.rowcount
            print(f'Registros actualizados: {registros_act},{valores}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
