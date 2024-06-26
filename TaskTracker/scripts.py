"""Scripts."""
import psycopg2


# from pprint import pprint

def all_tasks_by_worker_id(worker_id: int):
    """all_tasks_by_worker_id.

    :param worker_id:
    :type worker_id: int
    """
    try:
        conn = psycopg2.connect("dbname = 'db_task' user = 'postgres' host='localhost' password='0852'")
    except Exception as e:
        print(f'Undefined error {e}')

    with conn.cursor() as curs:
        # try:
        # Test fill
        """
        for i in range(ord('A'), ord('Z') + 1):
            curs.execute(f"INSERT INTO task_info (task_id,task_name,task_supervisor,task_workers,percent) VALUES
            ({i - ord('A')},'{chr(i)}',1,ARRAY[1, 2, 3],10)")
        for i in range(ord('A'), ord('Z') + 1):
            curs.execute(f"INSERT INTO task_entry (entry_id,task_id,workers_id,entry_description,percent,date)
             VALUES ({i - ord('A')},'{i - ord('A')}',{(i - ord('A')) % 3},'ROFLS',10,'2024-02-02')")
        """
        # Select all rows from task_info
        curs.execute('SELECT * FROM task_info')
        # fetch all of them
        q = curs.fetchall()
        ans = []
        for i in q:
            if worker_id in i[3]:
                ans.append([i[0], i[1], i[4], i[5], f'Description: {i[6][:-1]}'])
                curs.execute(f"""
                    SELECT workers_id,percent,entry_description FROM task_entry
                    WHERE task_id = {i[0]}
                    """)
                ans[-1].append(list(curs.fetchall()))
        return ans


def workers_and_types_script():
    """workers_and_types_script."""
    try:
        conn = psycopg2.connect("dbname = 'db_user' user = 'postgres' host='localhost' password='0852'")
    except Exception as e:
        print(f'Undefined error {e}')

    with conn.cursor() as curs:
        # try:
        # Test fill
        """
        for i in range(ord('A'), ord('Z') + 1):
            curs.execute(f"INSERT INTO user_type (user_id,user_type) VALUES ({i - ord('A')},'{chr(i)}')")
        for i in range(ord('A'), ord('Z') + 1):
            curs.execute(
                f"INSERT INTO user_authorization (user_id,user_fid,user_name,user_password) VALUES
                 ({i - ord('A')},{i - ord('A')},'{chr(i)}','{chr(i)}')")
        """
        # Select all rows from user_type
        curs.execute('SELECT * FROM user_type')
        # fetch all of them
        q = curs.fetchall()
        for i in q:
            curs.execute(f'SELECT user_fid, user_name FROM user_authorization WHERE (user_fid = {i[0]})')
            qwe = curs.fetchall()
            if qwe:
                yield [i[0], list(*qwe)[1], i[1]]


def all_tasks_script():
    """all_tasks_script."""
    try:
        conn = psycopg2.connect("dbname = 'db_task' user = 'postgres' host='localhost' password='0852'")
    except Exception as e:
        print(f'Undefined error {e}')

    with conn.cursor() as curs:
        # Test fill
        """
        for i in range(ord('A'), ord('Z') + 1):
            curs.execute(
                f"INSERT INTO task_info (task_id,task_name,task_supervisor,task_workers,percent) VALUES
                 ({i - ord('A')},'{chr(i)}',1,ARRAY[1, 2, 3],10)")
        for i in range(ord('A'), ord('Z') + 1):
            curs.execute(
                f"INSERT INTO task_entry (entry_id,task_id,workers_id,entry_description,percent,date) VALUES
                 ({i - ord('A')},'{i - ord('A')}',{(i - ord('A')) % 3},'ROFLS',10,'2024-02-02')")
        """
        # Select all rows from task_info
        curs.execute('SELECT * FROM task_info')
        # fetch all of them
        return curs.fetchall()
        # return curs.fetchall()

# pprint(list(all_tasks_by_worker_id(0)))
# pprint(list(all_tasks_script()))
# print(list(workers_and_types_script()))
