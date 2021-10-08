# accumulated-per-day-table
Codigo para calcular los ingresos y salidas totales desde postgreSQL

## Requisitos:
```
sudo apt install python3-pip
git clone https://github.com/ClaudioCampuzano/accumulated-per-day-table.git && cd accumulated-per-day-table
virtualenv env --python=python3 && source env/bin/activate
pip3 install -r requeriments.txt
```

## Ejecución:
```
source env/bin/activate
python3 SQLsuma.py -d MM/DD/YYYY -i ID_MALL
```
