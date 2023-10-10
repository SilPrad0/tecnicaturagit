import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = ('Luke', 'Skywalker', 'manorobotica@gmail.com')  #tupla
            cursor.execute(sentencia, valores) # asi ejecutamos la sentencia
            registros_ins = cursor.rowcount
            print(f'Los registros insertados son: {registros_ins}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
