### vpl6

Elevadores são comuns em prédios. Para sua automação é importante conhecer o andar em que o elevador está, a quantidade de andares do prédio, a capacidade de pessoas suportada e a contagem de pessoas no elevador.

As ações típicas de um elevador são subir e descer. Contudo, deve-se controlar a quantidade de pessoas que entram e saem do elevador, não permitindo exceder seu limite.

Também é importante controlar se o elevador já chegou ao térreo (andar 0) ou ao último andar.

Esses controles são realizados por meio da implementação de exceções.

Implemente as exceções esperadas e dispare as exceções nos momentos devidos. Não é necessário realizar o tratamento das exceções, pois o código de testes já realiza esse tratamento.

Quando o controlador inicializar o elevador, é importante garantir que os parâmetros de inicialização sejam válidos. Existem 4 casos que invalidam o comando de inicialização:

    1.Existe algum parâmetro que não é um valor inteiro.
    2.Existe algum parâmetro com valor negativo.
    3.O andar atual do elevador não respeita a restrição do número total de andares no prédio.
    4.O número total de pessoas no elevador não respeita a restrição da capacidade máxima do elevador.
Quando qualquer um desses casos ocorrer, o comando de inicialização é considerado inválido e o elevador deve manter seus atributos anteriores.

IMPORTANTE: Implemente o exercício seguindo exatamente as Classes e Interfaces disponibilizadas pelo professor.