import pymysql

dbhost = "ins-db-cursoaws.cxgoq86c6xdg.us-east-1.rds.amazonaws.com"
dbuser = "admin"
dbpwd = "M4b3lG4352*"
db = "cursoAWS"

try:
    pymysql.connect(
        host =dbhost, 
        user= dbuser, 
        password = dbpwd, 
        database = db
    )
    print("Coneccion exitosa!!!")
except Exception as err:
    print("No conecto, sorry", err)


