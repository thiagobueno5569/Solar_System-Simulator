# Simulador do Sistema Solar

Simulação em Python do movimento de planetas ao redor do Sol, calculada pela lei da gravitação universal de Newton.

Projeto de estudo de física computacional, de 2024.

## O que ele faz

- Modela o Sol, a Terra, Marte e Mercúrio, com distâncias em unidades astronômicas e massas aproximadas.
- Calcula a velocidade orbital de cada planeta por `v = √(G·M / r)`.
- Sorteia a posição inicial de cada planeta na sua órbita.
- Atualiza posições e velocidades a cada passo a partir da força gravitacional.
- Desenha as trajetórias em 3D com `matplotlib`, atualizadas em tempo real.
- Permite ajustar a velocidade da simulação com a tecla `S`.

## Como rodar

```
pip install matplotlib
python sla.py
```

O script importa as classes `SolarSystem`, `Sun` e `Planet` de um módulo `solarsystem.py`, que ainda não está neste repositório. Sem ele, o script não executa.

## Autor

Thiago Bueno da Silva, estudante de Engenharia Elétrica na UFSJ.
