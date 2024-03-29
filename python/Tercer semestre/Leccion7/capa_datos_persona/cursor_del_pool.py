from conexion import Conexion
from logger_base import *


class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None


    def __enter__(self):
        log.debug(f'Inicio del metodo with y __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug('Se ejecuta el metodo exit__')
        if exc_val:
            self._conexion.rollback()
            log.debug(f'Ocurrio una excepcion {exc_val}')
        else:
            self._conexion.commit()
            log.debug('commit de la transaccion')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

        if __name__ == '__main__':
            with CursorDelPool() as cursor:
                log.debug('dentro del bloque with')
                cursor.execute('SELECT * FROM persona')
                log.debug(cursor.fetchall())


