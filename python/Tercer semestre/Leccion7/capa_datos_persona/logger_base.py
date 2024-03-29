import logging as log

# llamamos una configuracion basica
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('Mje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('A nivel warning')
    log.error('a nivel error')
    log.critical('mje a nivel critical')