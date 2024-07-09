import os
import psycopg2
from flask import g
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

DATABASE_CONFIG = {
    'user': os.getenv('PGSQL_USER'),
    'password': os.getenv('PGSQL_PASSWORD'),
    'host': os.getenv('PGSQL_HOST'),
    'database': os.getenv('PGSQL_DATABASE'),
    'port': os.getenv('PGSQL_PORT')
}

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(**DATABASE_CONFIG)
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)


##################

def testear_conexion():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()
    conn.commit()
    cur.close()
    conn.close()

def crear_tabla_tragos():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE tragos (
            id SERIAL PRIMARY KEY,
            codigo VARCHAR(50) NOT NULL,
		    nombre VARCHAR(50) NOT NULL,
            instrucciones VARCHAR(800) NOT NULL,
			vaso VARCHAR(50) NOT NULL,
			imagen VARCHAR(200) NOT NULL,
			alcohol VARCHAR(50) NOT NULL,
            categoria VARCHAR(50) NOT NULL
        );
        """
        #activo BOOLEAN NOT NULL
    )
    conn.commit()
    cur.close()
    conn.close()
