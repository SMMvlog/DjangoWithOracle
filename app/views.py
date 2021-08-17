from django.shortcuts import render
from django.db import connection
from .models import Teacher
import cx_Oracle
import os
import config as cfg

# username = 'system'
# password = '12345'
# dsn = 'localhost/pdborcl'
# port = 1512
# encoding = 'UTF-8'

def store_procedure(request):
    # cursor = connection.cursor()
    # cursor.callproc('call sp_AllNew',{id:1})
    # cursor.execute('call sp_AllNew(2)')
    # result = cursor.fetchall()
    # result = Teacher.objects.raw(f'call sp_All({1})')
    # cursor.close()
    # result=Teacher.objects.raw(f'{Execute} sp_All(1)')
    # result=Teacher.objects.raw('Execute sp_All(1)')


    # con = cx_Oracle.connect('system/12345@localhost/orcl')
    # cur = con.cursor()
    # name = cur.var(cx_Oracle.NCHAR)
    # result=cur.callproc('sp_New')
    # print(result)
    # # print(result)
    # print('name',name.getvalue())
    # # print(result)
    # cur.close()
    """
    Get order count by salesman and year
    :param salesman_id:
    :param year:
    :return: the number of orders by a salesman and year
    """
    
    
    # try:
    #     username = 'system'
    #     password = '12345'
    #     dsn = 'localhost/pdborcl'
    #     port = 1512
    #     # create a connection to the Oracle Database
    #     # with cx_Oracle.connect(cfg.username,
    #     #                     cfg.password,
    #     #                     cfg.dsn,
    #     #                     encoding=cfg.encoding) as connection:
    #         # create a new cursor

    #     with cx_Oracle.connect(username,
    #                         password,
    #                         dsn) as connection:
            # create a new cursor
            # with connection.cursor() as cursor:
            #     print("yes")
            #     # create a new variable to hold the value of the
            #     # OUT parameter
            #     order_count = cursor.var(cx_Oracle.CURSOR)
            #     # call the stored procedure
            #     cursor.callproc('sp_AllNew',
            #                      [2])
            #     order_count.getvalue()
    # with cx_Oracle.connect('system/12345@localhost/orcl') as connection:
    #     with connection.cursor() as cursor:
    #         print("yes")
    #         # create a new variable to hold the value of the
    #         # OUT parameter
    #         name = cursor.var(cx_Oracle.CURSOR)
    #         cursor.callproc('sp_AllNew',
    #                         [1])
            
    #         print( name.fetchall())
            # call the stored procedure
            
            # print(name.getvalue())
    #     return render(request,'home.html')
    # except cx_Oracle.Error as error:
    #     print(error)


#     con = cx_Oracle.connect('system/12345@localhost:1521/orcl')
#     cur = con.cursor()
# #     cur.callproc('sp_AllNew',[1])
# #     name = cur.var(cx_Oracle.NCHAR)
#     cur.callproc("sp_New()")

    # connectString = os.getenv('system/12345@localhost:1521/orcl')
    






    
    
    # cur = cx_Oracle.connect('system/12345@localhost:1521/orcl')
    # cur = con.cursor()
# #     cur.callproc('sp_AllNew',[2])
#     sqlp = "call sp_AllNew(2)"
#     result=cur.execute(sqlp) 
#     print(result)


    # cursor = cx_Oracle.connect('system/12345@localhost:1521/orcl')
    # cur = connection.cursor()

    # cur_var=cur.var(cx_Oracle.CURSOR)
    # name= cur.var(cx_Oracle.NCHAR)
    # # print("name:",name)
    # teacher_id= cur.var(cx_Oracle.NCHAR)
    # teacher_location= cur.var(cx_Oracle.NCHAR)
    # cur.callproc('getAll',[3,name,teacher_id,teacher_location])
    # print(name.getvalue())
    # print(teacher_id.getvalue())
    # print(teacher_location.getvalue())

    

    # teach = cur.var(cx_Oracle.CURSOR)
    # teach_id = cur.var(cx_Oracle.NUMBER)
    # teach_id = cur.var(cx_Oracle.NUMBER)
    # # print("id:",id)
    # # l.append(id)  
    # teacher_name = cur.var(cx_Oracle.CURSOR)
    # teacher_name = cur.var(cx_Oracle.NCHAR)
    # # print("name:",name)
    # # l2.append(name)
    # teacher_id = cur.var(cx_Oracle.CURSOR)
    # teacher_id = cur.var(cx_Oracle.NCHAR)
    # # print("t_id:",t_id)
    # # l3.append(t_id)
    # teacher_location = cur.var(cx_Oracle.CURSOR)
    # teacher_location = cur.var(cx_Oracle.NCHAR)
    # # print("location:",location)
    # # l4.append(location)
    # cur.fetchall()

################### wright for single value #############################################

    connection = cx_Oracle.connect(user="system", password="12345",dsn="localhost:1521/orcl")
    cur = connection.cursor()
    teacher_name = cur.var(str)
    teacher_id = cur.var(str)
    teacher_location = cur.var(str)
    cur.callproc("getAll",[1,teacher_name,teacher_id,teacher_location]) 
    print(teacher_name.getvalue())
    print(teacher_id.getvalue())
    print(teacher_location.getvalue())

#######################################################################################





#######################  Wright #############################################################
    
    # connection = cx_Oracle.connect(user="system", password="12345",dsn="localhost:1521/orcl")
    # cur = connection.cursor()
    # ref_cursor = connection.cursor()
    # cur.callproc("sp_New",[ref_cursor])
    # for row in ref_cursor:
    #    print(row)

##############################################################################################

    # cur.callproc("sp_New1",['mumbai',ref_cursor])
    # for row in ref_cursor:
    #    print(row)

    
    # for row in ref_cursor:
    #     print(row)
    
    # for row in cur.fetchmany:
    #     print(row)
    
    # print(teacher_location.getvalue())
    # result = cur.fetchmany()
    # print(result)
    
    # for i in cur.fetchmany():
    #     pass
    # print(teach_id.getvalue())
    # print(teacher_name.getvalue())
    # print(teacher_id.getvalue())
    # print(teacher_location.getvalue())

    # cur=connection.cursor()
    # cur.execute("SELECT * FROM App_Teacher")
    # result = Teacher.objects.all()
    # for i in result:
    #     print(i.t_name+" "+i.t_id+" "+i.location)



    # connection = cx_Oracle.connect(user="system", password="12345",dsn="localhost:1521/orcl")
    # cur = connection.cursor()
    # cur.callproc("sp_New",[ref_cursor])




     

    return render(request, 'home.html')
