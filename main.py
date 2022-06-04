#  Librerias necesarias
import requests
import funcs
from bs4 import BeautifulSoup
from base64 import b64decode


def descargar_las(usuario, contrasena):
    '''
    Esta funcion descarga un PDF con el resultado, Se limita a 1 página.
    '''
    data = {
        'cod_cliente': usuario,
        'clave_reporte': contrasena,
        'pagina': '1',
    }

    url = "https://www.laboratoriosanaliticosdelsur.com/ie/listado_reportes.php"
    headers = funcs.get_user_agent()
    #  1. Obtener PDF
    store = requests.post(url, headers=headers, data=data)
    s = BeautifulSoup(store.text, 'lxml')
    tds = s.find('table', attrs={'class': 'table table-bordered'}).find('tbody').find_all('td')
    file_base64 = tds[3].a.get('href').replace('data:application/octet-stream;base64, ', '')
    file_pdf = b64decode(file_base64)
    filename = user + '_' + password

    #  2. Descargar PDF
    requests.post(f'https://api.telegram.org/bot{bot}/sendMessage',
                data={'chat_id': chat_id,
                    'text':
                        'descargando...'
                   })
    with open(f'{filename}.pdf', 'wb') as writer:
        writer.write(file_pdf)
       
    return
