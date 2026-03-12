"""ETL - é um tipo de data integration em três etapa:
Extract (Extração)
Transform (Transformação)
Load (Carga)

Extrair dados de uma fonte, transforma-los e carrega-los em um destino"""

import luigi as lg
import pandas as pd

class ExtractTask(lg.Task):    
    def output(self):
        return lg.LocalTarget('data/raw_data.csv')
    
    def run(self):
        # Simula extração de dados de uma fonte
        data = {
            'id': [1, 2, 3, 4, 5],
            'nome': ['João', 'Maria', 'Pedro', 'Ana', 'Carlos'],
            'idade': [25, 30, 35, 28, 42],
            'salario': [3000, 4500, 5200, 3800, 6000]
        }
        df = pd.DataFrame(data)
        df.to_csv(self.output().path, index=False)


class TransformTask(lg.Task):    
    def requires(self):
        return ExtractTask()
    
    def output(self):
        return lg.LocalTarget('data/transformed_data.csv')
    
    def run(self):
        # Lê os dados extraídos
        df = pd.read_csv(self.input().path)
        
        # Aplica transformações: adiciona coluna de categoria salarial
        df['categoria_salario'] = df['salario'].apply(
            lambda x: 'Alto' if x >= 5000 else 'Médio' if x >= 4000 else 'Baixo'
        )
        
        # Filtra apenas pessoas com mais de 25 anos
        df = df[df['idade'] > 25]
        
        # Salva os dados transformados
        df.to_csv(self.output().path, index=False)


class LoadTask(lg.Task):    
    def requires(self):
        return TransformTask()
    
    def output(self):
        return lg.LocalTarget('data/final_data.csv')
    
    def run(self):
        # Lê os dados transformados
        df = pd.read_csv(self.input().path)
        
        # Simula carregamento em destino final (aqui apenas copia o arquivo)
        df.to_csv(self.output().path, index=False)
        print(f"ETL concluído! {len(df)} registros carregados no destino final.")


if __name__ == '__main__':
    lg.build([LoadTask()], local_scheduler=True)