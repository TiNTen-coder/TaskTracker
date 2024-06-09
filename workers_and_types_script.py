import psycopg2


# from pprint import pprint

def workers_and_types_script():
    try:
        conn = psycopg2.connect("dbname = 'db_user' user = 'postgres' host='localhost' password='0852'")
    except:
        print('Undefined error')

    with conn.cursor() as curs:
        try:
            # Test fill
            """
            for i in range(ord('A'), ord('Z') + 1):
                curs.execute(f"INSERT INTO user_type (user_id,user_type) VALUES ({i - ord('A')},'{chr(i)}')")
            """
            # Select all rows from user_type
            curs.execute('SELECT * FROM user_type')
            # fetch all of them
            single_row = curs.fetchall()
            yield single_row
        except:
            print('Undefined error')

# pprint(list(workers_and_types_script()))
