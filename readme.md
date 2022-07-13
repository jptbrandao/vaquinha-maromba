# Versao v1:

## Datas

Inicio: 11/07/2022
Fim: 31/12/2022

## Entradas

Para entrar: 100 reais

## Premios dos ganhadores

Top 3 Ganham premio. 4o ganha trofeu joinha

- 1o -> 60% pot
- 2o -> 30% pot
- 3o -> 10% pot

## Regras de contabilidade

1. Só conta 1 vez por dia. Se vc for mais vezes no mesmo dia, só vai contar 1 vez
2. Max 5x semana. Semana inicia SEMPRE na 2a.
3. TEM que postar foto no grupo de vc malhando, com a hashtag #maromba23
4. TEM q contabilizar o proprio dia

## F.A.Q.

O que conta como exercicio?

- Esporte
- Malhar
- Algo que te faça suar por uns 45 mins de exercicio

No mais, confiamos no amiguinho para nao zuar a brincadeira, seja pra avacalhar, ou pra mentir
A unica coisa q pode avacalhar sao os outros membros do grupo,

## Instruções para rodar o parser:

1. Baixar as mensagens do telegram.
2. Botar o arquivo html no diretorio
3. Rodar da forma:

```
python parseHtmlFile.py arquivoInput.html arquivoOutput.csv
python countBids.py arquivoOutput.csv

```

Exemplo:

```
python parseHtmlFile.py msg-22-07-11.html output.txt`
pythonr countBids.py output.txt
```

## Links interessantes:

- https://github.com/pedroargento/meal-prep-help

### TODO:

1. Done - Salvar output para um arquivo txt (facilitar a leitura de outros). Cada linha é uma registro do bid
2. Fazer o parse desse arquivo txt para contabilizar os bids dos participantes.
3. Estipular as regras do jogo
