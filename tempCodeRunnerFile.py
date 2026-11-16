from turtle import *  # Importa os comandos gráficos da biblioteca turtle.

for steps in range(100):  # Repete o desenho para valores de 0 a 99.
    for c in ('blue', 'red', 'green'):  # Desenha cada segmento nas três cores.
        color(c)  # Define a cor do segmento atual.
        forward(steps)  # Avança e desenha um segmento com comprimento steps.
        right(30)  # Gira a tartaruga 30 graus para a direita.

showturtle()  # Exibe o cursor da tartaruga na janela.
done()  # Mantém a janela aberta até ela ser fechada.
