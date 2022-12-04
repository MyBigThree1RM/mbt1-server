import pymysql
import datetime
from time import sleep
import config

conn = pymysql.connect(host=config.DATABASE_CONFIG['host'],
                        user=config.DATABASE_CONFIG['user'], 
                        password=config.DATABASE_CONFIG['password'], 
                        db=config.DATABASE_CONFIG['dbname'], charset='utf8mb4')
cursor = conn.cursor()

def sign_up(cur, con, uid, upw):
    # 기능 추가는 아직
    try:
        sign_sql = "insert into User values('" + uid + "', '" + upw + "');"
        cur.execute(sign_sql)

        init_sql_s = "insert into Record values('Squat', '" + datetime.date.today().strftime("%y-%m-%d") + "', 0, '" + uid + "');"
        cur.execute(init_sql_s)

        init_sql_b = "insert into Record values('BenchPress', '" + datetime.date.today().strftime("%y-%m-%d") + "', 0, '" + uid + "');"
        cur.execute(init_sql_b)

        init_sql_d = "insert into Record values('Deadlift', '" + datetime.date.today().strftime("%y-%m-%d") + "', 0, '" + uid + "');"
        cur.execute(init_sql_d)
        con.commit()
        print(uid + ":" + upw + " 님 회원가입 성공")
        return 1

    except:
        print("이미 존재하는 아이디 입니다.")
        con.rollback()
        return 0




def log_in(cur, con, uid, upw):
    try:
        log_sql = "select UID from User where UID = '" + str(uid) + "' and UPW = '" + str(upw) + "';"
        cur.execute(log_sql)
        con.commit()

        uname = cur.fetchone()
        print(str(uname[0]) + "님 환영합니다.")
        
        return 1 # success login
    except:
        print("일치하는 ID 또는 PW가 없습니다.")
        con.rollback()

        return 0 # fail login


def saveData(cur, con, event, oneRM, uid):
    try:
        try:
            # Insert Data
            insert_sql = "insert into Record values('" + event + "', '" + datetime.date.today().strftime("%y-%m-%d") + "', " + str(oneRM) + ", '" + uid + "');"
            cur.execute(insert_sql)
            con.commit()
            print(event + ": 새로운 데이터 생성")

        except:
            # Update Data
            update_sql = "update Record set R1rm = " + str(oneRM) + " where UID = '" + uid + "' and REvent = '" + event + "' and RDate = '" + datetime.date.today().strftime("%y-%m-%d") + "';"
            cur.execute(update_sql)
            con.commit()
            print(event + ": 오늘 데이터 최신화")
    except:
        con.rollback()
        print("실패")

def saveChallenge(cur, con, event, oneRM, uid, gym_code):
    try:
        try:
            # Insert Data
            insert_sql = "insert into Challenge values('" + event + "', " + str(oneRM) + ", '" + uid + "', " + str(gym_code) + ");"
            cur.execute(insert_sql)
            con.commit()
            print(uid + event + " Challenge Code 1 생성")

        except:
            # Update Data
            update_sql = "update Challenge set CWeight = " + str(oneRM) + " where UID = '" + uid + "' and CEvent = '" + event + "' and CCODE = " + gym_code +";"
            cur.execute(update_sql)
            con.commit()
            print(uid + event + " Challenge Code 1 최신화")
    except:
        con.rollback()
        print("실패")




def get_userData_s(cur, con, uid):
    try:
        s_sql = "select RDate, R1rm from Record where UID = '" + uid + "' and REvent = 'Squat' order by RDate desc LIMIT 6;"
        cur.execute(s_sql)
        con.commit()

        s_record = cur.fetchall()
        squat_record = {}
        for i in s_record:
            squat_record[str(i[0])] = i[1]
        
        return squat_record


    except:
        print("스쿼트 기록 조회 실패")
        con.rollback()


def get_userData_b(cur, con, uid):
    try:
        b_sql = "select RDate, R1rm from Record where UID = '" + uid + "' and REvent = 'BenchPress' order by RDate desc LIMIT 6;"
        cur.execute(b_sql)
        con.commit()

        b_record = cur.fetchall()
        bench_record = {}
        for i in b_record:
            bench_record[str(i[0])] = i[1]
        
        return bench_record

    except:
        print("벤치 기록 조회 실패")
        con.rollback()


def get_userData_d(cur, con, uid):
    try:
        d_sql = "select RDate, R1rm from Record where UID = '" + uid + "' and REvent = 'Deadlift' order by RDate desc LIMIT 6;"
        cur.execute(d_sql)
        con.commit()

        d_record = cur.fetchall()
        dead_record = {}
        for i in d_record:
            dead_record[str(i[0])] = i[1]
        
        return dead_record

    except:
        print("데드 기록 조회 실패")
        con.rollback()


def get_userData_t(cur, con, uid):
    sleep(0.5) # get_userData_s/b/d 와 동시에 Table에 접근 방지
    try:
        oneRM = {}
        cur.execute("select MAX(R1rm) from Record where REvent = 'Squat' and UID = '" + uid + "';")
        # con.commit()
        best_s = cur.fetchone()

        cur.execute("select MAX(R1rm) from Record where REvent = 'BenchPress' and UID = '" + uid + "';")
        # con.commit()
        best_b = cur.fetchone()

        cur.execute("select MAX(R1rm) from Record where REvent = 'Deadlift' and UID = '" + uid + "';")
        best_d = cur.fetchone()
        con.commit()

        best_rm = best_s[0] + best_b[0] + best_d[0]

        oneRM['User'] = uid 
        oneRM['Total'] = best_rm 
        oneRM['S'] = best_s[0]
        oneRM['B'] = best_b[0]
        oneRM['D'] = best_d[0]
        
        return oneRM

    except:
        print("베스트 기록 조회 실패")
        con.rollback()



def rank_sys(cur, con):
    try:
        rank_list = {}
        query = "select UID from User"
        cur.execute(query)
        conn.commit()

        userID = cur.fetchall()
        print(userID)
        for i in userID:
            print(i[0])
            cur.execute("select Max(CWeight) from Challenge where CEvent = 'Squat' and UID = '" + i[0] + "';")
            temp = cur.fetchone()[0]
            if temp != None:
                best_s = temp
            else:
                best_s = 0

            cur.execute("select Max(CWeight) from Challenge where CEvent = 'BenchPress' and UID = '" + i[0] + "';")
            temp = cur.fetchone()[0]
            if temp != None:
                best_b = temp
            else:
                best_b = 0

            cur.execute("select Max(CWeight) from Challenge where CEvent = 'Deadlift' and UID = '" + i[0] + "';")
            temp = cur.fetchone()[0]
            if temp != None:
                best_d = temp
            else:
                best_d = 0

            best_rm = best_s + best_b + best_d
            rank_list[i[0]] = best_rm

        rank_list = dict(sorted(rank_list.items(), key=lambda x:x[1], reverse=True))

        print("랭크 조회 성공")
        con.commit()
        return rank_list

    except:
        print("랭크 조회 실패")
        con.rollback()

def getRecord(cur, con):
    try:
        ranking = []
        cur.execute("select CCode from Center;")
        # con.commit()
        gymCode = cur.fetchall()

        for code in gymCode:
            tempRank = {}
            tempRank['one'] = ' null '
            tempRank['two'] = ' null '
            tempRank['three'] = ' null '
            tempRank['four'] = ' null '
            tempRank['five'] = ' null '

            tempRank['Code'] = code[0]
            cur.execute("select Cname, lat, lon from Center where CCode = " + str(code[0]) + ";")
            name, lat, lon = cur.fetchall()[0]
            tempRank['name'] = name
            tempRank['lat'] = lat
            tempRank['lon'] = lon

            # con.commit()
            cur.execute("select UID from Challenge where CCode = " + str(code[0]) + ";")
            # con.commit()
            userID = set(cur.fetchall())

            tempRank2 = []
            for uid in userID:
                cur.execute("select sum(CWeight) from Challenge where CCode = " + str(code[0]) + " and UID = '" + str(uid[0]) + "';")
                # con.commit()
                tempRank2.append([str(uid[0]), int(cur.fetchone()[0])])
                tempRank2.sort(key = lambda x : -x[1])

            for i in range(len(tempRank2)):
                if i == 0:
                    tempRank['one'] = tempRank2[i][0] + ' ' + str(tempRank2[i][1])
                elif i == 1:
                    tempRank['two'] = tempRank2[i][0] + ' ' + str(tempRank2[i][1])
                elif i == 2:
                    tempRank['three'] = tempRank2[i][0] + ' ' + str(tempRank2[i][1])
                elif i == 3:
                    tempRank['four'] = tempRank2[i][0] + ' ' + str(tempRank2[i][1])
                elif i == 4:
                    tempRank['five'] = tempRank2[i][0] + ' ' + str(tempRank2[i][1])

            ranking.append(tempRank)

        for i in ranking:
            print(i)
        con.commit()

    except:
        print("Failed!")
        con.rollback()

    return ranking








if __name__ == '__main__':

    # print(sign_up(cursor, conn, "kms", "0000"))
    # print(log_in(cursor, conn, "kms", "1234"))

    print(rank_sys(cursor, conn))
    # print(saveChallenge(cursor, conn, 'Sqaut', 200, 'kms'))
    # print(get_userData_s(cursor, conn, 'kms'))
    # print(get_userData_b(cursor, conn, 'kms'))
    # print(get_userData_d(cursor, conn, 'kms'))

    # print(get_userData_t(cursor, conn, 'kms'))


    # print(type(get_userData_t(cursor, conn, 'kms')))
    # print(type(get_userData_s(cursor, conn, 'kms')))
    # print(type(get_userData_b(cursor, conn, 'kms')))
    # print(type(get_userData_d(cursor, conn, 'kms')))



