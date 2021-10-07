import psycopg2
from psycopg2 import extras
from psycopg2 import sql
import argparse

def connect(params_dic):
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(end=" ")
    #print("Connection successful PostgreSQL")
    return conn

def recoverData(param_dic, tableName, mallId, date):
    queryText = "SELECT * FROM {TABLA} WHERE id_cc='{MALLID}' AND fecha='{FECHA}';".replace('{TABLA}',tableName).replace('{MALLID}',mallId).replace('{FECHA}',date)
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
        ins += int(record[7])
        outs += int(record[8])
    print('Ingresos: '+ str(ins))
    print('Salidas: '+ str(outs))


def main(mallId,date):
    param_dic = {
        "host": "192.168.0.127",
        "database": "dk_omia",
        "user": "postgres",
        "password": "Video2021$"
    }
    tableName='ingreso_persona'

    recoverData(param_dic, tableName, mallId, date)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Small program to sum the inputs and outputs of a table in postgreSQL')
    parser.add_argument('-i', '--mall_id', type=str, default='1', required=True, help='value of mallId')
    parser.add_argument('-d', '--date', type=str, default='09/13/2021', required=True, help='date in format MM/DD/YYYY')
    args = parser.parse_args()

    main(args.mall_id,args.date)
