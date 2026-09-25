import sqlite3, json, sys

db = '/Users/lisa/.openclaw/state/openclaw.sqlite'
conn = sqlite3.connect(db)
cur = conn.cursor()

cur.execute('SELECT job_id, display_name, schedule_expr, job_json FROM cron_jobs WHERE enabled = 1')
rows = cur.fetchall()
fixed = 0
for job_id, name, db_expr, job_json_str in rows:
    try:
        job = json.loads(job_json_str) if job_json_str else {}
        json_expr = job.get('schedule', {}).get('expr', '')
        if json_expr and json_expr != db_expr:
            print(f'SYNC {name}: db={db_expr} -> json={json_expr}')
            cur.execute('UPDATE cron_jobs SET schedule_expr = ? WHERE job_id = ?', (json_expr, job_id))
            fixed += 1
        else:
            print(f'OK {name}: {db_expr}')
    except Exception as e:
        print(f'ERR {name}: {e}')

if fixed:
    conn.commit()
    print(f'Synced {fixed} jobs')
else:
    print('All in sync')
conn.close()
