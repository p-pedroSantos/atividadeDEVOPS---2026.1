from etl import limpar_nome

def test_limpar_nome_sucesso():
    assert limpar_nome("  joao  ") == "JOAO"

def test_limpar_nome_vazio():
    assert limpar_nome("   ") == ""