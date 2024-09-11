{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNrDtLIvXfrRD9ONTjQF7P/"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eM9Fi1RrLt5u",
        "outputId": "22fe7712-216c-4dd7-ee41-d2d93f03214f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite sua Média:5\n",
            "Reprovado! \n",
            " Média informada: 5.0\n"
          ]
        }
      ],
      "source": [
        "media = float(input(\"Digite sua Média:\"))\n",
        "\n",
        "if media > 5:\n",
        "  print(\"Aprovado!\", \"\\n Média informada:\", media)\n",
        "elif media < 3:\n",
        "  print(\"Reprovado!\", \"\\n Média informada:\", media)\n",
        "else:\n",
        "  print(\"Recuperação!\", \"\\n Média informada:\", media)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "time1 = float(input(\"Digite a quantidade de gols do time 1:\"))\n",
        "time2 = float(input(\"Digite a quantidade de gols do time 2:\"))\n",
        "\n",
        "if time1 > time2:\n",
        "  print(\"O vencedor é o time 1!\")\n",
        "elif time1 < time2:\n",
        "  print(\"O vencedor é o time 2!\")\n",
        "else:\n",
        "  print(\"O jogo deu empate!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VW4PckgTVJ_6",
        "outputId": "385b1ae5-f23b-4946-94bc-d1404ae7a246"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a quantidade de gols do time 1:2\n",
            "Digite a quantidade de gols do time 2:2\n",
            "O jogo deu empate\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "compra = float(input(\"Digite o valor da compra:\"))\n",
        "numParcelas = float(input(\"Digite o número de parcelas:\"))\n",
        "\n",
        "resultado = float(compra) / float(numParcelas)\n",
        "\n",
        "print(\"O valor de\", compra, \"em\", numParcelas, \"parcelas, será de:\", resultado)"
      ],
      "metadata": {
        "id": "2fG9nJ8XWI3J"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "qi0-pMOQYAhi"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}