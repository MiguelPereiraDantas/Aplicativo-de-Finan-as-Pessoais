import sqlite3

def create_database():
    conn = sqlite3.connect('financas_pessoais.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transacoes (
                    id INTEGER PRIMARY KEY,
                    tipo TEXT,
                    categoria TEXT,
                    descricao TEXT,
                    valor REAL,
                    data TEXT
                )''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
