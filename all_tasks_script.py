import psycopg2


# from pprint import pprint

def all_tasks_script():
    try:
        conn = psycopg2.connect("dbname = 'db_task' user = 'postgres' host='localhost' password='0852'")
    except:
        print('Undefined error')

    with conn.cursor() as curs:
        try:
            # Test fill
            """
            for i in range(ord('A'), ord('Z') + 1):
                curs.execute(
                    f"INSERT INTO task_info (task_id,task_name,task_supervisor,task_workers,percent) VALUES ({i - ord('A')},'{chr(i)}',1,ARRAY[1, 2, 3],10)")
            for i in range(ord('A'), ord('Z') + 1):
                curs.execute(
                    f"INSERT INTO task_entry (entry_id,task_id,workers_id,entry_description,percent,date) VALUES ({i - ord('A')},'{i - ord('A')}',{(i - ord('A')) % 3},'ROFLS',10,'2024-02-02')")
            """
            # Select all rows from task_info
            curs.execute('SELECT * FROM task_info')
            # fetch all of them
            q = curs.fetchall()
            for i in q:
                # Select rows which we need with rule
                curs.execute(f"SELECT * FROM task_entry WHERE (task_id = {i[0]})")
                yield (i, curs.fetchall())
        except:
            print('Undefined error')

# pprint(list(all_tasks_script()))
