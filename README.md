Spotify ETL - Canciones más escuchadas.

Introducción

Este proyecto busca las canciones más escuchadas del usuario usando la API de Spotify y el paquete Spotipy.

Prerequisitos

Se debe crear una aplicación en la siguiente pagina:

https://developer.spotify.com/dashboard/applications

Luego ingresar a la aplicación creada, obtener las key "Client ID" y "Client Secret" e ingresarlas en el archivo settings.ini

Después ingresar a "Edit Settings" agregar una dirección la cual puede ser tipo "http://ejemplo.com" el cual no es necesario que exista, solo se usará al momento de ejecutar el archivo main.py, el cual solicitará ingresar el link generado que se abrirá en el navegador que servirá como autenticación la primera vez, más información en la siguiente pagina.

https://spotipy.readthedocs.io/en/master/#quick-start

Luego instalar los paquetes requeridos con la herramienta spip, en el archivo requierements se encuentran todos los paquetes requeridos y se pueden instalar con el siguiente comando:

pip install -r /path/to/requirements.txt

Creación DB

Para este proyecto se debe crear un DB en postgres el cual se creará con docker con el siguiente comando:

docker run -d --name spotify_etl_pg -v db_spotify:/var/lib/postgresql/data -p 5432:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=spotify_data postgres

Para acceder a la DB se debe realizar con el siguiente comando:

docker exec -it spotify_etl_pg psql -U postgres -d spotify_data

Opcional

Se recomienda crear un entorno virtual con los siguientes comandos:

python -m venv myenvSpotify\
.\myenv\Scripts\Activate.ps1
pip install ipykernel
python -m ipykernel install --user --name=myenvSpotify

Ejecutar proyecto

Se debe ejecutar el archivo main.py el cual acepta la opcion "--day" cuyo número es un entero positivo y y por defecto es 10. Sirve para indicar a cuantos días atras traerá la información de las últimas canciones escuchadas  Ejemplo:

Obtener las canciones de los últimos 5 días.
python.exe main.py --day 5
