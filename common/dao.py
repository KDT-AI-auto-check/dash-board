import sqlite3
from . import singleton
from datetime import datetime
import time

DB_PATH = 'E:\workspace\kdt\db\students.db'

class DAOInstance:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self.cur = self.conn.cursor()

    def is_valid_student(self, student_id, class_id):
        """
        DB상에서 유효한 출석 정보인지/출석부에 존재하는 정보인지 확인
        
        args:
            student_id : 학생 id
            class_id : 수업 id
        
        returns:
            bool : 유효 출석 정보라면 True, 아니라면 False를 반환
        """
        assert type(student_id) in [str, int]
        assert type(class_id) in [str, int]

        query = f'select student_id \
                  from attendance \
                  where student_id=={student_id} and class_id=={class_id};'
        
        self.cur.execute(query)
        rows = self.cur.fetchall()

        res = False
        if rows and rows[0][0] == student_id:
            res = True
        
        return res
    
    def update_attendance(self, student_id, class_id):
        """
        학생이 현재 출결하고 있음이 확인된 후 동작하게 된다.
        DB 출석부에 학생 정보에 현재 시간을 업데이트 한다.
        
        args:
            student_id : 학생 id
            class_id : 수업 id
        """
        assert type(student_id) in [str, int]
        assert type(class_id) in [str, int]
    
        now_timestamp = int(time.mktime(datetime.today().timetuple()))
        query = f'update attendance \
                  set atd_time={now_timestamp} \
                  where student_id={student_id} and class_id={class_id};'
        self.cur.execute(query)
        self.conn.commit()

    def get_all_student_in_class(self, class_id):
        """
        수업의 출석부를 반환한다.
        
        args:
            class_id : 수업 id
        
        returns:
            dict({int: datetime})
        """
        assert type(class_id) in [str, int]

        query = f'select * from attendance where class_id={class_id};'
        
        self.cur.execute(query)
        rows = self.cur.fetchall()
        rows = [[s, t] for s, _, t in rows ]
        rows = [[s, t] if t is None else [s, datetime.fromtimestamp(t)] 
                 for s, t in rows]
        return rows


    def __del__(self):
        self.conn.close()

class DAO(DAOInstance, singleton.SingletonInstane):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    import pandas as pd
    my_dao = DAO()
    my_dao.update_attendance(3, 0)