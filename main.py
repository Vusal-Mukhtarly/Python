#Подключаем нужные библиотеки
import psycopg2

try:
    #Пытаемся подключиться к БД
    conn = psycopg2.connect(
        host = '89.179.245.134',
        port = '5432',
        dbname = 'postgres',
        user = 'postgres',
        password = 'postgres')
    print('Подключение установлено')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM public.user_id')
    all_users = cursor.fetchall()
    print(all_users)

except:
    #Выводим сообение, если подключение не удалось
    print('Подключение не удалось')

finally:
    if conn:
        cursor.close()
        conn.close()