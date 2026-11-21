from pathlib import Path


PASTA_PROJETO = Path(__file__).resolve().parents[2]

PASTA_DADOS = PASTA_PROJETO / "data"

# coloque abaixo o caminho para os arquivos de dados de seu projeto
DADOS_ORIGINAIS = PASTA_DADOS / "ml_project1_data.csv"
DADOS_NOVAS_COLS_DROP_COLS = PASTA_DADOS / "customers_new_features_and_drop.csv"
DADOS_DUMIES = PASTA_DADOS / "customers_new_features_and_drop_dummies.csv"

# coloque abaixo o caminho para os arquivos de modelos de seu projeto
#PASTA_MODELOS = PASTA_PROJETO / "modelos"
#MODELO_FINAL = PASTA_MODELOS / "ridge.joblib"

# coloque abaixo outros caminhos que você julgar necessário
#PASTA_RELATORIOS = PASTA_PROJETO / "relatorios"
#PASTA_IMAGENS = PASTA_RELATORIOS / "imagens"