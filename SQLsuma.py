import psycopg2
from psycopg2 import extras
from psycopg2 import sql


param_dic = {
    "host": "192.168.0.127",
    "database": "dk_omia",
    "user": "postgres",
    "password": "Video2021$"
}

tableName='visitantes_totales'
mallId='3'
fecha='09/13/2021'

def connect(params_dic):
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(end=" ")
    #print("Connection successful PostgreSQL")
    return conn

def recoverData():
    global param_dic, tableName, mallId, fecha
    queryText = "SELECT * FROM {TABLA} WHERE id_cc='{MALLID}' AND fecha='{FECHA}';".replace('{TABLA}',tableName).replace('{MALLID}',mallId).replace('{FECHA}',fecha)
    try:
        conn = connect(param_dic)
        if conn is None:
            raise ValueError('Error when trying to connect to the DB ...')
        cur = conn.cursor()
        cur.execute(queryText)
        recordDB = cur.fetchall()        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    ins, outs = 0,0
    for record in recordDB:
        ins += int(record[6])
        outs += int(record[7])
    print('Ingresos: '+ str(ins))
    print('Salidas: '+ str(outs))

recoverData()
