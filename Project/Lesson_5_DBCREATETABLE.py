import pymysql

schema_name = "freedb_Yaniv_DB"

# Establishing a connection to DB
conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_Yaniv', passwd='!Q4QHwpt$SSzZbp',
                       db="freedb_Yaniv_DB")
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

#Create table op
statementToExecute = "CREATE TABLE `" + schema_name + "`.`users`(`id` INT NOT NULL,`name` VARCHAR(45) NOT NULL," \
                                                      "creation_date datetime default now(), PRIMARY KEY (`id`)); "
#statementToExecute ="CREATE TABLE " + schema_name + ".dogs( name VARCHAR(45) NOT NULL,age INT NOT NULL,breed VARCHAR(30) NOT NULL, PRIMARY KEY (name))"
#statementToExecute = "DROP TABLE users"
# statementToExecute = "CREATE TABLE `"+schema_name+"`.`users`(`id` INT NOT NULL,`first_name` VARCHAR(45) NOT NULL,`last_name` VARCHAR(45) NULL,'User_Id' INT NOT NULL,'Domain' VARCHAR(45)  DEFAULT `DOMAIN` , PRIMARY KEY (`id`));"

cursor.execute(statementToExecute)

cursor.close()
conn.close()
