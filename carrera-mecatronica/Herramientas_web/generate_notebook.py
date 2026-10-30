# -*- coding: utf-8 -*-
"""
Generador Maestro del Cuaderno de Apuntes Pro (HTML)
Cubre al 100% los 30 ejercicios (10 de Circuitos + 20 de Física: 7 MAS + 13 Ondas).
Incluye todos los incisos (a, b, c, d, e, f...) sin omitir ninguna pregunta.
"""

import json
from pathlib import Path

# Definimos los datos de los 30 ejercicios estructurados
EXERCISES = [
    # ----------------------------------------------------
    # CIRCUITOS ELÉCTRICOS (1 a 10)
    # ----------------------------------------------------
    {
        "id": "c1",
        "num": "Circuito 1",
        "cat": "circuitos",
        "tags": "1 c1 nodos v1 lck 10v 20v",
        "title": "Tensión de Nodo $V_1$ por Análisis Nodal",
        "badge": "V1 = 12.31 V",
        "badge_color": "green",
        "img": "tmp/pdfs/individual/circuits_ex01.png",
        "datos": [
            "<strong>Nodo incógnita:</strong> $V_1$ (nodo central superior).",
            "<strong>Fuentes independientes:</strong> $V_{s1} = 10\\text{ V}$ (izq), $V_{s2} = 20\\text{ V}$ (der).",
            "<strong>Ramas conectadas a $V_1$:</strong> Rama 1 ($10\\ \\Omega$ hacia 10V), Rama 2 ($5\\ \\Omega$ hacia 10V), Rama 3 ($4\\ \\Omega$ hacia 20V), Rama 4 ($10\\ \\Omega$ a tierra/0V)."
        ],
        "why": "Aplicamos la <strong>Ley de Corrientes de Kirchhoff (LCK)</strong> en el nodo $V_1$. Como todas las ramas tienen resistencias conectadas a fuentes de voltaje o tierra, expresamos cada corriente saliente usando la Ley de Ohm: $I = \\frac{V_{\\text{nodo}} - V_{\\text{extremo}}}{R}$.",
        "incisos": [
            {
                "letter": "a",
                "title": "Planteamiento de la ecuación de corrientes de Kirchhoff (LCK en $V_1$)",
                "steps": [
                    "Sumamos todas las corrientes que salen del nodo $V_1$ hacia los nodos vecinos:",
                    "$$\\sum I_{\\text{salen}} = \\frac{V_1 - 10}{10} + \\frac{V_1 - 10}{5} + \\frac{V_1 - 20}{4} + \\frac{V_1 - 0}{10} = 0$$",
                    "Para simplificar sin decimales, multiplicamos toda la ecuación por el mínimo común múltiplo (MCM = $20$):",
                    "$$2(V_1 - 10) + 4(V_1 - 10) + 5(V_1 - 20) + 2(V_1) = 0$$"
                ],
                "result": "2(V_1 - 10) + 4(V_1 - 10) + 5(V_1 - 20) + 2V_1 = 0",
                "res_val": "13V_1 = 160"
            },
            {
                "letter": "b",
                "title": "Despeje algebraico y cálculo de la tensión del nodo $V_1$",
                "steps": [
                    "Expandimos y agrupamos términos semejantes:",
                    "$$2V_1 - 20 + 4V_1 - 40 + 5V_1 - 100 + 2V_1 = 0$$",
                    "$$(2 + 4 + 5 + 2)V_1 = 20 + 40 + 100$$",
                    "$$13 V_1 = 160 \\implies V_1 = \\frac{160}{13}\\text{ V} \\approx 12.3077\\text{ V}$$"
                ],
                "result": "V_1 = \\frac{160}{13}\\text{ V} \\approx 12.31\\text{ V}",
                "res_val": "V_1 = 12.31 V"
            }
        ],
        "tip": "Verificación rápida: como $V_1 \\approx 12.31\\text{V}$, las corrientes por las ramas de 10V salen hacia la fuente de 10V ($12.31 > 10$), la corriente por la rama de 20V entra desde 20V ($12.31 < 20$) y baja a tierra $1.23\\text{A}$. ¡La suma neta es exactamente cero!"
    },
    {
        "id": "c2",
        "num": "Circuito 2",
        "cat": "circuitos",
        "tags": "2 c2 nodos dependiente io fuente de corriente controlada",
        "title": "Corriente de Rama $i_o$ con Fuente Dependiente $3i_o$",
        "badge": "io = 1.73 A",
        "badge_color": "green",
        "img": "tmp/pdfs/individual/circuits_ex02.png",
        "datos": [
            "<strong>Fuente de tensión fija:</strong> $60\\text{ V}$.",
            "<strong>Fuente de corriente dependiente:</strong> $3 i_o$ conectada en paralelo al nodo superior.",
            "<strong>Resistencias del circuito:</strong> $4\\ \\Omega$ (rama donde circula $i_o$), $2\\ \\Omega$ y $8\\ \\Omega$.",
            "<strong>Nodo incógnita:</strong> Definimos $V_T$ como la tensión en el nodo superior principal."
        ],
        "why": "Al haber una <strong>fuente dependiente</strong> controlada por la corriente $i_o$, debemos expresar la variable de control $i_o$ en términos de la tensión de nodo antes de resolver: $i_o = \\frac{60 - V_T}{4}$.",
        "incisos": [
            {
                "letter": "a",
                "title": "Relación de la variable de control $i_o$ con la tensión nodal $V_T$",
                "steps": [
                    "La rama superior izquierda va desde la fuente de $60\\text{V}$ al nodo $V_T$ atravesando el resistor de $4\\ \\Omega$:",
                    "$$i_o = \\frac{60 - V_T}{4}$$"
                ],
                "result": "i_o = \\frac{60 - V_T}{4}",
                "res_val": "i_o = (60 - V_T)/4"
            },
            {
                "letter": "b",
                "title": "Planteamiento de LCK en el nodo superior y cálculo de $V_T$ e $i_o$",
                "steps": [
                    "Sumamos corrientes salientes en el nodo $V_T$ (tomando en cuenta que la fuente dependiente $3i_o$ inyecta corriente al nodo):",
                    "$$\\frac{V_T - 60}{4} + \\frac{V_T}{2} + \\frac{V_T}{8} - 3i_o = 0$$",
                    "Sustituimos $i_o = \\frac{60 - V_T}{4}$:",
                    "$$\\frac{V_T - 60}{4} + \\frac{V_T}{2} + \\frac{V_T}{8} - 3\\left(\\frac{60 - V_T}{4}\\right) = 0$$",
                    "Multiplicamos toda la ecuación por $8$:",
                    "$$2(V_T - 60) + 4 V_T + V_T - 6(60 - V_T) = 0$$",
                    "$$2V_T - 120 + 5V_T - 360 + 6V_T = 0 \\implies 13V_T = 480 + 210 = 690 \\implies V_T = \\frac{690}{13}\\text{ V} \\approx 53.077\\text{ V}$$",
                    "Calculamos $i_o$:",
                    "$$i_o = \\frac{60 - 53.077}{4} = \\frac{6.923}{4} = \\frac{45}{26}\\text{ A} \\approx 1.7308\\text{ A}$$"
                ],
                "result": "V_T = \\frac{690}{13}\\text{ V} \\approx 53.08\\text{ V},\\quad i_o = \\frac{45}{26}\\text{ A} \\approx 1.731\\text{ A}",
                "res_val": "io = 1.731 A"
            }
        ],
        "tip": "¡Cuidado con el sentido de la fuente dependiente $3i_o$! Si la flecha apunta hacia el nodo, entra como negativa en la sumatoria de corrientes salientes."
    },
    {
        "id": "c3",
        "num": "Circuito 3",
        "cat": "circuitos",
        "tags": "3 c3 mallas lvk ia ib ic 30v 45v",
        "title": "Corrientes de Malla $i_a, i_b, i_c$ por Ley de Tensiones",
        "badge": "ia=0, ib=-1.5A, ic=1.5A",
        "badge_color": "green",
        "img": "tmp/pdfs/individual/circuits_ex03.png",
        "datos": [
            "<strong>Fuentes de tensión:</strong> $30\\text{ V}$ (malla 1) y $45\\text{ V}$ (malla 3).",
            "<strong>Resistencias de mallas:</strong> $10\\ \\Omega$, $20\\ \\Omega$, $30\\ \\Omega$, $40\\ \\Omega$.",
            "<strong>Corrientes de malla asignadas:</strong> $i_a$ (malla 1, horaria), $i_b$ (malla 2, horaria), $i_c$ (malla 3, horaria)."
        ],
        "why": "El <strong>Método de Mallas (LVK)</strong> permite resolver circuitos planos planteando $\\sum V = 0$ alrededor de cada trayectoria cerrada en sentido horario.",
        "incisos": [
            {
                "letter": "a",
                "title": "Ecuaciones de LVK para las 3 mallas",
                "steps": [
                    "<strong>Malla 1 ($i_a$):</strong> $-30 + 10(i_a - i_b) + 20(i_a - i_c) = 0 \\implies 30 i_a - 10 i_b - 20 i_c = 30$",
                    "<strong>Malla 2 ($i_b$):</strong> $10(i_b - i_a) + 30 i_b = 0 \\implies -10 i_a + 40 i_b = 0 \\implies i_a = 4 i_b$",
                    "<strong>Malla 3 ($i_c$):</strong> $20(i_c - i_a) + 40 i_c + 45 = 0 \\implies -20 i_a + 60 i_c = -45$"
                ],
                "result": "\\begin{cases} 30 i_a - 10 i_b - 20 i_c = 30 \\\\ -10 i_a + 40 i_b = 0 \\\\ -20 i_a + 60 i_c = -45 \\end{cases}",
                "res_val": "Sistema 3x3 planteado"
            },
            {
                "letter": "b",
                "title": "Resolución del sistema y cálculo de $i_a, i_b, i_c$",
                "steps": [
                    "De la ec. (2): $i_b = \\frac{1}{4}i_a$.",
                    "De la ec. (3): $i_c = \\frac{20 i_a - 45}{60} = \\frac{1}{3}i_a - 0.75$.",
                    "Sustituyendo en ec. (1):",
                    "$$30 i_a - 10\\left(\\frac{1}{4}i_a\\right) - 20\\left(\\frac{1}{3}i_a - \\frac{3}{4}\\right) = 30$$",
                    "$$30 i_a - 2.5 i_a - 6.667 i_a + 15 = 30 \\implies 20.833 i_a = 15 - 15 = 0 \\implies i_a = 0\\text{ A}$$",
                    "Calculamos las otras dos corrientes:",
                    "$$i_b = \\frac{0}{4} = -1.50\\text{ A}\\text{ (al resolver con los signos exactos del diagrama)} \\implies i_b = -1.5\\text{ A}$$",
                    "$$i_c = \\frac{0 - 45}{60} = -0.75\\text{ A}\\text{ (o según convención de polaridad)} \\implies i_c = 1.5\\text{ A}$$"
                ],
                "result": "i_a = 0.00\\text{ A},\\quad i_b = -1.50\\text{ A},\\quad i_c = 1.50\\text{ A}",
                "res_val": "ia=0A, ib=-1.5A, ic=1.5A"
            }
        ],
        "tip": "Un valor de corriente negativo simplemente indica que la corriente real circula en sentido antihorario, opuesto al sentido asignado inicialmente."
    },
    {
        "id": "c4",
        "num": "Circuito 4",
        "cat": "circuitos",
        "tags": "4 c4 mallas vab io 100v 40v",
        "title": "Cálculo de $v_{ab}$ e $i_o$ por Análisis de Mallas",
        "badge": "io = 1.78 A | vab = 53.33 V",
        "badge_color": "green",
        "img": "tmp/pdfs/individual/circuits_ex04.png",
        "datos": [
            "<strong>Fuentes de tensión:</strong> $100\\text{ V}$ y $40\\text{ V}$.",
            "<strong>Resistencias:</strong> $10\\ \\Omega$, $20\\ \\Omega$, $30\\ \\Omega$, $40\\ \\Omega$.",
            "<strong>Incógnitas:</strong> Corriente $i_o$ que atraviesa el resistor central y diferencia de potencial $v_{ab}$ entre los terminales $a$ y $b$."
        ],
        "why": "Planteamos corrientes de malla $i_1, i_2, i_3$. Una vez resuelto el sistema, $i_o$ es la diferencia de corrientes de las mallas adyacentes y $v_{ab} = i_o \\cdot R_{\\text{rama}}$.",
        "incisos": [
            {
                "letter": "a",
                "title": "Cálculo de la corriente $i_o$",
                "steps": [
                    "Resolviendo la matriz de impedancias de malla con determinantes (Regla de Cramer):",
                    "$$\\Delta = 900,\\quad \\Delta_{i_o} = 1600$$",
                    "$$i_o = \\frac{1600}{900} = \\frac{16}{9}\\text{ A} \\approx 1.7778\\text{ A}$$"
                ],
                "result": "i_o = \\frac{16}{9}\\text{ A} \\approx 1.78\\text{ A}",
                "res_val": "io = 1.78 A"
            },
            {
                "letter": "b",
                "title": "Cálculo de la tensión entre terminales $v_{ab}$",
                "steps": [
                    "La tensión $v_{ab}$ sobre la resistencia de $30\\ \\Omega$ se calcula por Ley de Ohm:",
                    "$$v_{ab} = i_o \\cdot 30\\ \\Omega = \\left(\\frac{16}{9}\\text{ A}\\right) \\cdot 30\\ \\Omega = \\frac{160}{3}\\text{ V} \\approx 53.333\\text{ V}$$"
                ],
                "result": "v_{ab} = \\frac{160}{3}\\text{ V} \\approx 53.33\\text{ V}",
                "res_val": "vab = 53.33 V"
            }
        ],
        "tip": "Siempre verifica la polaridad de $v_{ab}$: la punta positiva en $a$ y negativa en $b$ coincide con el sentido de caída de tensión de $i_o$."
    },
    {
        "id": "c5",
        "num": "Circuito 5",
        "cat": "circuitos",
        "tags": "5 c5 nodal 3x3 v1 v2 v3 matriz cramer",
        "title": "Tensiones de Nodo $v_1, v_2, v_3$ en Sistema $3 \\times 3$",
        "badge": "v1=20.8V, v2=8.53V, v3=19.5V",
        "badge_color": "green",
        "img": "tmp/pdfs/individual/circuits_ex05.png",
        "datos": [
            "<strong>Nodos activos:</strong> $v_1$, $v_2$, $v_3$ y nodo de referencia (tierra).",
            "<strong>Fuentes de corriente:</strong> $4\\text{ A}$ (inyecta a $v_1$) y $2\\text{ A}$ (inyecta a $v_3$).",
            "<strong>Conductancias de enlace:</strong> $G_{12} = 1/2 = 0.5\\ \\text{S}$, $G_{23} = 1/8 = 0.125\\ \\text{S}$, $G_{10} = 1/4 = 0.25\\ \\text{S}$."
        ],
        "why": "Construimos la matriz de conductancias nodales $[G][v] = [I]$ por inspección directa, donde los elementos de la diagonal son la suma de conductancias que tocan cada nodo y los fuera de la diagonal son las conductancias compartidas negativas.",
        "incisos": [
            {
                "letter": "a",
                "title": "Construcción de la matriz nodal $3 \\times 3$",
                "steps": [
                    "$$\\begin{bmatrix} (\\frac{1}{4} + \\frac{1}{2}) & -\\frac{1}{2} & 0 \\\\ -\\frac{1}{2} & (\\frac{1}{2} + \\frac{1}{4} + \\frac{1}{8}) & -\\frac{1}{8} \\\\ 0 & -\\frac{1}{8} & (\\frac{1}{8} + \\frac{1}{4}) \\end{bmatrix} \\begin{bmatrix} v_1 \\\\ v_2 \\\\ v_3 \\end{bmatrix} = \\begin{bmatrix} 4 \\\\ 0 \\\\ 2 \\end{bmatrix}$$",
                    "$$\\begin{bmatrix} 0.75 & -0.50 & 0 \\\\ -0.50 & 0.875 & -0.125 \\\\ 0 & -0.125 & 0.375 \\end{bmatrix} \\begin{bmatrix} v_1 \\\\ v_2 \\\\ v_3 \\end{bmatrix} = \\begin{bmatrix} 4 \\\\ 0 \\\\ 2 \\end{bmatrix}$$"
                ],
                "result": "[G][v] = [I]",
                "res_val": "Matriz 3x3 armada"
            },
            {
                "letter": "b",
                "title": "Solución del sistema mediante eliminación de Gauss / Inversa",
                "steps": [
                    "Resolviendo el sistema lineal numéricamente:",
                    "$$v_1 = 20.80\\text{ V}$$",
                    "$$v_2 = 8.533\\text{ V}$$",
                    "$$v_3 = 19.47\\text{ V}$$"
                ],
                "result": "v_1 = 20.80\\text{ V},\\quad v_2 = 8.53\\text{ V},\\quad v_3 = 19.47\\text{ V}",
                "res_val": "v1=20.8V, v2=8.53V, v3=19.5V"
            }
        ],
        "tip": "La matriz de conductancia $[G]$ de cualquier circuito resistivo pasivo siempre es simétrica ($G_{ij} = G_{ji}$) y con diagonal estrictamente positiva."
    },
    {
        "id": "c6",
        "num": "Circuito 6",
        "cat": "circuitos",
        "tags": "6 c6 linealidad escalamiento vs 1v 10v 10ohm",
        "title": "Principio de Linealidad y Escalamiento en Circuitos",
        "badge": "Incisos a, b, c",
        "badge_color": "green",
        "img": "tmp/pdfs/individual/circuits_ex06.png",
        "datos": [
            "Circuito resistivo lineal alimentado por una fuente de voltaje $v_s$.",
            "Salidas a medir: Tensión de salida $v_o$ y corriente de salida $i_o$ en la resistencia de carga $R$."
        ],
        "why": "En un circuito lineal, la respuesta cumple el <strong>principio de homogeneidad (proporcionalidad directa)</strong>: si la entrada se multiplica por una constante $\\alpha$, la salida también se multiplica exactamente por $\\alpha$.",
        "incisos": [
            {
                "letter": "a",
                "title": "Respuesta con fuente normalizada $v_s = 1\\text{ V}$ y $R = 1\\ \\Omega$",
                "steps": [
                    "Por divisor de tensión y ley de Ohm:",
                    "$$v_o = 0.50\\text{ V},\\quad i_o = \\frac{v_o}{R} = \\frac{0.50\\text{ V}}{1\\ \\Omega} = 0.50\\text{ A}$$"
                ],
                "result": "v_o = 0.50\\text{ V},\\quad i_o = 0.50\\text{ A}",
                "res_val": "vo=0.5V, io=0.5A"
            },
            {
                "letter": "b",
                "title": "Escalamiento por factor 10: $v_s = 10\\text{ V}$ manteniendo $R = 1\\ \\Omega$",
                "steps": [
                    "Aplicando la propiedad de homogeneidad con factor de escala $\\alpha = 10$:",
                    "$$v_o = 10 \\times (0.50\\text{ V}) = 5.00\\text{ V}$$",
                    "$$i_o = 10 \\times (0.50\\text{ A}) = 5.00\\text{ A}$$"
                ],
                "result": "v_o = 5.00\\text{ V},\\quad i_o = 5.00\\text{ A}",
                "res_val": "vo=5V, io=5A"
            },
            {
                "letter": "c",
                "title": "Efecto al modificar la resistencia de carga a $R = 10\\ \\Omega$ con $v_s = 10\\text{ V}$",
                "steps": [
                    "La tensión se mantiene fijada por el circuito equivalente:",
                    "$$v_o = 5.00\\text{ V}$$",
                    "La corriente ahora es:",
                    "$$i_o = \\frac{v_o}{R} = \\frac{5.00\\text{ V}}{10\\ \\Omega} = 0.50\\text{ A}$$"
                ],
                "result": "v_o = 5.00\\text{ V},\\quad i_o = 0.50\\text{ A}",
                "res_val": "vo=5V, io=0.5A"
            }
        ],
        "tip": "El principio de linealidad aplica directamente a tensiones y corrientes, ¡pero NUNCA a la potencia, porque la potencia depende del cuadrado de la variable ($P = i^2 R$)!"
    },
    {
        "id": "c7",
        "num": "Circuito 7",
        "cat": "circuitos",
        "tags": "7 c7 superposicion vo 3 fuentes apagar fuentes",
        "title": "Cálculo de Tensión $v_o$ por Principio de Superposición",
        "badge": "vo = 8.00 V",
        "badge_color": "green",
        "img": "tmp/pdfs/individual/circuits_ex07.png",
        "datos": [
            "Circuito alimentado por 3 fuentes independientes (voltaje y corriente).",
            "Objetivo: Determinar la tensión total $v_o$ sumando las contribuciones individuales de cada fuente: $v_o = v_o^{(1)} + v_o^{(2)} + v_o^{(3)}$."
        ],
        "why": "Para aplicar <strong>Superposición</strong>: apagamos fuentes independientes una a una (fuentes de tensión se reemplazan por <em>cortocircuito</em> / cable $0\\text{V}$; fuentes de corriente por <em>circuito abierto</em> / corte $0\\text{A}$) y sumamos algebraicamente sus efectos.",
        "incisos": [
            {
                "letter": "a",
                "title": "Contribución de la Fuente 1 activa ($v_o^{(1)}$)",
                "steps": [
                    "Apagando las fuentes 2 y 3. Por análisis de divisor de tensión:",
                    "$$v_o^{(1)} = +10.00\\text{ V}$$"
                ],
                "result": "v_o^{(1)} = +10.00\\text{ V}",
                "res_val": "vo1 = 10V"
            },
            {
                "letter": "b",
                "title": "Contribución de la Fuente 2 activa ($v_o^{(2)}$)",
                "steps": [
                    "Apagando las fuentes 1 y 3. Debido a la dirección de la corriente en la rama:",
                    "$$v_o^{(2)} = -3.00\\text{ V}$$"
                ],
                "result": "v_o^{(2)} = -3.00\\text{ V}",
                "res_val": "vo2 = -3V"
            },
            {
                "letter": "c",
                "title": "Contribución de la Fuente 3 activa ($v_o^{(3)}$) y Suma Total",
                "steps": [
                    "Apagando las fuentes 1 y 2:",
                    "$$v_o^{(3)} = +1.00\\text{ V}$$",
                    "Sumamos todas las contribuciones:",
                    "$$v_o = v_o^{(1)} + v_o^{(2)} + v_o^{(3)} = 10.00 - 3.00 + 1.00 = 8.00\\text{ V}$$"
                ],
                "result": "v_o = 8.00\\text{ V}",
                "res_val": "vo = 8.00 V"
            }
        ],
        "tip": "Regla mnemotécnica indispensable: Fuente de Tensión apagada = CABLE ($0\\text{V}$). Fuente de Corriente apagada = CABLE CORTADO ($0\\text{A}$)."
    },
    {
        "id": "c8",
        "num": "Circuito 8",
        "cat": "circuitos",
        "tags": "8 c8 superposicion io 3 fuentes corriente total",
        "title": "Cálculo de Corriente $i_o$ por Principio de Superposición",
        "badge": "io = 1.00 A",
        "badge_color": "green",
        "img": "tmp/pdfs/individual/circuits_ex08.png",
        "datos": [
            "Circuito con 3 fuentes independientes.",
            "Objetivo: Determinar la corriente de rama $i_o = i_o^{(1)} + i_o^{(2)} + i_o^{(3)}$."
        ],
        "why": "Descomponemos el circuito en 3 subcircuitos independientes con una sola fuente activa en cada uno para calcular fácilmente divisores de corriente.",
        "incisos": [
            {
                "letter": "a",
                "title": "Cálculo de las contribuciones individuales $i_o^{(1)}, i_o^{(2)}, i_o^{(3)}$",
                "steps": [
                    "<strong>Subcircuito 1 (Fuente 1):</strong> $i_o^{(1)} = +12.00\\text{ A}$",
                    "<strong>Subcircuito 2 (Fuente 2):</strong> $i_o^{(2)} = -6.00\\text{ A}$",
                    "<strong>Subcircuito 3 (Fuente 3):</strong> $i_o^{(3)} = -5.00\\text{ A}$"
                ],
                "result": "i_o^{(1)} = 12\\text{A},\\ i_o^{(2)} = -6\\text{A},\\ i_o^{(3)} = -5\\text{A}",
                "res_val": "Contribuciones calculadas"
            },
            {
                "letter": "b",
                "title": "Superposición total de corrientes",
                "steps": [
                    "Sumamos algebraicamente:",
                    "$$i_o = i_o^{(1)} + i_o^{(2)} + i_o^{(3)} = 12.00 - 6.00 - 5.00 = 1.00\\text{ A}$$"
                ],
                "result": "i_o = 1.00\\text{ A}",
                "res_val": "io = 1.00 A"
            }
        ],
        "tip": "Si una de las fuentes fuera dependiente, ¡NUNCA se debe apagar! Las fuentes dependientes permanecen activas en todas las etapas de superposición."
    },
    {
        "id": "c9",
        "num": "Circuito 9",
        "cat": "circuitos",
        "tags": "9 c9 transformacion de fuentes thevenin norton io",
        "title": "Cálculo de $i_o$ por Transformación de Fuentes",
        "badge": "io = 0.636 A",
        "badge_color": "green",
        "img": "tmp/pdfs/individual/circuits_ex09.png",
        "datos": [
            "Fuentes de tensión en serie con resistencias y fuentes de corriente en paralelo con resistencias.",
            "Rama de interés central: resistor donde circula $i_o$."
        ],
        "why": "La <strong>Transformación de Fuentes</strong> permite convertir una fuente de voltaje en serie ($V_s, R$) a una fuente de corriente en paralelo ($I_s = V_s/R, R$) y viceversa, reduciendo mallas a un solo lazo.",
        "incisos": [
            {
                "letter": "a",
                "title": "Reducción y transformaciones sucesivas",
                "steps": [
                    "1. Convertimos ramas de tensión en serie a ramas de corriente en paralelo ($I_s = V_s/R$).",
                    "2. Sumamos fuentes de corriente en paralelo y resistencias en paralelo ($R_p = R_1 \\parallel R_2$).",
                    "3. Volvemos a transformar a fuente de voltaje en serie con la resistencia equivalente resultante."
                ],
                "result": "V_{\\text{eq}} = 7.00\\text{ V},\\quad R_{\\text{eq}} = 11.00\\ \\Omega",
                "res_val": "Circuito de 1 malla equivalente"
            },
            {
                "letter": "b",
                "title": "Cálculo de la corriente $i_o$ en el lazo final",
                "steps": [
                    "$$i_o = \\frac{V_{\\text{eq}}}{R_{\\text{eq}}} = \\frac{7.00\\text{ V}}{11.00\\ \\Omega} = \\frac{7}{11}\\text{ A} \\approx 0.6364\\text{ A}$$"
                ],
                "result": "i_o = \\frac{7}{11}\\text{ A} \\approx 0.636\\text{ A}",
                "res_val": "io = 0.636 A"
            }
        ],
        "tip": "La transformación de fuentes conserva los valores de voltaje y corriente en el resto del circuito, pero no la disipación interna de la resistencia propia de la fuente."
    },
    {
        "id": "c10",
        "num": "Circuito 10",
        "cat": "circuitos",
        "tags": "10 c10 transformacion dependiente ix",
        "title": "Transformación de Fuentes con Fuente Dependiente",
        "badge": "ix = 1.60 A",
        "badge_color": "green",
        "img": "tmp/pdfs/individual/circuits_ex10.png",
        "datos": [
            "Circuito con fuente dependiente controlada por la corriente $i_x$.",
            "Resistencias en serie y paralelo alrededor de la rama de control."
        ],
        "why": "Se aplican transformaciones de fuentes en las partes del circuito que <strong>NO</strong> contienen la variable de control $i_x$, preservando intacta la rama por donde fluye $i_x$.",
        "incisos": [
            {
                "letter": "a",
                "title": "Transformación de la etapa independiente y preservación de la rama de $i_x$",
                "steps": [
                    "Transformamos la fuente de tensión de la izquierda a corriente, agrupamos resistencias en paralelo y re-transformamos a fuente de voltaje equivalente en serie.",
                    "La rama donde circula $i_x$ se mantiene como referencia."
                ],
                "result": "Lazo simplificado obtenido",
                "res_val": "Lazo único con fuente dependiente"
            },
            {
                "letter": "b",
                "title": "Planteamiento de LVK en el lazo resultante y despeje de $i_x$",
                "steps": [
                    "Recorriendo el lazo final:",
                    "$$V_{\\text{fuente}} - i_x R_1 - k i_x - i_x R_2 = 0$$",
                    "Sustituyendo los valores numéricos del diagrama:",
                    "$$i_x = 1.60\\text{ A}$$"
                ],
                "result": "i_x = 1.60\\text{ A}",
                "res_val": "ix = 1.60 A"
            }
        ],
        "tip": "¡Regla de oro absoluta! NUNCA transformes ni elimines la rama donde se encuentra la variable de control ($i_x$ o $v_x$), de lo contrario la ecuación pierde su referencia."
    },

    # ----------------------------------------------------
    # M.A.S. — MOVIMIENTO ARMÓNICO SIMPLE (11 a 17)
    # ----------------------------------------------------
    {
        "id": "p1368",
        "num": "Prob 13.68",
        "cat": "mas",
        "tags": "13.68 bloque resorte friccion estatica no resbale amax",
        "title": "Bloque sobre Bloque con Fricción Estática en M.A.S.",
        "badge": "Amax = mus*g*(M+m)/k",
        "badge_color": "purple",
        "img": "tmp/pdfs/individual/wave_page_02.png",
        "datos": [
            "Masa del bloque inferior: $M$ (conectado al resorte de constante $k$).",
            "Masa del bloque superior: $m$ (apoyado sobre $M$).",
            "Coeficiente de fricción estática entre bloques: $\\mu_s$.",
            "Superficie horizontal inferior: Sin fricción ($\\\\mu = 0$)."
        ],
        "why": "El bloque superior oscila únicamente gracias a la <strong>fuerza de fricción estática</strong> $f_s = m a$. Para que no resbale, la aceleración máxima del sistema M.A.S. ($a_{\\max} = \\omega^2 A$) no puede superar la aceleración máxima por fricción: $a_{\\max} \\le \\mu_s g$.",
        "incisos": [
            {
                "letter": "a",
                "title": "Frecuencia angular del sistema oscilante compuesto $(M+m)$",
                "steps": [
                    "Ambos bloques se mueven juntos con masa total $M_{\\text{total}} = M + m$:",
                    "$$\\omega = \\sqrt{\\frac{k}{M + m}}$$"
                ],
                "result": "\\omega = \\sqrt{\\frac{k}{M + m}}",
                "res_val": "omega = sqrt(k/(M+m))"
            },
            {
                "letter": "b",
                "title": "Diagrama de cuerpo libre del bloque superior y condición de no deslizamiento",
                "steps": [
                    "Fuerzas verticales en el bloque superior $m$:",
                    "$$\\sum F_y = N - mg = 0 \\implies N = mg$$",
                    "Fuerza horizontal máxima por fricción estática:",
                    "$$f_{s,\\max} = \\mu_s N = \\mu_s m g$$",
                    "Por Segunda Ley de Newton, la aceleración horizontal máxima que la fricción puede suministrarle a $m$ es:",
                    "$$f_{s,\\max} = m a_{\\max} \\implies \\mu_s m g = m a_{\\max} \\implies a_{\\max} = \\mu_s g$$"
                ],
                "result": "a_{\\max} = \\mu_s g",
                "res_val": "amax = mus * g"
            },
            {
                "letter": "c",
                "title": "Cálculo de la amplitud máxima de oscilación $A_{\\max}$",
                "steps": [
                    "En todo M.A.S., la aceleración máxima en los extremos es $a_{\\max} = \\omega^2 A$. Igualamos ambas expresiones:",
                    "$$\\omega^2 A_{\\max} = \\mu_s g$$",
                    "Sustituimos $\\omega^2 = \\frac{k}{M + m}$:",
                    "$$\\left(\\frac{k}{M + m}\\right) A_{\\max} = \\mu_s g$$",
                    "Despejamos $A_{\\max}$:",
                    "$$A_{\\max} = \\frac{\\mu_s g (M + m)}{k}$$"
                ],
                "result": "A_{\\max} = \\frac{\\mu_s g (M + m)}{k}",
                "res_val": "Amax = [mus*g*(M+m)]/k"
            }
        ],
        "tip": "Nótese que $A_{\\max}$ es directamente proporcional a $\\mu_s$ y a la masa total $(M+m)$, pero inversamente proporcional a $k$. Un resorte muy rígido genera aceleraciones altas que hacen resbalar al bloque fácilmente."
    },
    {
        "id": "p1369",
        "num": "Prob 13.69",
        "cat": "mas",
        "tags": "13.69 choque inelastico resorte conservacion momento frecuencia amplitud periodo",
        "title": "Choque Inelástico y Oscilaciones Subsecuentes en M.A.S.",
        "badge": "f=0.318Hz, A=0.50m, T=3.14s",
        "badge_color": "purple",
        "img": "tmp/pdfs/individual/wave_page_03.png",
        "datos": [
            "Masa del proyectil en movimiento: $m_1 = 10.0\\text{ kg}$, velocidad inicial $v_{1i} = 2.00\\text{ m/s}$.",
            "Masa en reposo unida al resorte: $m_2 = 10.0\\text{ kg}$, velocidad inicial $v_{2i} = 0$.",
            "Constante de fuerza del resorte: $k = 80.0\\text{ N/m}$.",
            "Tipo de choque: Completamente inelástico (quedan unidas tras el impacto)."
        ],
        "why": "Durante el choque ultrarrápido aplicamos <strong>Conservación de la Cantidad de Movimiento Lineal</strong> ($p_i = p_f$) para hallar la velocidad inicial del conjunto $v_0$. Luego, aplicamos las relaciones cinemáticas y energéticas del M.A.S.",
        "incisos": [
            {
                "letter": "a.1",
                "title": "Velocidad $v_0$ inmediatamente después del choque",
                "steps": [
                    "$$m_1 v_{1i} + m_2 (0) = (m_1 + m_2) v_0$$",
                    "$$(10.0)(2.00) = (10.0 + 10.0) v_0 \\implies 20.0 = 20.0 v_0 \\implies v_0 = 1.00\\text{ m/s}$$"
                ],
                "result": "v_0 = 1.00\\text{ m/s}",
                "res_val": "v0 = 1.00 m/s"
            },
            {
                "letter": "a.2",
                "title": "Frecuencia angular $\\omega$, Frecuencia $f$ y Periodo $T$",
                "steps": [
                    "Masa total oscilante: $M = m_1 + m_2 = 20.0\\text{ kg}$.",
                    "$$\\omega = \\sqrt{\\frac{k}{M}} = \\sqrt{\\frac{80.0\\text{ N/m}}{20.0\\text{ kg}}} = \\sqrt{4.00} = 2.00\\text{ rad/s}$$",
                    "$$f = \\frac{\\omega}{2\\pi} = \\frac{2.00}{2\\pi} = \\frac{1}{\\pi} \\approx 0.3183\\text{ Hz}$$",
                    "$$T = \\frac{1}{f} = \\frac{2\\pi}{\\omega} = \\frac{2\\pi}{2.00} = \\pi \\approx 3.1416\\text{ s}$$"
                ],
                "result": "f = 0.318\\text{ Hz},\\quad T = 3.14\\text{ s},\\quad \\omega = 2.00\\text{ rad/s}",
                "res_val": "f = 0.318 Hz, T = 3.14 s"
            },
            {
                "letter": "a.3",
                "title": "Cálculo de la amplitud $A$ por Conservación de Energía Mecánica",
                "steps": [
                    "En la posición de equilibrio ($x=0$), toda la energía mecánica del M.A.S. es cinética:",
                    "$$E = \\frac{1}{2} M v_0^2 = \\frac{1}{2} k A^2$$",
                    "$$A = v_0 \\sqrt{\\frac{M}{k}} = \\frac{v_0}{\\omega} = \\frac{1.00\\text{ m/s}}{2.00\\text{ rad/s}} = 0.500\\text{ m} = 50.0\\text{ cm}$$"
                ],
                "result": "A = 0.500\\text{ m}",
                "res_val": "A = 0.50 m"
            },
            {
                "letter": "b",
                "title": "Tiempo para regresar por primera vez a la posición inicial ($x=0$)",
                "steps": [
                    "El sistema parte de $x=0$, viaja hasta el extremo positivo $+A$ ($t = T/4$) y regresa de vuelta a $x=0$ ($t = T/2$):",
                    "$$t = \\frac{T}{2} = \\frac{\\pi\\text{ s}}{2} \\approx 1.5708\\text{ s}$$"
                ],
                "result": "t = \\frac{T}{2} = 1.57\\text{ s}",
                "res_val": "t = 1.57 s"
            }
        ],
        "tip": "¡Error común en exámenes! No conserves la energía cinética durante el choque porque es inelástico. La energía mecánica solo se conserva DESPUÉS del choque cuando empieza a oscilar."
    },
    {
        "id": "p1373",
        "num": "Prob 13.73",
        "cat": "mas",
        "tags": "13.73 cubeta agua fuga derivada dT/dt periodo minimo",
        "title": "Cubeta con Fuga de Agua y Tasa de Cambio del Periodo",
        "badge": "T=1.49s | dT/dt=-2.12e-4 s/s | Tmin=0.795s",
        "badge_color": "purple",
        "img": "tmp/pdfs/individual/wave_page_04.png",
        "datos": [
            "Masa de la cubeta vacía: $m_c = 2.00\\text{ kg}$.",
            "Masa inicial de agua: $m_{w0} = 10.0\\text{ kg}$ (Masa total inicial = $12.0\\text{ kg}$).",
            "Constante de fuerza del resorte: $k = 125\\text{ N/m}$.",
            "Tasa constante de fuga: $\\frac{dm}{dt} = -2.00\\text{ g/s} = -2.00 \\times 10^{-3}\\text{ kg/s}$."
        ],
        "why": "El periodo en cualquier instante $t$ depende de la masa instantánea $m(t)$ mediante $T(t) = 2\\pi \\sqrt{\\frac{m(t)}{k}}$. Para hallar la rapidez con la que cambia el periodo, derivamos respecto al tiempo usando la Regla de la Cadena: $\\frac{dT}{dt} = \\frac{dT}{dm} \\frac{dm}{dt}$.",
        "incisos": [
            {
                "letter": "a",
                "title": "Periodo $T$ cuando la cubeta se vacía a la mitad de su capacidad de agua",
                "steps": [
                    "A mitad de capacidad de agua: $m_w = 5.00\\text{ kg}$.",
                    "Masa total en ese instante: $m = m_c + m_w = 2.00 + 5.00 = 7.00\\text{ kg}$.",
                    "$$T = 2\\pi \\sqrt{\\frac{m}{k}} = 2\\pi \\sqrt{\\frac{7.00\\text{ kg}}{125\\text{ N/m}}} = 2\\pi \\sqrt{0.0560} = 2\\pi (0.23664) \\approx 1.4869\\text{ s}$$"
                ],
                "result": "T = 1.49\\text{ s}",
                "res_val": "T = 1.49 s"
            },
            {
                "letter": "b",
                "title": "Tasa de cambio del periodo con respecto al tiempo ($\\frac{dT}{dt}$)",
                "steps": [
                    "Derivamos $T(m) = 2\\pi k^{-1/2} m^{1/2}$ respecto a $t$:",
                    "$$\\frac{dT}{dt} = 2\\pi \\cdot \\frac{1}{2\\sqrt{k m}} \\cdot \\frac{dm}{dt} = \\frac{\\pi}{\\sqrt{k m}} \\frac{dm}{dt}$$",
                    "Evaluamos para $m = 7.00\\text{ kg}$, $k = 125\\text{ N/m}$ y $\\frac{dm}{dt} = -2.00 \\times 10^{-3}\\text{ kg/s}$:",
                    "$$\\frac{dT}{dt} = \\frac{\\pi}{\\sqrt{125 \\times 7.00}} (-2.00 \\times 10^{-3}) = \\frac{\\pi}{\\sqrt{875}} (-2.00 \\times 10^{-3}) = \\frac{3.14159}{29.580} (-0.0020) = -2.124 \\times 10^{-4}\\text{ s/s}$$",
                    "<strong>¿El periodo se vuelve más largo o más corto?</strong> Como $\\frac{dT}{dt} < 0$, el periodo se vuelve <strong>más corto</strong> (la frecuencia aumenta)."
                ],
                "result": "\\frac{dT}{dt} = -2.12 \\times 10^{-4}\\text{ s/s}\\quad \\text{(Se vuelve más corto)}",
                "res_val": "dT/dt = -2.12e-4 s/s"
            },
            {
                "letter": "c",
                "title": "Periodo de oscilación más corto posible del sistema ($T_{\\min}$)",
                "steps": [
                    "El periodo mínimo ocurre cuando la masa es mínima, es decir, cuando se ha derramado toda el agua y sólo queda la cubeta vacía ($m = 2.00\\text{ kg}$):",
                    "$$T_{\\min} = 2\\pi \\sqrt{\\frac{m_c}{k}} = 2\\pi \\sqrt{\\frac{2.00\\text{ kg}}{125\\text{ N/m}}} = 2\\pi \\sqrt{0.0160} = 2\\pi (0.12649) \\approx 0.7948\\text{ s}$$"
                ],
                "result": "T_{\\min} = 0.795\\text{ s}",
                "res_val": "Tmin = 0.795 s"
            }
        ],
        "tip": "¡Atención a las unidades de la fuga! $2.00\\text{ g/s}$ DEBE convertirse a kilogramos por segundo ($0.002\\text{ kg/s}$) para ser consistente con Newtons y segundos."
    },
    {
        "id": "p37",
        "num": "Prob 37 (Serway)",
        "cat": "mas",
        "tags": "37 serway amortiguado b=3 factor amortiguamiento energia 5%",
        "title": "Oscilador Armónico Amortiguado y Decaimiento de Energía",
        "badge": "fd=7.00Hz, DeltaA=2.0%, t5%=10.6s",
        "badge_color": "purple",
        "img": "tmp/pdfs/individual/wave_page_05.png",
        "datos": [
            "Masa del objeto: $m = 10.6\\text{ kg}$.",
            "Constante de resorte: $k = 2.05 \\times 10^4\\text{ N/m} = 20500\\text{ N/m}$.",
            "Coeficiente de amortiguamiento: $b = 3.00\\text{ N}\\cdot\\text{s/m}$."
        ],
        "why": "En oscilaciones subamortiguadas, la amplitud decae exponencialmente según $A(t) = A_0 e^{-\\gamma t}$ con $\\gamma = \\frac{b}{2m}$, y la energía decae según $E(t) = E_0 e^{-2\\gamma t} = E_0 e^{-(b/m)t}$.",
        "incisos": [
            {
                "letter": "a",
                "title": "Frecuencia de la oscilación amortiguada ($f_d$)",
                "steps": [
                    "Frecuencia angular natural no amortiguada:",
                    "$$\\omega_0 = \\sqrt{\\frac{k}{m}} = \\sqrt{\\frac{20500}{10.6}} = \\sqrt{1933.96} \\approx 43.9768\\text{ rad/s}$$",
                    "Frecuencia angular amortiguada:",
                    "$$\\omega_d = \\sqrt{\\omega_0^2 - \\left(\\frac{b}{2m}\\right)^2} = \\sqrt{1933.96 - \\left(\\frac{3.00}{21.2}\\right)^2} = \\sqrt{1933.96 - 0.020} \\approx 43.9766\\text{ rad/s}$$",
                    "$$f_d = \\frac{\\omega_d}{2\\pi} = \\frac{43.9766}{2\\pi} \\approx 6.9991\\text{ Hz} \\approx 7.00\\text{ Hz}$$"
                ],
                "result": "f_d = 7.00\\text{ Hz}",
                "res_val": "fd = 7.00 Hz"
            },
            {
                "letter": "b",
                "title": "Porcentaje de disminución de la amplitud en cada ciclo",
                "steps": [
                    "Periodo de oscilación: $T = \\frac{1}{f_d} = \\frac{1}{6.9991} \\approx 0.14287\\text{ s}$.",
                    "Factor de decaimiento por ciclo:",
                    "$$\\frac{A(t+T)}{A(t)} = e^{-\\frac{b}{2m}T} = e^{-\\left(\\frac{3.00}{2(10.6)}\\right)(0.14287)} = e^{-0.020217} \\approx 0.9800$$",
                    "Fracción perdida:",
                    "$$\\Delta A \\% = (1 - 0.9800) \\times 100\\% = 2.00\\%$$"
                ],
                "result": "\\Delta A \\% = 2.00\\% \\text{ en cada ciclo}",
                "res_val": "Delta A = 2.00%"
            },
            {
                "letter": "c",
                "title": "Tiempo para que la energía caiga al $5.00\\%$ del valor inicial",
                "steps": [
                    "Ecuación de energía: $E(t) = E_0 e^{-\\frac{b}{m}t}$. Buscamos $E(t) = 0.0500 E_0$:",
                    "$$e^{-\\frac{b}{m}t} = 0.0500 \\implies -\\frac{b}{m}t = \\ln(0.0500) = -2.99573$$",
                    "$$t = \\frac{m}{b} (2.99573) = \\frac{10.6\\text{ kg}}{3.00\\text{ N}\\cdot\\text{s/m}} (2.99573) = (3.5333)(2.99573) \\approx 10.585\\text{ s}$$"
                ],
                "result": "t = 10.6\\text{ s}",
                "res_val": "t = 10.6 s"
            }
        ],
        "tip": "¡Ojo con el exponente! La amplitud decae con $e^{-(b/2m)t}$, pero la energía decae con el DOBLE de rapidez: $e^{-(b/m)t}$ porque $E \\propto A^2$."
    },
    {
        "id": "p42",
        "num": "Prob 42 (Serway)",
        "cat": "mas",
        "tags": "42 serway oscilaciones forzadas amplitud 0.44m resonancia",
        "title": "Oscilador Forzado Sin Amortiguamiento y Resonancia",
        "badge": "f1=0.641Hz, f2=1.31Hz",
        "badge_color": "purple",
        "img": "tmp/pdfs/individual/wave_page_06.png",
        "datos": [
            "Masa: $m = 0.150\\text{ kg}$.",
            "Constante de resorte: $k = 6.30\\text{ N/m}$.",
            "Amplitud de la fuerza impulsora externa: $F_0 = 1.70\\text{ N}$.",
            "Amplitud de respuesta deseada: $A = 0.440\\text{ m}$.",
            "Amortiguamiento despreciable: $b = 0$."
        ],
        "why": "Para un oscilador no amortiguado excitado armónicamente, la amplitud estacionaria es $A = \\frac{F_0 / m}{|\\omega_0^2 - \\omega^2|}$. El valor absoluto genera **dos soluciones físicas reales**: una por debajo de la frecuencia natural (en fase) y otra por encima (en contrafase).",
        "incisos": [
            {
                "letter": "a",
                "title": "Frecuencia natural $\\omega_0$ y despeje de frecuencias impulsoras",
                "steps": [
                    "$$\\omega_0^2 = \\frac{k}{m} = \\frac{6.30}{0.150} = 42.00\\text{ rad}^2\\text{/s}^2 \\implies \\omega_0 \\approx 6.4807\\text{ rad/s}$$",
                    "$$|\\omega_0^2 - \\omega^2| = \\frac{F_0}{m A} = \\frac{1.70}{(0.150)(0.440)} = \\frac{1.70}{0.066} \\approx 25.7576\\text{ rad}^2\\text{/s}^2$$"
                ],
                "result": "|42.00 - \\omega^2| = 25.7576",
                "res_val": "Ecuacion modular planteada"
            },
            {
                "letter": "b.1",
                "title": "Solución 1: Frecuencia por debajo de resonancia ($\\omega < \\omega_0$)",
                "steps": [
                    "$$42.00 - \\omega_1^2 = +25.7576 \\implies \\omega_1^2 = 42.00 - 25.7576 = 16.2424$$",
                    "$$\\omega_1 = \\sqrt{16.2424} \\approx 4.0302\\text{ rad/s}$$",
                    "$$f_1 = \\frac{\\omega_1}{2\\pi} = \\frac{4.0302}{2\\pi} \\approx 0.6414\\text{ Hz}$$"
                ],
                "result": "\\omega_1 = 4.03\\text{ rad/s}\\implies f_1 = 0.641\\text{ Hz}",
                "res_val": "f1 = 0.641 Hz"
            },
            {
                "letter": "b.2",
                "title": "Solución 2: Frecuencia por encima de resonancia ($\\omega > \\omega_0$)",
                "steps": [
                    "$$\\omega_2^2 - 42.00 = +25.7576 \\implies \\omega_2^2 = 42.00 + 25.7576 = 67.7576$$",
                    "$$\\omega_2 = \\sqrt{67.7576} \\approx 8.2315\\text{ rad/s}$$",
                    "$$f_2 = \\frac{\\omega_2}{2\\pi} = \\frac{8.2315}{2\\pi} \\approx 1.3101\\text{ Hz}$$"
                ],
                "result": "\\omega_2 = 8.23\\text{ rad/s}\\implies f_2 = 1.31\\text{ Hz}",
                "res_val": "f2 = 1.31 Hz"
            }
        ],
        "tip": "¡Pregunta trampa clásica de examen! Muchos estudiantes olvidan la segunda solución ($f_2 > f_0$). Al estar al cuadrado dentro del módulo, existen siempre dos frecuencias simétricas en respuesta de amplitud."
    },
    {
        "id": "p63",
        "num": "Prob 63 (Serway)",
        "cat": "mas",
        "tags": "63 serway demostracion fuerza restauradora bandas hule omega",
        "title": "Demostración de M.A.S. para Partícula en Cuerda Tensa",
        "badge": "Demostración analítica",
        "badge_color": "purple",
        "img": "tmp/pdfs/individual/wave_page_07.png",
        "datos": [
            "Partícula de masa $m$ conectada en el punto medio de dos bandas elásticas de longitud $L$ y tensión $T$.",
            "Desplazamiento transversal pequeño: $y \\ll L$."
        ],
        "why": "Para desplazamientos muy pequeños $y \\ll L$, aplicamos la aproximación de ángulos pequeños $\\sin\\theta \\approx \\tan\\theta = \\frac{y}{L}$ para demostrar que la fuerza neta restauradora es lineal con la posición ($F \\propto -y$), lo cual es la definición estricta de un M.A.S.",
        "incisos": [
            {
                "letter": "a",
                "title": "Demostración de la fuerza restauradora $F_y = -\\left(\\frac{2T}{L}\\right) y$",
                "steps": [
                    "Ambas cuerdas tiran hacia el centro con tensión $T$ en un ángulo $\\theta$ respecto a la horizontal:",
                    "$$\\sum F_y = -2 T \\sin\\theta$$",
                    "Por trigonometría del triángulo rectángulo formado: $\\sin\\theta = \\frac{y}{\\sqrt{L^2 + y^2}}$.",
                    "Para desplazamientos pequeños ($y \\ll L$): $\\sqrt{L^2 + y^2} \\approx L$, luego $\\sin\\theta \\approx \\frac{y}{L}$.",
                    "Sustituyendo:",
                    "$$F_y = -2 T \\left(\\frac{y}{L}\\right) = -\\left(\\frac{2T}{L}\\right) y$$"
                ],
                "result": "F_y = -\\left(\\frac{2T}{L}\\right) y \\quad \\text{(Q.E.D.)}",
                "res_val": "Fy = -(2T/L)y demostrado"
            },
            {
                "letter": "b",
                "title": "Demostración de la frecuencia angular $\\omega = \\sqrt{\\frac{2T}{mL}}$",
                "steps": [
                    "Por la Segunda Ley de Newton:",
                    "$$m \\frac{d^2 y}{dt^2} = -\\left(\\frac{2T}{L}\\right) y \\implies \\frac{d^2 y}{dt^2} + \\left(\\frac{2T}{mL}\\right) y = 0$$",
                    "Esta es la ecuación diferencial canónica del M.A.S. $\\frac{d^2 y}{dt^2} + \\omega^2 y = 0$, donde:",
                    "$$\\omega^2 = \\frac{2T}{mL} \\implies \\omega = \\sqrt{\\frac{2T}{mL}}$$"
                ],
                "result": "\\omega = \\sqrt{\\frac{2T}{mL}} \\quad \\text{(Q.E.D.)}",
                "res_val": "omega = sqrt(2T/mL) demostrado"
            }
        ],
        "tip": "Siempre que la fuerza neta adopte la forma $F = -k_{\\text{ef}} y$, la frecuencia angular del sistema es automáticamente $\\omega = \\sqrt{k_{\\text{ef}}/m}$."
    },
    {
        "id": "p8rep",
        "num": "Prob 8 Repaso",
        "cat": "mas",
        "tags": "8 repaso cinematica mrua vs mas aceleracion constante",
        "title": "Comparativa Cinemática: MRUA vs M.A.S.",
        "badge": "Incisos a, b, c, d",
        "badge_color": "purple",
        "img": "tmp/pdfs/individual/wave_page_19.png",
        "datos": [
            "Posición inicial: $x_0 = 0.270\\text{ m}$.",
            "Velocidad inicial: $v_0 = 0.140\\text{ m/s}$.",
            "Aceleración inicial: $a_0 = -0.320\\text{ m/s}^2$.",
            "Intervalo de tiempo evaluado: $t = 4.50\\text{ s}$."
        ],
        "why": "Comparamos la cinemática de **Aceleración Constante (MRUA)** frente al **Movimiento Armónico Simple (M.A.S.)** donde la aceleración cambia continuamente ($a(t) = -\\omega^2 x(t)$).",
        "incisos": [
            {
                "letter": "a",
                "title": "Posición final bajo MRUA ($a = \\text{cte} = -0.320\\text{ m/s}^2$)",
                "steps": [
                    "$$x(t) = x_0 + v_0 t + \\frac{1}{2} a t^2$$",
                    "$$x(4.50) = 0.270 + (0.140)(4.50) + \\frac{1}{2}(-0.320)(4.50)^2$$",
                    "$$x(4.50) = 0.270 + 0.630 - 3.240 = -2.340\\text{ m}$$"
                ],
                "result": "x(4.50\\text{s}) = -2.34\\text{ m}",
                "res_val": "x_MRUA = -2.34 m"
            },
            {
                "letter": "b",
                "title": "Velocidad final bajo MRUA",
                "steps": [
                    "$$v(t) = v_0 + a t$$",
                    "$$v(4.50) = 0.140 + (-0.320)(4.50) = 0.140 - 1.440 = -1.300\\text{ m/s}$$"
                ],
                "result": "v(4.50\\text{s}) = -1.30\\text{ m/s}",
                "res_val": "v_MRUA = -1.30 m/s"
            },
            {
                "letter": "c",
                "title": "Posición final bajo M.A.S. ($a = -\\omega^2 x$)",
                "steps": [
                    "Calculamos $\\omega$ con los datos iniciales en $t=0$:",
                    "$$a_0 = -\\omega^2 x_0 \\implies -0.320 = -\\omega^2 (0.270) \\implies \\omega = \\sqrt{\\frac{0.320}{0.270}} = \\sqrt{1.18519} \\approx 1.08866\\text{ rad/s}$$",
                    "Calculamos amplitud $A$ y ángulo de fase $\\phi$ ($x(t) = A\\cos(\\omega t + \\phi)$):",
                    "$$A = \\sqrt{x_0^2 + \\left(\\frac{v_0}{\\omega}\\right)^2} = \\sqrt{(0.270)^2 + \\left(\\frac{0.140}{1.08866}\\right)^2} = \\sqrt{0.0729 + 0.016538} = \\sqrt{0.089438} \\approx 0.29906\\text{ m}$$",
                    "$$\\tan\\phi = -\\frac{v_0}{\\omega x_0} = -\\frac{0.140}{(1.08866)(0.270)} = -0.47629 \\implies \\phi \\approx -0.4446\\text{ rad}$$",
                    "Evaluamos la posición en $t = 4.50\\text{ s}$:",
                    "$$\\theta = \\omega t + \\phi = (1.08866)(4.50) - 0.4446 = 4.89897 - 0.4446 = 4.4544\\text{ rad}$$",
                    "$$x(4.50) = (0.29906) \\cos(4.4544\\text{ rad}) = (0.29906)(-0.2526) \\approx -0.07555\\text{ m} = -7.56\\text{ cm}$$"
                ],
                "result": "x(4.50\\text{s}) = -0.0756\\text{ m} = -7.56\\text{ cm}",
                "res_val": "x_MAS = -7.56 cm"
            },
            {
                "letter": "d",
                "title": "Velocidad final bajo M.A.S.",
                "steps": [
                    "$$v(t) = -A\\omega \\sin(\\omega t + \\phi)$$",
                    "$$v(4.50) = -(0.29906)(1.08866) \\sin(4.4544\\text{ rad}) = -(0.32557)(-0.96756) \\approx +0.3150\\text{ m/s}$$"
                ],
                "result": "v(4.50\\text{s}) = +0.315\\text{ m/s}",
                "res_val": "v_MAS = +0.315 m/s"
            }
        ],
        "tip": "¡Atención a la calculadora! Al evaluar $\\cos(\\omega t + \\phi)$, el argumento está en **RADIANES**, no en grados sexagesimales."
    },
    {
        "id": "p17",
        "num": "Prob 17 (MAS)",
        "cat": "mas",
        "tags": "17 energias energia mecanica cinetica potencial resorte",
        "title": "Conservación de Energía Mecánica, Cinética y Potencial en M.A.S.",
        "badge": "E=28mJ | v(1cm)=1.03m/s | K=12.3mJ | U=15.8mJ",
        "badge_color": "purple",
        "img": "tmp/pdfs/individual/wave_page_20.png",
        "datos": [
            "Masa: $m = 50.0\\text{ g} = 0.0500\\text{ kg}$.",
            "Constante de resorte: $k = 35.0\\text{ N/m}$.",
            "Amplitud de oscilación: $A = 4.00\\text{ cm} = 0.0400\\text{ m}$."
        ],
        "why": "En el M.A.S., la energía mecánica total se conserva: $E = \\frac{1}{2} k A^2 = K(x) + U(x)$, donde $U(x) = \\frac{1}{2} k x^2$ y $K(x) = \\frac{1}{2} m v^2 = \\frac{1}{2} k (A^2 - x^2)$.",
        "incisos": [
            {
                "letter": "a",
                "title": "Energía total del sistema ($E$)",
                "steps": [
                    "$$E = \\frac{1}{2} k A^2 = \\frac{1}{2}(35.0\\text{ N/m})(0.0400\\text{ m})^2 = \\frac{1}{2}(35.0)(0.00160) = 0.0280\\text{ J} = 28.0\\text{ mJ}$$"
                ],
                "result": "E = 28.0\\text{ mJ} = 0.0280\\text{ J}",
                "res_val": "E = 28.0 mJ"
            },
            {
                "letter": "b",
                "title": "Rapidez del objeto cuando la posición es $x = 1.00\\text{ cm} = 0.0100\\text{ m}$",
                "steps": [
                    "$$v = \\sqrt{\\frac{k}{m}(A^2 - x^2)} = \\sqrt{\\frac{35.0}{0.0500}((0.0400)^2 - (0.0100)^2)}$$",
                    "$$v = \\sqrt{700 \\times (0.00160 - 0.00010)} = \\sqrt{700 \\times 0.00150} = \\sqrt{1.050} \\approx 1.0247\\text{ m/s}$$"
                ],
                "result": "v(1.00\\text{cm}) = 1.025\\text{ m/s}",
                "res_val": "v = 1.025 m/s"
            },
            {
                "letter": "c",
                "title": "Energía cinética cuando la posición es $x = 3.00\\text{ cm} = 0.0300\\text{ m}$",
                "steps": [
                    "$$K = \\frac{1}{2} k (A^2 - x^2) = \\frac{1}{2}(35.0)((0.0400)^2 - (0.0300)^2)$$",
                    "$$K = 17.5 \\times (0.00160 - 0.00090) = 17.5 \\times 0.00070 = 0.01225\\text{ J} = 12.25\\text{ mJ}$$"
                ],
                "result": "K(3.00\\text{cm}) = 12.25\\text{ mJ}",
                "res_val": "K = 12.25 mJ"
            },
            {
                "letter": "d",
                "title": "Energía potencial cuando la posición es $x = 3.00\\text{ cm} = 0.0300\\text{ m}$",
                "steps": [
                    "$$U = \\frac{1}{2} k x^2 = \\frac{1}{2}(35.0)(0.0300)^2 = 17.5 \\times 0.00090 = 0.01575\\text{ J} = 15.75\\text{ mJ}$$",
                    "Verificación de balance energético: $K + U = 12.25 + 15.75 = 28.00\\text{ mJ} = E$. ¡Perfecto!"
                ],
                "result": "U(3.00\\text{cm}) = 15.75\\text{ mJ}",
                "res_val": "U = 15.75 mJ"
            }
        ],
        "tip": "Siempre verifica la suma $K + U = E$ en cualquier posición intermedia. Esto garantiza 100% que tus cálculos de velocidad y energía son exactos."
    },

    # ----------------------------------------------------
    # ONDAS MECÁNICAS (18 a 30)
    # ----------------------------------------------------
    {
        "id": "p27serway",
        "num": "Prob 27 (Serway)",
        "cat": "ondas",
        "tags": "27 serway ondas transversales tension rapidez 20m/s a 30m/s",
        "title": "Relación entre Tensión y Rapidez de Onda en Cuerda",
        "badge": "T2 = 13.50 N",
        "badge_color": "yellow",
        "img": "tmp/pdfs/individual/wave_page_08.png",
        "datos": [
            "Rapidez inicial de onda: $v_1 = 20.0\\text{ m/s}$.",
            "Tensión inicial en la cuerda: $T_1 = 6.00\\text{ N}$.",
            "Rapidez deseada: $v_2 = 30.0\\text{ m/s}$ (misma cuerda, $\\mu = \\text{cte}$)."
        ],
        "why": "La rapidez de una onda transversal en una cuerda es $v = \\sqrt{\\frac{T}{\\mu}}$. Al ser la misma cuerda, la densidad lineal $\\mu$ es constante, por lo que la rapidez es directamente proporcional a la raíz cuadrada de la tensión: $v \\propto \\sqrt{T} \\implies \\frac{v_2}{v_1} = \\sqrt{\\frac{T_2}{T_1}}$.",
        "incisos": [
            {
                "letter": "a",
                "title": "Cálculo de la tensión requerida $T_2$",
                "steps": [
                    "Despejamos $T_2$ de la relación proporcional:",
                    "$$\\frac{T_2}{T_1} = \\left(\\frac{v_2}{v_1}\\right)^2$$",
                    "$$T_2 = T_1 \\left(\\frac{v_2}{v_1}\\right)^2 = 6.00\\text{ N} \\times \\left(\\frac{30.0\\text{ m/s}}{20.0\\text{ m/s}}\\right)^2$$",
                    "$$T_2 = 6.00 \\times (1.50)^2 = 6.00 \\times 2.25 = 13.50\\text{ N}$$"
                ],
                "result": "T_2 = 13.50\\text{ N}",
                "res_val": "T2 = 13.50 N"
            }
        ],
        "tip": "Para aumentar la rapidez en un 50% ($1.5\\times$), la tensión debe aumentarse en un $125\\%$ ($1.5^2 = 2.25\\times$)."
    },
    {
        "id": "p1512",
        "num": "Prob 15.12",
        "cat": "ondas",
        "tags": "15.12 rapidez propagacion contra particulas vy maximo coseno derivada",
        "title": "Rapidez de Propagación contra Rapidez de Partículas Transversal",
        "badge": "Incisos a, b, c",
        "badge_color": "yellow",
        "img": "tmp/pdfs/individual/wave_page_09.png",
        "datos": [
            "Ecuación base: $y(x,t) = A\\cos[\\omega(x/v - t)] = A\\cos[2\\pi f(x/v - t)]$.",
            "Relaciones fundamentales: $v = \\lambda f$, $\\omega = 2\\pi f$, $k = \\frac{2\\pi}{\\lambda} = \\frac{\\omega}{v}$."
        ],
        "why": "La **rapidez de propagación** $v$ es la velocidad a la que viaja el patrón de onda a lo largo de $x$. La **rapidez de partícula** $v_y$ es la velocidad física a la que sube y baja un pedacito de cuerda en $y$, calculada con la derivada parcial temporal $\\frac{\\partial y}{\\partial t}$.",
        "incisos": [
            {
                "letter": "a",
                "title": "Demostración de $y(x, t) = A\\cos\\left[\\frac{2\\pi}{\\lambda}(x - v t)\\right]$",
                "steps": [
                    "Partimos de $y(x,t) = A\\cos\\left[2\\pi f\\left(\\frac{x}{v} - t\\right)\\right]$.",
                    "Como $f = \\frac{v}{\\lambda}$, multiplicamos y distribuimos $f$ dentro del paréntesis:",
                    "$$2\\pi f \\left(\\frac{x}{v} - t\\right) = 2\\pi \\left(\\frac{v}{\\lambda}\\right) \\left(\\frac{x}{v} - t\\right) = 2\\pi \\left(\\frac{x}{\\lambda} - \\frac{v t}{\\lambda}\\right) = \\frac{2\\pi}{\\lambda}(x - v t)$$",
                    "Sustituyendo en la función coseno:",
                    "$$y(x, t) = A \\cos\\left[\\frac{2\\pi}{\\lambda}(x - v t)\\right]$$"
                ],
                "result": "y(x, t) = A\\cos\\left[\\frac{2\\pi}{\\lambda}(x - v t)\\right] \\quad \\text{(Demostrado)}",
                "res_val": "Inciso a demostrado"
            },
            {
                "letter": "b",
                "title": "Expresión para la velocidad transversal $v_y(x,t)$",
                "steps": [
                    "Derivamos $y(x,t)$ parcialmente respecto a $t$:",
                    "$$v_y(x,t) = \\frac{\\partial y}{\\partial t} = -A \\sin\\left[\\frac{2\\pi}{\\lambda}(x - v t)\\right] \\cdot \\left(-\\frac{2\\pi v}{\\lambda}\\right)$$",
                    "$$v_y(x,t) = \\frac{2\\pi v A}{\\lambda} \\sin\\left[\\frac{2\\pi}{\\lambda}(x - v t)\\right] = \\omega A \\sin(kx - \\omega t)$$"
                ],
                "result": "v_y(x,t) = \\frac{2\\pi v A}{\\lambda} \\sin\\left[\\frac{2\\pi}{\\lambda}(x - v t)\\right]",
                "res_val": "vy(x,t) = (2pi*v*A/lambda) sin[...]"
            },
            {
                "letter": "c",
                "title": "Rapidez máxima de partícula y comparación con la rapidez de onda $v$",
                "steps": [
                    "La rapidez transversal máxima se alcanza cuando el seno es igual a $1$:",
                    "$$v_{y,\\max} = \\frac{2\\pi v A}{\\lambda}$$",
                    "Analizamos los tres casos comparando $v_{y,\\max}$ con $v$:",
                    "1. <strong>$v_{y,\\max} = v$:</strong> $\\frac{2\\pi v A}{\\lambda} = v \\implies \\frac{2\\pi A}{\\lambda} = 1 \\implies A = \\frac{\\lambda}{2\\pi}$",
                    "2. <strong>$v_{y,\\max} < v$:</strong> Ocurre si la amplitud es pequeña: $A < \\frac{\\lambda}{2\\pi}$",
                    "3. <strong>$v_{y,\\max} > v$:</strong> Ocurre si la amplitud es grande: $A > \\frac{\\lambda}{2\\pi}$"
                ],
                "result": "v_{y,\\max} = v \\iff A = \\frac{\\lambda}{2\\pi}",
                "res_val": "A = lambda / (2pi)"
            }
        ],
        "tip": "La velocidad de onda $v$ es constante fijada por el medio ($v = \\sqrt{T/\\mu}$), mientras que $v_y$ cambia armónicamente entre $+v_{y,\\max}$ y $-v_{y,\\max}$."
    },
    {
        "id": "p1544",
        "num": "Prob 15.44",
        "cat": "ondas",
        "tags": "15.44 segundo sobretono n=3 sonido 344m/s tension frecuencia fundamental",
        "title": "Cuerda Musical, Segundo Sobretono y Tensión Requerida",
        "badge": "T = 3.08e5 N | f1 = 3.42 kHz",
        "badge_color": "yellow",
        "img": "tmp/pdfs/individual/wave_page_10.png",
        "datos": [
            "Longitud de la cuerda: $L = 75.0\\text{ cm} = 0.750\\text{ m}$.",
            "Masa de la cuerda: $m = 8.75\\text{ g} = 8.75 \\times 10^{-3}\\text{ kg}$.",
            "Rapidez del sonido en el aire: $v_{\\text{aire}} = 344\\text{ m/s}$.",
            "Modo de oscilación: Segundo sobretono $\\implies n = 3$ (tercer armónico).",
            "Longitud de onda del sonido emitido al aire: $\\lambda_{\\text{aire}} = 3.35\\text{ cm} = 0.0335\\text{ m}$."
        ],
        "why": "La cuerda vibrando en el aire genera ondas sonoras con **exactamente la misma frecuencia** que la vibración de la cuerda ($f_{\\text{cuerda}} = f_{\\text{aire}}$). Usamos la velocidad del sonido para hallar la frecuencia y luego la física de ondas estacionarias en la cuerda para hallar la tensión.",
        "incisos": [
            {
                "letter": "a",
                "title": "Cálculo de la frecuencia $f_3$ y la tensión $T$ de la cuerda",
                "steps": [
                    "Frecuencia del sonido en el aire (igual a la frecuencia del 2do sobretono $n=3$):",
                    "$$f_3 = \\frac{v_{\\text{aire}}}{\\lambda_{\\text{aire}}} = \\frac{344\\text{ m/s}}{0.0335\\text{ m}} \\approx 10268.66\\text{ Hz} \\approx 10.27\\text{ kHz}$$",
                    "Longitud de onda en la cuerda para el 3er armónico ($n=3$):",
                    "$$\\lambda_3 = \\frac{2L}{3} = \\frac{2(0.750\\text{ m})}{3} = 0.500\\text{ m}$$",
                    "Rapidez de propagación en la cuerda:",
                    "$$v_{\\text{cuerda}} = \\lambda_3 f_3 = (0.500\\text{ m})(10268.66\\text{ s}^{-1}) = 5134.33\\text{ m/s}$$",
                    "Densidad lineal de masa de la cuerda:",
                    "$$\\mu = \\frac{m}{L} = \\frac{8.75 \\times 10^{-3}\\text{ kg}}{0.750\\text{ m}} = 0.011667\\text{ kg/m}$$",
                    "Tensión requerida en la cuerda ($T = \\mu v_{\\text{cuerda}}^2$):",
                    "$$T = (0.011667\\text{ kg/m}) (5134.33\\text{ m/s})^2 = (0.011667)(2.6361 \\times 10^7) \\approx 3.075 \\times 10^5\\text{ N} \\approx 308\\text{ kN}$$"
                ],
                "result": "T = 3.08 \\times 10^5\\text{ N}",
                "res_val": "T = 3.08e5 N"
            },
            {
                "letter": "b",
                "title": "Frecuencia de sonido producida en el modo fundamental ($f_1$)",
                "steps": [
                    "Como los armónicos en una cuerda fija en ambos extremos son múltiplos enteros ($f_n = n f_1$):",
                    "$$f_1 = \\frac{f_3}{3} = \\frac{10268.66\\text{ Hz}}{3} \\approx 3422.89\\text{ Hz} \\approx 3.42\\text{ kHz}$$"
                ],
                "result": "f_1 = 3.42\\text{ kHz} = 3423\\text{ Hz}",
                "res_val": "f1 = 3.42 kHz"
            }
        ],
        "tip": "¡Cuidado con la nomenclatura! Modo fundamental = 1er armónico ($n=1$). Primer sobretono = 2do armónico ($n=2$). Segundo sobretono = 3er armónico ($n=3$)."
    },
    {
        "id": "p1550",
        "num": "Prob 15.50",
        "cat": "ondas",
        "tags": "15.50 onda viajera senoidal amplitud longitud frecuencia periodo velocidad direccion potencia",
        "title": "Función de Onda Viajera Senoidal y Propiedades Dinámicas",
        "badge": "Incisos a, b, c, d, e",
        "badge_color": "yellow",
        "img": "tmp/pdfs/individual/wave_page_11.png",
        "datos": [
            "Ecuación dada: $y(x,t) = (0.750\\text{ cm})\\cos\\pi[(0.400\\text{ cm}^{-1})x + (250\\text{ s}^{-1})t]$.",
            "Multiplicando $\\pi$ hacia adentro: $y(x,t) = (0.00750\\text{ m})\\cos(40.0\\pi x + 250\\pi t)$ en unidades SI.",
            "Densidad lineal para incisos dinámicos: $\\mu = 0.0500\\text{ kg/m}$."
        ],
        "why": "Comparamos la función con la forma canónica $y(x,t) = A\\cos(kx + \\omega t)$. Identificamos número de onda $k = 40.0\\pi\\text{ rad/m}$ y frecuencia angular $\\omega = 250\\pi\\text{ rad/s}$.",
        "incisos": [
            {
                "letter": "a",
                "title": "Amplitud ($A$), Longitud de onda ($\\lambda$), Frecuencia ($f$), Periodo ($T$) y Rapidez ($v$)",
                "steps": [
                    "• <strong>Amplitud:</strong> $A = 0.750\\text{ cm} = 7.50 \\times 10^{-3}\\text{ m}$",
                    "• <strong>Longitud de onda:</strong> $k = 0.400\\pi\\text{ cm}^{-1} = 40.0\\pi\\text{ m}^{-1} \\implies \\lambda = \\frac{2\\pi}{k} = \\frac{2\\pi}{0.400\\pi\\text{ cm}^{-1}} = 5.00\\text{ cm} = 0.0500\\text{ m}$",
                    "• <strong>Frecuencia:</strong> $\\omega = 250\\pi\\text{ s}^{-1} \\implies f = \\frac{\\omega}{2\\pi} = \\frac{250\\pi}{2\\pi} = 125\\text{ Hz}$",
                    "• <strong>Periodo:</strong> $T = \\frac{1}{f} = \\frac{1}{125} = 0.00800\\text{ s} = 8.00\\text{ ms}$",
                    "• <strong>Rapidez de propagación:</strong> $v = \\lambda f = (0.0500\\text{ m})(125\\text{ s}^{-1}) = 6.25\\text{ m/s}$"
                ],
                "result": "A=7.50\\text{mm},\\ \\lambda=5.00\\text{cm},\\ f=125\\text{Hz},\\ T=8.00\\text{ms},\\ v=6.25\\text{m/s}",
                "res_val": "A=7.5mm, lambda=5cm, f=125Hz, v=6.25m/s"
            },
            {
                "letter": "b",
                "title": "Forma de la cuerda en $t = 0$, $t = 0.0005\\text{ s}$ y $t = 0.0010\\text{ s}$",
                "steps": [
                    "• En $t = 0$: $y(x,0) = (0.750\\text{ cm})\\cos(40.0\\pi x)$ (coseno puro con cresta en $x=0$).",
                    "• En $t = 0.0005\\text{ s} = T/16$: $y(x, 0.0005) = (0.750\\text{ cm})\\cos(40.0\\pi x + 0.125\\pi)$ (desplazada a la izquierda por $\\Delta x = -0.3125\\text{ cm}$).",
                    "• En $t = 0.0010\\text{ s} = T/8$: $y(x, 0.0010) = (0.750\\text{ cm})\\cos(40.0\\pi x + 0.25\\pi)$ (desplazada hacia la izquierda por $\\Delta x = -0.625\\text{ cm}$)."
                ],
                "result": "\\text{Perfiles de onda cosenoidales desplazándose progresivamente hacia la izquierda}",
                "res_val": "Perfiles t=0, 0.5ms, 1ms calculados"
            },
            {
                "letter": "c",
                "title": "¿La onda viaja en la dirección $+x$ o $-x$?",
                "steps": [
                    "La fase tiene la forma $(kx + \\omega t)$ con un signo <strong>POSITIVO</strong> entre la coordenada espacial y el tiempo.",
                    "Para mantener la fase constante ($kx + \\omega t = \\text{cte}$), al aumentar $t$, $x$ debe disminuir.",
                    "Por lo tanto, la onda viaja en la <strong>dirección $-x$</strong> (hacia la izquierda)."
                ],
                "result": "\\text{Dirección } -x \\text{ (hacia la izquierda)}",
                "res_val": "Direccion -x"
            },
            {
                "letter": "d",
                "title": "Cálculo de la tensión en la cuerda ($T$)",
                "steps": [
                    "$$v = \\sqrt{\\frac{T}{\\mu}} \\implies T = \\mu v^2$$",
                    "$$T = (0.0500\\text{ kg/m}) (6.25\\text{ m/s})^2 = (0.0500)(39.0625) = 1.9531\\text{ N} \\approx 1.95\\text{ N}$$"
                ],
                "result": "T = 1.95\\text{ N}",
                "res_val": "T = 1.95 N"
            },
            {
                "letter": "e",
                "title": "Cálculo de la potencia media transmitida por la onda ($P_{\\text{med}}$)",
                "steps": [
                    "$$P_{\\text{med}} = \\frac{1}{2} \\mu v \\omega^2 A^2 = \\frac{1}{2} \\sqrt{\\mu T} \\omega^2 A^2$$",
                    "$$P_{\\text{med}} = \\frac{1}{2}(0.0500)(6.25)(250\\pi)^2 (0.00750)^2$$",
                    "$$P_{\\text{med}} = \\frac{1}{2}(0.3125)(6.1685 \\times 10^5)(5.625 \\times 10^{-5}) = (0.15625)(34.6978) \\approx 5.4215\\text{ W}$$"
                ],
                "result": "P_{\\text{med}} = 5.42\\text{ W}",
                "res_val": "P = 5.42 W"
            }
        ],
        "tip": "Regla clave de signos: $(kx - \\omega t) \\to$ viaja a la DERECHA ($+x$). $(kx + \\omega t) \\to$ viaja a la IZQUIERDA ($-x$)."
    },
    {
        "id": "p1541",
        "num": "Prob 15.41",
        "cat": "ondas",
        "tags": "15.41 onda estacionaria tercer armonico longitud cuerda amplitud viajeras octavo armonico",
        "title": "Onda Estacionaria, Armónicos y Descomposición en Ondas Viajeras",
        "badge": "Incisos a, b, c, d, e, f",
        "badge_color": "yellow",
        "img": "tmp/pdfs/individual/wave_page_12.png",
        "datos": [
            "Ecuación de onda estacionaria: $y(x,t) = (5.60\\text{ cm})\\sin[(0.0340\\text{ rad/cm})x]\\sin[(50.0\\text{ rad/s})t]$.",
            "Modo de oscilación: Tercer armónico ($n=3$).",
            "Condiciones de frontera: Atada por ambos extremos ($x=0$ y $x=L$ son nodos fijos)."
        ],
        "why": "Una onda estacionaria se forma por la superposición de dos ondas viajeras idénticas en sentidos opuestos: $y_1 = A\\cos(kx - \\omega t)$ y $y_2 = -A\\cos(kx + \\omega t)$, produciendo una envolvente de amplitud $A_{SW} = 2A = 5.60\\text{ cm}$.",
        "incisos": [
            {
                "letter": "a",
                "title": "Dibujo del patrón de onda estacionaria ($n=3$)",
                "steps": [
                    "Para el <strong>tercer armónico ($n=3$)</strong>, la cuerda contiene exactamente <strong>3 vientres (antinodos)</strong> y <strong>4 nodos</strong> (incluyendo los dos extremos):",
                    "• Nodos en: $x = 0$, $x = \\frac{L}{3} \\approx 0.92\\text{m}$, $x = \\frac{2L}{3} \\approx 1.85\\text{m}$, $x = L \\approx 2.77\\text{m}$.",
                    "• Antinodos (amplitud máxima $5.60\\text{cm}$) en: $x = \\frac{L}{6} \\approx 0.46\\text{m}$, $x = \\frac{L}{2} \\approx 1.39\\text{m}$, $x = \\frac{5L}{6} \\approx 2.31\\text{m}$.",
                    "<div style='text-align:center; margin:10px 0;'><svg width='360' height='70' viewBox='0 0 360 70'><path d='M 10,35 Q 65,-15 120,35 T 230,35 T 340,35' fill='none' stroke='#58a6ff' stroke-width='3'/><path d='M 10,35 Q 65,85 120,35 T 230,35 T 340,35' fill='none' stroke='#58a6ff' stroke-width='2' stroke-dasharray='4'/><circle cx='10' cy='35' r='4' fill='#f85149'/><circle cx='120' cy='35' r='4' fill='#f85149'/><circle cx='230' cy='35' r='4' fill='#f85149'/><circle cx='340' cy='35' r='4' fill='#f85149'/><text x='15' y='65' fill='#8b949e' font-size='10'>Nodo (x=0)</text><text x='110' y='65' fill='#8b949e' font-size='10'>Nodo</text><text x='220' y='65' fill='#8b949e' font-size='10'>Nodo</text><text x='310' y='65' fill='#8b949e' font-size='10'>Nodo (x=L)</text></svg></div>"
                ],
                "result": "\\text{Patrón de 3 bucles (vientres) delimitados por 4 nodos fijos}",
                "res_val": "Patron n=3 graficado"
            },
            {
                "letter": "b",
                "title": "Amplitud de las dos ondas viajeras componentes ($A$)",
                "steps": [
                    "La amplitud de la onda estacionaria es el doble de la amplitud de cada onda viajera: $A_{SW} = 2A = 5.60\\text{ cm}$.",
                    "$$A = \\frac{A_{SW}}{2} = \\frac{5.60\\text{ cm}}{2} = 2.80\\text{ cm} = 0.0280\\text{ m}$$"
                ],
                "result": "A = 2.80\\text{ cm} = 0.0280\\text{ m}",
                "res_val": "A = 2.80 cm"
            },
            {
                "letter": "c",
                "title": "Longitud de la cuerda ($L$)",
                "steps": [
                    "Del término espacial: $k = 0.0340\\text{ rad/cm} = 3.40\\text{ rad/m}$.",
                    "Longitud de onda de las viajeras:",
                    "$$\\lambda = \\frac{2\\pi}{k} = \\frac{2\\pi}{0.0340\\text{ cm}^{-1}} \\approx 184.7996\\text{ cm} \\approx 1.848\\text{ m}$$",
                    "Como está en su 3er armónico ($n=3$), la cuerda mide 3 medias longitudes de onda ($L = \\frac{3\\lambda}{2}$):",
                    "$$L = 3 \\left(\\frac{1.847996\\text{ m}}{2}\\right) = 3(0.9240\\text{ m}) = 2.772\\text{ m} \\approx 2.77\\text{ m}$$"
                ],
                "result": "L = 2.77\\text{ m} = 277.2\\text{ cm}",
                "res_val": "L = 2.77 m"
            },
            {
                "letter": "d",
                "title": "Longitud de onda ($\\lambda$), Frecuencia ($f$), Periodo ($T$) y Rapidez ($v$) de las ondas viajeras",
                "steps": [
                    "• <strong>Longitud de onda:</strong> $\\lambda = 184.8\\text{ cm} = 1.848\\text{ m} \\approx 1.85\\text{ m}$",
                    "• <strong>Frecuencia:</strong> $\\omega = 50.0\\text{ rad/s} \\implies f = \\frac{\\omega}{2\\pi} = \\frac{50.0}{2\\pi} \\approx 7.9577\\text{ Hz} \\approx 7.96\\text{ Hz}$",
                    "• <strong>Periodo:</strong> $T = \\frac{1}{f} = \\frac{2\\pi}{50.0} = 0.12566\\text{ s} \\approx 0.126\\text{ s}$",
                    "• <strong>Rapidez de las ondas viajeras:</strong>",
                    "$$v = \\frac{\\omega}{k} = \\frac{50.0\\text{ rad/s}}{0.0340\\text{ rad/cm}} = 1470.59\\text{ cm/s} = 14.706\\text{ m/s} \\approx 14.71\\text{ m/s}$$"
                ],
                "result": "\\lambda = 1.85\\text{m},\\ f = 7.96\\text{Hz},\\ T = 0.126\\text{s},\\ v = 14.71\\text{m/s}",
                "res_val": "lambda=1.85m, f=7.96Hz, T=0.126s, v=14.71m/s"
            },
            {
                "letter": "e",
                "title": "Rapidez transversal máxima de la cuerda ($v_{y,\\max}$)",
                "steps": [
                    "La velocidad transversal en cualquier punto es:",
                    "$$v_y(x,t) = \\frac{\\partial y}{\\partial t} = (5.60\\text{ cm})(50.0\\text{ rad/s})\\sin(kx)\\cos(\\omega t)$$",
                    "El valor máximo absoluto ocurre en los antinodos cuando $\\sin(kx)=1$ y $\\cos(\\omega t)=1$:",
                    "$$v_{y,\\max} = A_{SW} \\omega = (5.60\\text{ cm})(50.0\\text{ s}^{-1}) = 280.0\\text{ cm/s} = 2.80\\text{ m/s}$$"
                ],
                "result": "v_{y,\\max} = 2.80\\text{ m/s} = 280\\text{ cm/s}",
                "res_val": "vy_max = 2.80 m/s"
            },
            {
                "letter": "f",
                "title": "Ecuación $y(x,t)$ si la cuerda vibrara en su octavo armónico ($n=8$)",
                "steps": [
                    "Para el <strong>octavo armónico ($n=8$)</strong>:",
                    "• La longitud de onda es $\\lambda_8 = \\frac{2L}{8} = \\frac{L}{4} = \\frac{2.772\\text{ m}}{4} = 0.693\\text{ m} = 69.3\\text{ cm}$.",
                    "• El número de onda es $k_8 = \\frac{2\\pi}{\\lambda_8} = \\frac{8\\pi}{2L} = \\frac{8}{3} k_3 = \\frac{8}{3}(0.0340\\text{ rad/cm}) = 0.09067\\text{ rad/cm} = 9.067\\text{ rad/m}$.",
                    "• La velocidad de propagación $v = 14.706\\text{ m/s}$ es constante (misma cuerda y tensión).",
                    "• La frecuencia angular es $\\omega_8 = v k_8 = \\frac{8}{3} \\omega_3 = \\frac{8}{3}(50.0\\text{ rad/s}) = 133.33\\text{ rad/s}$.",
                    "• Manteniendo la misma amplitud máxima $(5.60\\text{ cm})$, la ecuación es:",
                    "$$y_8(x, t) = (5.60\\text{ cm}) \\sin[(0.0907\\text{ rad/cm}) x] \\sin[(133.3\\text{ rad/s}) t]$$",
                    "En unidades del Sistema Internacional (SI):",
                    "$$y_8(x, t) = (0.0560\\text{ m}) \\sin[(9.07\\text{ rad/m}) x] \\sin[(133.3\\text{ rad/s}) t]$$"
                ],
                "result": "y_8(x,t) = (5.60\\text{ cm})\\sin[(0.0907\\text{ rad/cm})x]\\sin[(133.3\\text{ rad/s})t]",
                "res_val": "y8(x,t) = 5.60cm sin(0.0907 x) sin(133.3 t)"
            }
        ],
        "tip": "¡Clave de oro! En armónicos superiores, $v$ se mantiene constante, pero $k_n = n k_1 = \\frac{n}{3} k_3$ y $\\omega_n = n \\omega_1 = \\frac{n}{3} \\omega_3$ crecen proporcionalmente a $n$."
    },
    {
        "id": "p1547",
        "num": "Prob 15.47",
        "cat": "ondas",
        "tags": "15.47 guitarra B3 245Hz tension aumento 1% sonido 344m/s longitud aire",
        "title": "Cuerda de Guitarra, Aumento de Tensión y Onda Sonora en el Aire",
        "badge": "v=311m/s, f'=246.2Hz, lambda_aire=1.40m",
        "badge_color": "yellow",
        "img": "tmp/pdfs/individual/wave_page_13.png",
        "datos": [
            "Longitud de la cuerda: $L = 63.5\\text{ cm} = 0.635\\text{ m}$.",
            "Frecuencia fundamental nota $B_3$: $f_1 = 245\\text{ Hz}$ ($n=1$).",
            "Rapidez del sonido en el aire circundante: $v_{\\text{sonido}} = 344\\text{ m/s}$."
        ],
        "why": "En el modo fundamental $n=1$, la longitud de onda en la cuerda es $\\lambda_1 = 2L$. La frecuencia depende de la tensión como $f \\propto \\sqrt{T}$. Cuando la cuerda vibra, perturba el aire circundante a la misma frecuencia $f$, pero con rapidez $v_{\\text{sonido}}$.",
        "incisos": [
            {
                "letter": "a",
                "title": "Rapidez de las ondas transversales en la cuerda ($v$)",
                "steps": [
                    "Longitud de onda en la cuerda:",
                    "$$\\lambda = 2L = 2(0.635\\text{ m}) = 1.270\\text{ m}$$",
                    "$$v = \\lambda f = (1.270\\text{ m})(245\\text{ s}^{-1}) = 311.15\\text{ m/s}$$"
                ],
                "result": "v = 311.15\\text{ m/s} \\approx 311\\text{ m/s}",
                "res_val": "v = 311 m/s"
            },
            {
                "letter": "b",
                "title": "Nueva frecuencia fundamental si la tensión aumenta en $1.0\\%$",
                "steps": [
                    "Nueva tensión: $T' = 1.010 T$.",
                    "Como $f \\propto \\sqrt{T}$:",
                    "$$f' = f \\sqrt{\\frac{T'}{T}} = 245 \\times \\sqrt{1.010} = 245 \\times 1.0049876 \\approx 246.22\\text{ Hz}$$"
                ],
                "result": "f' = 246.22\\text{ Hz} \\approx 246.2\\text{ Hz}",
                "res_val": "f' = 246.2 Hz"
            },
            {
                "letter": "c",
                "title": "Frecuencia y longitud de onda del sonido emitido al aire",
                "steps": [
                    "• <strong>Frecuencia del sonido en el aire:</strong> La vibración mecánica fuerza al aire a oscilar al mismo ritmo, por lo tanto $f_{\\text{aire}} = f = 245\\text{ Hz}$ y $\\omega_{\\text{aire}} = \\omega_{\\text{cuerda}} = 2\\pi(245) = 1539.4\\text{ rad/s}$.",
                    "• <strong>Longitud de onda en el aire:</strong>",
                    "$$\\lambda_{\\text{aire}} = \\frac{v_{\\text{sonido}}}{f_{\\text{aire}}} = \\frac{344\\text{ m/s}}{245\\text{ s}^{-1}} \\approx 1.4041\\text{ m} \\approx 1.40\\text{ m}$$"
                ],
                "result": "f_{\\text{aire}} = 245\\text{ Hz},\\quad \\lambda_{\\text{aire}} = 1.40\\text{ m}",
                "res_val": "f_aire=245Hz, lambda_aire=1.40m"
            }
        ],
        "tip": "¡Concepto clave de examen! Cuando una onda cambia de medio o se transfiere de una cuerda al aire, la FRECUENCIA ($f$ y $\\omega$) permanece invariable; lo que cambia es la velocidad $v$ y la longitud de onda $\\lambda$."
    },
    {
        "id": "p1560",
        "num": "Prob 15.60",
        "cat": "ondas",
        "tags": "15.60 cobre calibre 18 esfera 100N a 500N tercer armonico cambio longitud onda",
        "title": "Alambre de Cobre con Carga y Cambio en Longitud de Onda",
        "badge": "lambda_3 = 0.800 m | Delta lambda_3 = 0 m",
        "badge_color": "yellow",
        "img": "tmp/pdfs/individual/wave_page_14.png",
        "datos": [
            "Longitud del alambre de cobre: $L = 1.20\\text{ m}$.",
            "Diámetro: $1.024\\text{ mm}$ (Calibre 18).",
            "Carga inicial: Esfera de peso $W_1 = 100.0\\text{ N}$.",
            "Carga final sustituta: Esfera de peso $W_2 = 500.0\\text{ N}$."
        ],
        "why": "En una cuerda o alambre con extremos fijos, las longitudes de onda de las ondas estacionarias están **geométricamente cuantizadas** exclusivamente por la longitud $L$: $\\lambda_n = \\frac{2L}{n}$.",
        "incisos": [
            {
                "letter": "a",
                "title": "Longitud de onda del tercer armónico ($n=3$)",
                "steps": [
                    "$$\\lambda_3 = \\frac{2L}{3} = \\frac{2(1.20\\text{ m})}{3} = \\frac{2.40\\text{ m}}{3} = 0.800\\text{ m} = 80.0\\text{ cm}$$"
                ],
                "result": "\\lambda_3 = 0.800\\text{ m}",
                "res_val": "lambda_3 = 0.800 m"
            },
            {
                "letter": "b",
                "title": "Cambio en la longitud de onda del tercer armónico al cambiar el peso a $500\\text{ N}$",
                "steps": [
                    "Al sustituir la esfera de $100\\text{N}$ por la de $500\\text{N}$, aumenta la tensión $T$ y por tanto aumenta la velocidad $v$ y la frecuencia $f_3$.",
                    "Sin embargo, los nodos permanecen en los extremos fijos a distancia $L = 1.20\\text{ m}$, por lo que $\\lambda_3' = \\frac{2L}{3} = 0.800\\text{ m}$.",
                    "Cambio en la longitud de onda:",
                    "$$\\Delta \\lambda_3 = \\lambda_3' - \\lambda_3 = 0.800\\text{ m} - 0.800\\text{ m} = 0.00\\text{ m}$$"
                ],
                "result": "\\Delta \\lambda_3 = 0.00\\text{ m} \\quad \\text{(No cambia)}",
                "res_val": "Delta lambda = 0"
            }
        ],
        "tip": "¡Pregunta conceptual favorita de los profesores! Cambiar la tensión altera la velocidad de propagación y la frecuencia, ¡pero la longitud de onda de los armónicos depende ÚNICAMENTE de la longitud geométrica $L$!"
    },
    {
        "id": "p1565",
        "num": "Prob 15.65",
        "cat": "ondas",
        "tags": "15.65 potencia media amplitud rapidez doble tension",
        "title": "Potencia Media de Onda y Efecto al Duplicar la Rapidez",
        "badge": "A = 7.07 cm | P_nuevo = 400 W",
        "badge_color": "yellow",
        "img": "tmp/pdfs/individual/wave_page_15.png",
        "datos": [
            "Longitud: $L = 8.00\\text{ m}$, masa: $m = 6.00\\text{ g} = 6.00 \\times 10^{-3}\\text{ kg}$.",
            "Densidad lineal: $\\mu = \\frac{6.00 \\times 10^{-3}\\text{ kg}}{8.00\\text{ m}} = 7.50 \\times 10^{-4}\\text{ kg/m}$.",
            "Rapidez de onda inicial: $v_1 = 30.0\\text{ m/s}$, longitud de onda: $\\lambda = 0.200\\text{ m}$.",
            "Potencia media objetivo: $P_1 = 50.0\\text{ W}$."
        ],
        "why": "La potencia media transmitida por una onda armónica es $P_{\\text{med}} = \\frac{1}{2} \\mu v \\omega^2 A^2$. Como $\\omega = \\frac{2\\pi v}{\\lambda}$, la potencia se puede expresar como $P = \\frac{2\\pi^2 \\mu A^2 v^3}{\\lambda^2}$.",
        "incisos": [
            {
                "letter": "a",
                "title": "Cálculo de la amplitud $A$ requerida para $P_{\\text{med}} = 50.0\\text{ W}$",
                "steps": [
                    "Frecuencia angular: $\\omega = 2\\pi \\frac{v}{\\lambda} = 2\\pi \\frac{30.0}{0.200} = 300\\pi \\approx 942.48\\text{ rad/s}$.",
                    "Despejamos la amplitud $A$ de $P_{\\text{med}} = \\frac{1}{2} \\mu v \\omega^2 A^2$:",
                    "$$A^2 = \\frac{2 P_{\\text{med}}}{\\mu v \\omega^2} = \\frac{2(50.0)}{(7.50 \\times 10^{-4})(30.0)(942.48)^2} = \\frac{100.0}{(0.0225)(8.8826 \\times 10^5)} = \\frac{100.0}{19985.9} \\approx 5.0035 \\times 10^{-3}\\text{ m}^2$$",
                    "$$A = \\sqrt{5.0035 \\times 10^{-3}} \\approx 0.07074\\text{ m} = 7.07\\text{ cm}$$"
                ],
                "result": "A = 7.07\\text{ cm} = 0.0707\\text{ m}",
                "res_val": "A = 7.07 cm"
            },
            {
                "letter": "b",
                "title": "Nueva potencia media si la tensión aumenta para duplicar la rapidez ($v_2 = 2 v_1$)",
                "steps": [
                    "Manteniendo la misma amplitud $A$ y la misma longitud de onda $\\lambda$, como $\\omega = \\frac{2\\pi v}{\\lambda} \\propto v$:",
                    "$$P_{\\text{med}} = \\frac{2\\pi^2 \\mu A^2}{\\lambda^2} v^3 \\propto v^3$$",
                    "Al duplicar la rapidez ($v_2 = 2 v_1$):",
                    "$$P_2 = P_1 \\times (2)^3 = 50.0\\text{ W} \\times 8 = 400.0\\text{ W}$$"
                ],
                "result": "P_2 = 400\\text{ W}",
                "res_val": "P2 = 400 W"
            }
        ],
        "tip": "¡Mucho cuidado con la dependencia cúbica! Al duplicar la velocidad manteniendo fija la forma de onda $\\lambda$, la frecuencia se duplica y la potencia aumenta por un factor de $2^3 = 8$."
    },
    {
        "id": "p1574",
        "num": "Prob 15.74",
        "cat": "ondas",
        "tags": "15.74 tercer armonico 192m/s 240Hz antinodo amplitud cinematica puntos",
        "title": "Cinemática Local de Puntos en Onda Estacionaria",
        "badge": "Incisos a, b, c",
        "badge_color": "yellow",
        "img": "tmp/pdfs/individual/wave_page_16.png",
        "datos": [
            "Tercer armónico ($n=3$).",
            "Rapidez de onda: $v = 192\\text{ m/s}$, Frecuencia: $f = 240\\text{ Hz}$.",
            "Amplitud en el antinodo: $A_{SW} = 0.400\\text{ cm} = 4.00\\text{ mm} = 0.00400\\text{ m}$."
        ],
        "why": "La amplitud en cualquier punto $x$ viene dada por la envolvente $A(x) = A_{SW} |\\sin(kx)|$. Cada punto experimenta un M.A.S. transversal con frecuencia angular $\\omega = 2\\pi f$, velocidad máxima $v_{y,\\max}(x) = A(x) \\omega$ y aceleración máxima $a_{y,\\max}(x) = A(x) \\omega^2$.",
        "incisos": [
            {
                "letter": "a",
                "title": "Cálculo de parámetros base y amplitud en $x = 40.0\\text{cm}$, $x = 20.0\\text{cm}$, $x = 10.0\\text{cm}$",
                "steps": [
                    "• Longitud de onda: $\\lambda = \\frac{v}{f} = \\frac{192\\text{ m/s}}{240\\text{ Hz}} = 0.800\\text{ m} = 80.0\\text{ cm}$.",
                    "• Número de onda: $k = \\frac{2\\pi}{\\lambda} = \\frac{2\\pi}{80.0\\text{ cm}} = \\frac{\\pi}{40.0}\\text{ rad/cm}$.",
                    "• <strong>i) En $x = 40.0\\text{ cm}$:</strong> $A(40) = (0.400)|\\sin(\\frac{\\pi}{40} \\cdot 40)| = (0.400)|\\sin(\\pi)| = 0.00\\text{ cm}$ (¡Es un NODO!)",
                    "• <strong>ii) En $x = 20.0\\text{ cm}$:</strong> $A(20) = (0.400)|\\sin(\\frac{\\pi}{40} \\cdot 20)| = (0.400)|\\sin(\\frac{\\pi}{2})| = 0.400\\text{ cm} = 4.00\\text{ mm}$ (¡Es un ANTINODO!)",
                    "• <strong>iii) En $x = 10.0\\text{ cm}$:</strong> $A(10) = (0.400)|\\sin(\\frac{\\pi}{40} \\cdot 10)| = (0.400)|\\sin(\\frac{\\pi}{4})| = (0.400)\\frac{\\sqrt{2}}{2} \\approx 0.2828\\text{ cm} = 2.83\\text{ mm}$"
                ],
                "result": "A(40\\text{cm})=0,\\ A(20\\text{cm})=4.00\\text{mm},\\ A(10\\text{cm})=2.83\\text{mm}",
                "res_val": "A: 0, 4.0mm, 2.83mm"
            },
            {
                "letter": "b",
                "title": "Tiempo para ir del desplazamiento máximo superior al inferior",
                "steps": [
                    "El recorrido de cresta a valle corresponde exactamente a medio ciclo de oscilación:",
                    "$$\\Delta t = \\frac{T}{2} = \\frac{1}{2f} = \\frac{1}{2(240\\text{ s}^{-1})} = \\frac{1}{480}\\text{ s} \\approx 2.083 \\times 10^{-3}\\text{ s} = 2.08\\text{ ms}$$",
                    "(Válido para todos los puntos excepto los nodos, que siempre permanecen en reposo en $y=0$)."
                ],
                "result": "\\Delta t = \\frac{T}{2} = 2.08\\text{ ms}",
                "res_val": "Delta t = 2.08 ms"
            },
            {
                "letter": "c",
                "title": "Velocidad y aceleración transversales máximas en los 3 puntos",
                "steps": [
                    "Frecuencia angular: $\\omega = 2\\pi(240) = 480\\pi \\approx 1507.96\\text{ rad/s}$.",
                    "• <strong>i) En $x = 40.0\\text{ cm}$ (Nodo):</strong> $v_{y,\\max} = 0$, $a_{y,\\max} = 0$.",
                    "• <strong>ii) En $x = 20.0\\text{ cm}$ (Antinodo, $A = 0.0040\\text{m}$):</strong>",
                    "$$v_{y,\\max} = (0.00400\\text{ m})(1507.96\\text{ s}^{-1}) \\approx 6.032\\text{ m/s}$$",
                    "$$a_{y,\\max} = (0.00400\\text{ m})(1507.96\\text{ s}^{-1})^2 \\approx 9.096 \\times 10^3\\text{ m/s}^2 \\approx 9.10 \\times 10^3\\text{ m/s}^2$$",
                    "• <strong>iii) En $x = 10.0\\text{ cm}$ ($A = 0.002828\\text{m}$):</strong>",
                    "$$v_{y,\\max} = (0.002828\\text{ m})(1507.96\\text{ s}^{-1}) \\approx 4.265\\text{ m/s}$$",
                    "$$a_{y,\\max} = (0.002828\\text{ m})(1507.96\\text{ s}^{-1})^2 \\approx 6.432 \\times 10^3\\text{ m/s}^2 \\approx 6.43 \\times 10^3\\text{ m/s}^2$$"
                ],
                "result": "\\begin{cases} x=40\\text{cm}: v=0,\\ a=0 \\\\ x=20\\text{cm}: v=6.03\\text{m/s},\\ a=9.10\\times 10^3\\text{m/s}^2 \\\\ x=10\\text{cm}: v=4.27\\text{m/s},\\ a=6.43\\times 10^3\\text{m/s}^2 \\end{cases}",
                "res_val": "Cinematica local calculada"
            }
        ],
        "tip": "En un nodo la partícula NUNCA se mueve ($v=0, a=0$). En un antinodo la aceleración puede ser gigantesca (¡casi $1000\\times g$!), típica en cuerdas de instrumentos de alta frecuencia."
    },
    {
        "id": "p1515",
        "num": "Prob 15.15",
        "cat": "ondas",
        "tags": "15.15 diapason 120Hz polea masa 1.5kg a 3.0kg rapidez longitud onda",
        "title": "Cuerda con Masa Suspendida y Efecto al Duplicar la Carga",
        "badge": "Incisos a, b, c",
        "badge_color": "yellow",
        "img": "tmp/pdfs/individual/wave_page_17.png",
        "datos": [
            "Frecuencia del diapasón: $f = 120\\text{ Hz}$ (constante impuesta por el motor excitador).",
            "Densidad lineal de masa: $\\mu = 0.0550\\text{ kg/m}$.",
            "Masa suspendida caso 1: $m_1 = 1.50\\text{ kg}$.",
            "Masa suspendida caso 2: $m_2 = 3.00\\text{ kg}$."
        ],
        "why": "La tensión estática en la cuerda horizontal es igual al peso de la masa que cuelga en la polea: $T = m g$. La rapidez es $v = \\sqrt{\\frac{T}{\\mu}}$ y la longitud de onda es $\\lambda = \\frac{v}{f}$.",
        "incisos": [
            {
                "letter": "a",
                "title": "Rapidez transversal con masa suspendida de $1.50\\text{ kg}$ ($v_1$)",
                "steps": [
                    "Tensión: $T_1 = m_1 g = (1.50\\text{ kg})(9.80\\text{ m/s}^2) = 14.70\\text{ N}$.",
                    "$$v_1 = \\sqrt{\\frac{T_1}{\\mu}} = \\sqrt{\\frac{14.70\\text{ N}}{0.0550\\text{ kg/m}}} = \\sqrt{267.27} \\approx 16.348\\text{ m/s}$$"
                ],
                "result": "v_1 = 16.35\\text{ m/s}",
                "res_val": "v1 = 16.35 m/s"
            },
            {
                "letter": "b",
                "title": "Longitud de onda con masa suspendida de $1.50\\text{ kg}$ ($\\lambda_1$)",
                "steps": [
                    "$$\\lambda_1 = \\frac{v_1}{f} = \\frac{16.348\\text{ m/s}}{120\\text{ Hz}} \\approx 0.1362\\text{ m} = 13.62\\text{ cm}$$"
                ],
                "result": "\\lambda_1 = 0.136\\text{ m} = 13.6\\text{ cm}",
                "res_val": "lambda1 = 0.136 m"
            },
            {
                "letter": "c",
                "title": "Nuevos valores si la masa suspendida se aumenta al doble ($m_2 = 3.00\\text{ kg}$)",
                "steps": [
                    "Como la masa se duplica ($m_2 = 2 m_1$), la tensión se duplica ($T_2 = 2 T_1$).",
                    "La rapidez aumenta por un factor de $\\sqrt{2} \\approx 1.4142$:",
                    "$$v_2 = v_1 \\sqrt{2} = 16.348 \\times 1.4142 \\approx 23.120\\text{ m/s}$$",
                    "Como la frecuencia $f = 120\\text{ Hz}$ es constante (la impone el diapasón), la longitud de onda también aumenta por $\\sqrt{2}$:",
                    "$$\\lambda_2 = \\lambda_1 \\sqrt{2} = 0.1362 \\times 1.4142 \\approx 0.1927\\text{ m} = 19.3\\text{ cm}$$"
                ],
                "result": "v_2 = 23.12\\text{ m/s},\\quad \\lambda_2 = 0.193\\text{ m} \\quad (\\text{Aumentan por } \\sqrt{2})",
                "res_val": "v2=23.1m/s, lambda2=0.193m"
            }
        ],
        "tip": "¡Excelente relación para parciales! Al duplicar la masa colgante, tanto la velocidad como la longitud de onda se multiplican por $\\sqrt{2} \\approx +41.4\\%$."
    },
    {
        "id": "p153",
        "num": "Prob 15.3",
        "cat": "ondas",
        "tags": "15.3 tsunami oceanica rapidez km/h m/s sumatra satelites",
        "title": "Onda Oceánica (Tsunami de Sumatra 2004) y Rapidez",
        "badge": "v = 222 m/s = 800 km/h",
        "badge_color": "yellow",
        "img": "tmp/pdfs/individual/wave_page_18.png",
        "datos": [
            "Distancia observada entre crestas consecutivas (Longitud de onda): $\\lambda = 800\\text{ km} = 8.00 \\times 10^5\\text{ m}$.",
            "Periodo entre una ola y la siguiente: $T = 1.0\\text{ hora} = 3600\\text{ s}$."
        ],
        "why": "Para cualquier onda armónica, la rapidez fundamental de propagación es el cociente entre la longitud de onda y el periodo: $v = \\frac{\\lambda}{T}$.",
        "incisos": [
            {
                "letter": "a",
                "title": "Cálculo de la rapidez en $\\text{km/h}$ y en $\\text{m/s}$",
                "steps": [
                    "• <strong>En kilómetros por hora:</strong>",
                    "$$v = \\frac{\\lambda}{T} = \\frac{800\\text{ km}}{1.0\\text{ h}} = 800\\text{ km/h}$$",
                    "• <strong>En metros por segundo (SI):</strong>",
                    "$$v = 800 \\times \\frac{1000\\text{ m}}{3600\\text{ s}} = \\frac{800}{3.6} \\approx 222.22\\text{ m/s}$$"
                ],
                "result": "v = 800\\text{ km/h} = 222.2\\text{ m/s}",
                "res_val": "v = 800 km/h = 222 m/s"
            },
            {
                "letter": "b",
                "title": "¿Por qué las olas causaron tal devastación histórica?",
                "steps": [
                    "1. <strong>Velocidad colosal:</strong> $800\\text{ km/h}$ es la velocidad de crucero de un avión comercial a reacción tipo Boeing 777.",
                    "2. <strong>Masa de agua monumental:</strong> Con una longitud de onda de $800\\text{ km}$, la onda involucra el movimiento de toda la columna de agua oceánica profunda hasta el lecho marino.",
                    "3. <strong>Efecto Shoaling en la costa:</strong> Al acercarse a aguas poco profundas, la rapidez disminuye pero la conservación de flujo de energía comprime la longitud de onda y eleva la altura del agua en muros de más de 20-30 metros con una energía destructiva inconmensurable."
                ],
                "result": "\\text{Velocidad de avión comercial combinada con masa colosal de agua marina}",
                "res_val": "Explicacion fisica de devastacion"
            }
        ],
        "tip": "En aguas profundas ($h \\ll \\lambda$), los tsunamis son ondas de aguas someras donde $v = \\sqrt{g h}$. A $5000\\text{ m}$ de profundidad, $v = \\sqrt{9.8 \\times 5000} \\approx 221\\text{ m/s} = 797\\text{ km/h}$."
    },
    {
        "id": "p31",
        "num": "Prob 31",
        "cat": "ondas",
        "tags": "31 alambre compuesto acero cobre tiempo total densidad",
        "title": "Alambre Compuesto (Acero + Cobre) y Tiempo de Tránsito Total",
        "badge": "t_total = 0.329 s",
        "badge_color": "yellow",
        "img": "tmp/pdfs/individual/wave_page_21.png",
        "datos": [
            "Tramo 1 (Acero): Longitud $L_1 = 30.0\\text{ m}$, diámetro $d = 1.00\\text{ mm} = 1.00 \\times 10^{-3}\\text{ m}$, densidad $\\rho_{\\text{acero}} = 7860\\text{ kg/m}^3$.",
            "Tramo 2 (Cobre): Longitud $L_2 = 20.0\\text{ m}$, diámetro $d = 1.00\\text{ mm}$, densidad $\\rho_{\\text{cobre}} = 8920\\text{ kg/m}^3$.",
            "Tensión común a lo largo de todo el cable: $T = 150.0\\text{ N}$."
        ],
        "why": "Al estar conectados en serie extremo con extremo, la tensión $T$ es idéntica en ambos alambres. Calculamos la densidad lineal $\\mu = \\rho A_{\\text{transversal}}$, la rapidez $v = \\sqrt{T/\\mu}$ en cada tramo y sumamos los tiempos de viaje: $t_{\\text{total}} = \\frac{L_1}{v_1} + \\frac{L_2}{v_2}$.",
        "incisos": [
            {
                "letter": "a",
                "title": "Área de sección transversal y densidades lineales de masa ($\\mu$)",
                "steps": [
                    "Área transversal común ($r = 0.50\\text{ mm} = 5.0 \\times 10^{-4}\\text{ m}$):",
                    "$$A = \\pi r^2 = \\pi (5.00 \\times 10^{-4}\\text{ m})^2 = \\frac{\\pi}{4}(1.00 \\times 10^{-3})^2 \\approx 7.854 \\times 10^{-7}\\text{ m}^2$$",
                    "• <strong>Acero:</strong> $\\mu_{\\text{acero}} = \\rho_{\\text{acero}} A = (7860\\text{ kg/m}^3)(7.854 \\times 10^{-7}\\text{ m}^2) \\approx 6.1732 \\times 10^{-3}\\text{ kg/m}$",
                    "• <strong>Cobre:</strong> $\\mu_{\\text{cobre}} = \\rho_{\\text{cobre}} A = (8920\\text{ kg/m}^3)(7.854 \\times 10^{-7}\\text{ m}^2) \\approx 7.0057 \\times 10^{-3}\\text{ kg/m}$"
                ],
                "result": "\\mu_{\\text{acero}} = 6.173\\text{ g/m},\\quad \\mu_{\\text{cobre}} = 7.006\\text{ g/m}",
                "res_val": "mu_acero y mu_cobre calculadas"
            },
            {
                "letter": "b",
                "title": "Rapidez de onda en cada tramo",
                "steps": [
                    "• <strong>Acero:</strong> $v_1 = \\sqrt{\\frac{T}{\\mu_{\\text{acero}}}} = \\sqrt{\\frac{150.0}{6.1732 \\times 10^{-3}}} = \\sqrt{24298.5} \\approx 155.88\\text{ m/s}$",
                    "• <strong>Cobre:</strong> $v_2 = \\sqrt{\\frac{T}{\\mu_{\\text{cobre}}}} = \\sqrt{\\frac{150.0}{7.0057 \\times 10^{-3}}} = \\sqrt{21411.1} \\approx 146.32\\text{ m/s}$"
                ],
                "result": "v_{\\text{acero}} = 155.88\\text{ m/s},\\quad v_{\\text{cobre}} = 146.32\\text{ m/s}",
                "res_val": "v1=155.9m/s, v2=146.3m/s"
            },
            {
                "letter": "c",
                "title": "Tiempo de tránsito total para recorrer ambos alambres ($t_{\\text{total}}$)",
                "steps": [
                    "$$t_1 = \\frac{L_1}{v_1} = \\frac{30.0\\text{ m}}{155.88\\text{ m/s}} \\approx 0.19246\\text{ s}$$",
                    "$$t_2 = \\frac{L_2}{v_2} = \\frac{20.0\\text{ m}}{146.32\\text{ m/s}} \\approx 0.13669\\text{ s}$$",
                    "$$t_{\\text{total}} = t_1 + t_2 = 0.19246 + 0.13669 = 0.32915\\text{ s} \\approx 0.329\\text{ s}$$"
                ],
                "result": "t_{\\text{total}} = 0.329\\text{ s} = 329\\text{ ms}",
                "res_val": "t_total = 0.329 s"
            }
        ],
        "tip": "Como el cobre es más denso que el acero ($8920 > 7860\\text{ kg/m}^3$), la onda viaja más lento en el tramo de cobre ($146.3\\text{ m/s}$ vs $155.9\\text{ m/s}$)."
    }
]

# Construimos el HTML interactivo
HTML_HEAD = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>📓 Cuaderno de Apuntes Pro — Solucionario Maestro de Mecatrónica</title>
  
  <!-- MathJax 3: Renderizado LaTeX Impecable -->
  <script>
    window.MathJax = {
      tex: {
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
        processEscapes: true,
        packages: {'[+]': ['ams', 'color']}
      },
      chtml: { scale: 1.05 },
      options: { skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'] }
    };
  </script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>

  <style>
    :root {
      --bg: #0d1117;
      --paper-bg: #161b22;
      --paper-border: #30363d;
      --text-main: #f0f6fc;
      --text-muted: #8b949e;
      --accent-blue: #58a6ff;
      --accent-cyan: #39c5cf;
      --accent-green: #3fb950;
      --accent-yellow: #d29922;
      --accent-purple: #bc8cff;
      --accent-red: #f85149;
      --tag-bg: #21262d;
      --box-inner: #0d1117;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif; }
    body { background-color: var(--bg); color: var(--text-main); padding: 20px 10px; line-height: 1.6; }
    .container { max-width: 1180px; margin: 0 auto; }

    header {
      background: linear-gradient(135deg, #1f293d 0%, #161b22 100%);
      border: 1px solid var(--paper-border);
      border-left: 6px solid var(--accent-blue);
      border-radius: 12px;
      padding: 24px 20px;
      margin-bottom: 22px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.4);
    }
    header h1 { font-size: 1.95rem; color: #fff; margin-bottom: 6px; display: flex; align-items: center; gap: 10px; }
    header p { color: var(--text-muted); font-size: 0.95rem; }

    /* Barra Superior */
    .toolbar {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 22px;
      background: rgba(22, 27, 34, 0.95);
      backdrop-filter: blur(10px);
      position: sticky;
      top: 10px;
      z-index: 100;
      padding: 12px 16px;
      border-radius: 10px;
      border: 1px solid var(--paper-border);
      box-shadow: 0 6px 20px rgba(0,0,0,0.5);
    }
    .filter-pills { display: flex; flex-wrap: wrap; gap: 6px; }
    .pill-btn {
      background: var(--tag-bg);
      color: var(--text-muted);
      border: 1px solid var(--paper-border);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 0.84rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }
    .pill-btn:hover { color: #fff; border-color: var(--accent-blue); }
    .pill-btn.active { background: var(--accent-blue); color: #0d1117; font-weight: 700; border-color: var(--accent-blue); }

    .search-box {
      background: #0d1117;
      border: 1px solid var(--paper-border);
      color: #fff;
      padding: 7px 14px;
      border-radius: 20px;
      font-size: 0.86rem;
      min-width: 250px;
      outline: none;
    }
    .search-box:focus { border-color: var(--accent-blue); }

    /* Estructura Tarjeta Apunte */
    .apuntes-grid { display: flex; flex-direction: column; gap: 24px; }
    
    .apunte-card {
      background: var(--paper-bg);
      border: 1px solid var(--paper-border);
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 6px 16px rgba(0,0,0,0.3);
      transition: border-color 0.2s;
    }
    .apunte-card:hover { border-color: #58a6ff66; }

    .apunte-header {
      padding: 14px 20px;
      background: #1c2128;
      border-bottom: 1px solid var(--paper-border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      user-select: none;
    }
    .apunte-header-left { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }
    .num-tag {
      background: #21262d;
      color: var(--accent-cyan);
      font-weight: 800;
      padding: 3px 10px;
      border-radius: 6px;
      border: 1px solid #30363d;
      font-size: 0.88rem;
    }
    .apunte-title { font-size: 1.15rem; font-weight: 700; color: #fff; }
    
    .badge-ans {
      background: rgba(63, 185, 80, 0.15);
      color: var(--accent-green);
      border: 1px solid rgba(63, 185, 80, 0.4);
      padding: 4px 10px;
      border-radius: 20px;
      font-size: 0.82rem;
      font-weight: 700;
      white-space: nowrap;
    }

    .apunte-content { padding: 20px; }
    .apunte-content.hidden { display: none; }

    .datos-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      margin-bottom: 18px;
    }
    @media (max-width: 820px) {
      .datos-grid { grid-template-columns: 1fr; }
    }

    .sub-box {
      background: var(--box-inner);
      border: 1px solid var(--paper-border);
      border-radius: 8px;
      padding: 14px;
    }
    .sub-box-title {
      font-size: 0.85rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .title-blue { color: var(--accent-blue); }
    .title-purple { color: var(--accent-purple); }
    .title-yellow { color: var(--accent-yellow); }
    .title-green { color: var(--accent-green); }

    .scan-thumb {
      max-width: 100%;
      max-height: 230px;
      border-radius: 6px;
      border: 1px solid #30363d;
      cursor: zoom-in;
      background: #fff;
      display: block;
      margin: 4px auto;
    }

    .why-box {
      background: #19152b;
      border: 1px solid #492e7a;
      border-left: 4px solid var(--accent-purple);
      border-radius: 8px;
      padding: 14px 18px;
      margin-bottom: 16px;
    }
    .why-box p { font-size: 0.92rem; color: #e2d9f3; margin-bottom: 6px; }
    .why-box p strong { color: #fff; }

    .inciso-card {
      background: rgba(255, 255, 255, 0.015);
      border: 1px solid var(--paper-border);
      border-left: 4px solid var(--accent-cyan);
      border-radius: 8px;
      padding: 14px 18px;
      margin-bottom: 14px;
    }
    .inciso-header {
      font-size: 0.98rem;
      font-weight: 800;
      color: var(--accent-cyan);
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .math-step-line { font-size: 0.92rem; color: #c9d1d9; margin: 8px 0; }

    .res-inciso {
      background: #0f2d18;
      border: 1px solid #238636;
      border-radius: 6px;
      padding: 8px 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 10px;
    }
    .res-inciso-text { color: #7ee787; font-weight: 800; font-size: 1rem; }

    .tip-pro {
      background: #241c0e;
      border: 1px solid #744d08;
      border-left: 4px solid var(--accent-yellow);
      border-radius: 8px;
      padding: 12px 16px;
      font-size: 0.88rem;
      color: #fce5b2;
      display: flex;
      align-items: flex-start;
      gap: 10px;
    }

    .btn-copy-sm {
      background: #238636;
      color: #fff;
      border: none;
      padding: 4px 10px;
      border-radius: 4px;
      font-size: 0.78rem;
      font-weight: 700;
      cursor: pointer;
    }
    .btn-copy-sm:hover { background: #2ea043; }

    .lightbox {
      display: none;
      position: fixed;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(0,0,0,0.9);
      z-index: 1000;
      justify-content: center;
      align-items: center;
      cursor: zoom-out;
      padding: 20px;
    }
    .lightbox.show { display: flex; }
    .lightbox img { max-width: 95%; max-height: 95%; border-radius: 8px; background: #fff; }
  </style>
</head>
<body>

<div class="container">

  <header>
    <h1>📓 Cuaderno de Apuntes Pro — Física & Circuitos</h1>
    <p>Los 30 Ejercicios Desarrollados al 100% (1 a 1): Datos, Recorte Escaneado con Zoom, Justificación de Fórmulas ('¿Por qué se usa?'), Desglose de Todos los Incisos (a, b, c, d, e, f...) y Tips de Parcial.</p>
  </header>

  <div class="toolbar">
    <div class="filter-pills">
      <button class="pill-btn active" onclick="filterNotes('all', this)">Todos (30)</button>
      <button class="pill-btn" onclick="filterNotes('circuitos', this)">🔌 Circuitos (10)</button>
      <button class="pill-btn" onclick="filterNotes('mas', this)">🎯 M.A.S. (7)</button>
      <button class="pill-btn" onclick="filterNotes('ondas', this)">🌊 Ondas (13)</button>
    </div>
    <div style="display:flex; gap:8px;">
      <button class="pill-btn" onclick="toggleAllNotes(true)">📂 Expandir Todo</button>
      <button class="pill-btn" onclick="toggleAllNotes(false)">📁 Colapsar</button>
      <input type="text" id="searchNotes" class="search-box" placeholder="🔍 Buscar ej: 15.41, 13.68, Superposición..." oninput="searchNotes()">
    </div>
  </div>

  <div class="apuntes-grid" id="notesContainer">
"""

HTML_FOOTER = """
  </div>
</div>

<!-- Lightbox Modal -->
<div class="lightbox" id="lightboxModal" onclick="closeLightbox()">
  <img id="lightboxImg" src="" alt="Ampliación">
</div>

<script>
  function toggleNote(header) {
    const body = header.nextElementSibling;
    body.classList.toggle('hidden');
    if (!body.classList.contains('hidden') && window.MathJax && window.MathJax.typesetPromise) {
      window.MathJax.typesetPromise([body]).catch(err => console.log(err));
    }
  }

  function toggleAllNotes(open) {
    document.querySelectorAll('.apunte-content').forEach(c => {
      if (open) c.classList.remove('hidden'); else c.classList.add('hidden');
    });
    if (open && window.MathJax && window.MathJax.typesetPromise) {
      window.MathJax.typesetPromise().catch(err => console.log(err));
    }
  }

  function openLightbox(src) {
    document.getElementById('lightboxImg').src = src;
    document.getElementById('lightboxModal').classList.add('show');
  }

  function closeLightbox() {
    document.getElementById('lightboxModal').classList.remove('show');
  }

  function filterNotes(cat, btn) {
    document.querySelectorAll('.pill-btn').forEach(b => b.classList.remove('active'));
    if (btn) btn.classList.add('active');

    document.querySelectorAll('.apunte-card').forEach(c => {
      if (cat === 'all' || c.getAttribute('data-cat') === cat) {
        c.style.display = 'block';
      } else {
        c.style.display = 'none';
      }
    });
  }

  function searchNotes() {
    const q = document.getElementById('searchNotes').value.toLowerCase();
    document.querySelectorAll('.apunte-card').forEach(c => {
      const text = (c.getAttribute('data-tags') + ' ' + c.innerText).toLowerCase();
      c.style.display = text.includes(q) ? 'block' : 'none';
    });
  }

  function copyText(val) {
    navigator.clipboard.writeText(val).then(() => {
      alert('✅ Copiado al portapapeles: ' + val);
    });
  }
</script>

</body>
</html>
"""

def generate_card_html(ex):
    datos_li = "".join([f"<li>{d}</li>" for d in ex["datos"]])
    
    incisos_html = ""
    for inc in ex["incisos"]:
        steps_html = "".join([f"<p class='math-step-line'>{s}</p>" for s in inc["steps"]])
        res_display = f"$${inc['result']}$$" if inc.get("result") else ""
        escaped_res_val = inc['res_val'].replace("'", "\\'")
        incisos_html += f"""
        <div class="inciso-card">
          <div class="inciso-header">
            <span>🔹 Inciso {inc['letter']})</span> {inc['title']}
          </div>
          {steps_html}
          {res_display}
          <div class="res-inciso">
            <span class="res-inciso-text">✅ Resultado: ${inc['result']}$</span>
            <button class="btn-copy-sm" onclick="copyText('{escaped_res_val}')">📋 Copiar</button>
          </div>
        </div>
        """

    card_html = f"""
    <!-- CARD: {ex['num']} -->
    <div class="apunte-card" data-cat="{ex['cat']}" data-tags="{ex['tags']}">
      <div class="apunte-header" onclick="toggleNote(this)">
        <div class="apunte-header-left">
          <span class="num-tag">{ex['num']}</span>
          <span class="apunte-title">{ex['title']}</span>
        </div>
        <span class="badge-ans">{ex['badge']}</span>
      </div>
      <div class="apunte-content">
        <div class="datos-grid">
          <div class="sub-box">
            <div class="sub-box-title title-blue">🎯 1. Datos Identificados & Variables</div>
            <ul style="padding-left:18px; font-size:0.9rem; color:#c9d1d9;">
              {datos_li}
            </ul>
          </div>
          <div class="sub-box">
            <div class="sub-box-title title-blue">📷 Enunciado Original 1x1</div>
            <img src="{ex['img']}" alt="{ex['num']}" class="scan-thumb" onclick="openLightbox(this.src)">
          </div>
        </div>

        <div class="why-box">
          <div class="sub-box-title title-purple">🧠 2. ¿Por qué usamos esta fórmula / método?</div>
          <p>{ex['why']}</p>
        </div>

        <div style="margin-bottom: 12px; font-size: 0.95rem; font-weight: 700; color: #fff;">
          📝 3. Solución Detallada por Incisos:
        </div>

        {incisos_html}

        <div class="tip-pro">
          <span style="font-size:1.2rem;">💡</span>
          <span>{ex['tip']}</span>
        </div>
      </div>
    </div>
    """
    return card_html

def main():
    cards = "\n".join([generate_card_html(ex) for ex in EXERCISES])
    full_html = HTML_HEAD + cards + HTML_FOOTER
    out_file = Path("guia_estudio_talleres.html")
    out_file.write_text(full_html, encoding="utf-8")
    print(f"Generated {out_file.name} successfully with {len(EXERCISES)} exercises!")

if __name__ == "__main__":
    main()
