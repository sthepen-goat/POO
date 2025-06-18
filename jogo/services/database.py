import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name='jogo_cartas.db'):
        self.conn = sqlite3.connect(db_name)
        self.criar_tabelas()

    def criar_tabelas(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vitorias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_jogador TEXT NOT NULL,
                data_vitoria TEXT NOT NULL,
                vida_restante INTEGER,
                cartas_restantes INTEGER
            )
        ''')
        self.conn.commit()

    def registrar_vitoria(self, nome_jogador, vida_restante, cartas_restantes):
        data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO vitorias (nome_jogador, data_vitoria, vida_restante, cartas_restantes)
            VALUES (?, ?, ?, ?)
        ''', (nome_jogador, data_atual, vida_restante, cartas_restantes))
        self.conn.commit()

    def obter_ranking(self, limite=10):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT nome_jogador, COUNT(*) as total_vitorias, 
                   MAX(data_vitoria) as ultima_vitoria
            FROM vitorias
            GROUP BY nome_jogador
            ORDER BY total_vitorias DESC, ultima_vitoria DESC
            LIMIT ?
        ''', (limite,))
        return cursor.fetchall()

    def fechar_conexao(self):
        self.conn.close()