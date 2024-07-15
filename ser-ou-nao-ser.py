algo = input('Digite algo: ')
print(f'''O que você digitou...
      É do tipo: {type(algo)}
      É alfanumérico? {algo.isalnum()}
      É alfabético? {algo.isalpha()}
      É ASCII? {algo.isascii()}
      É decimal? {algo.isdecimal()}
      É digito? {algo.isdigit()}
      É identificador? {algo.isidentifier()}
      É minúsculo? {algo.islower()}
      É maiúsculo? {algo.isupper()}
      É numérico? {algo.isnumeric()}
      É imprimível? {algo.isprintable()}
      É um título? {algo.istitle()}
      Tem somente espaços? {algo.isspace()}
      ''')
input()
