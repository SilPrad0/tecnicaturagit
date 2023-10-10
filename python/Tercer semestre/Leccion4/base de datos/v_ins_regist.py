import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = (('Etc', 'Etc', 'etc@gmail.com'),
                       ('Luke', 'Skywalker', 'manorobotica@gmail.com'),
                       ('Leia', 'Organa', 'leia@gmail.com'))  #tupla de tuplas
            cursor.executemany(sentencia, valores) # asi ejecutamos la sentencia
            registros_ins = cursor.rowcount
            print(f'Los registros insertados son: {registros_ins},{valores}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
