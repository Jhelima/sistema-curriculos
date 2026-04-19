import pandas as pd
import os

# Caminho onde o arquivo sera salvo
caminho_arquivo = 'data/candidatos.csv'

def inicializar_banco():
    # Verifica  arquivo se já existe para não apagar os dados antigos
    if not os.path.exists(caminho_arquivo):
       
        # Cria  colunas baseadas  formulário HTML
        colunas = ['nome', 'email', 'telefone', 'cpf', 'nascimento', 'genero', 'area', 'nivel', 'resumo']
        df = pd.DataFrame(columns=colunas)
        
        # Cria a pasta 'data' caso esqueca de cria-la
        os.makedirs('data', exist_ok=True)
        
        # Salva o arquivo vazio apenas com o cabeçalho
        df.to_csv(caminho_arquivo, index=False, encoding='utf-8')
        print("✅ Banco de dados CSV criado com sucesso!")
    else:
        print("📂 Banco de dados já existe. Pronto para uso.")

def adicionar_candidato(dados):
    # Lê o banco atual
    df = pd.read_csv(caminho_arquivo)
    
    # Transforma os novos dados em uma linha da tabela
    novo_candidato = pd.DataFrame([dados])
    
    # Adiciona a nova linha ao banco existente
    df = pd.concat([df, novo_candidato], ignore_index=True)
    
    # Salva de volta no CSV
    df.to_csv(caminho_arquivo, index=False, encoding='utf-8')
    print(f"👤 Candidato {dados['nome']} salvo no banco Pandas!")

# --- TESTE MANUAL ---
#  este arquivo, ele vai simular um cadastro:
if __name__ == "__main__":
    inicializar_banco()
    
    exemplo_dados = {
        'nome': 'Jéssica Lima',
        'email': 'jessica@email.com',
        'telefone': '2199999999',
        'area': 'Software Engineering',
        'nivel': 'Estágio',
        'resumo': 'Estudante focada em transição para Tech.'
    }
    
    adicionar_candidato(exemplo_dados)
    