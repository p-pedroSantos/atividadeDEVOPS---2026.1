def limpar_nome(nome):
    # Simula uma limpeza: remove espaços e coloca em maiúsculas
    return nome.strip().upper()

if __name__ == "__main__":
    print(limpar_nome("  dataflow etl  "))