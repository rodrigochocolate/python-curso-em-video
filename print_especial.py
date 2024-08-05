def cabecalho(texto: str):
    texto = texto.strip()
    tamanho = len(texto) + 4
    print('~' * tamanho)
    print(f'{texto:^{tamanho}}')
    print('~' * tamanho)
    
cabecalho('Curso em Vídeo')
cabecalho('Cev')
cabecalho('Python')