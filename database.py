from sqlalchemy import create_engine,text


db_conn_string="mysql+pymysql://mqzipnqvbrdjz88j9ki7:pscale_pw_2BXdJ2JkHrOijt7OaJYHr4iPR42DN9ZVqBuBng8VqfV@aws.connect.psdb.cloud/jonpost?charset=utf8mb4"
engine = create_engine(db_conn_string,
        connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
    })

def Load_db():
    with engine.connect() as conn:
        result=conn.execute(text("select * from JOBS"))
        result_dict=[]
        for row in result.all():
            result_dict.append(row._asdict())
        return result_dict 
