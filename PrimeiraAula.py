{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOuidT9jImyRqURtkqqq60X",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Giovanna994/ds-III-giovanna-soares/blob/main/PrimeiraAula.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qIMNmLVbIBe5",
        "outputId": "4524753d-7dbe-4cf8-97f4-ce21be7284c7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello Word\n",
            "Meu Nome é Giovanna\n",
            "Isso é um teste...\n"
          ]
        }
      ],
      "source": [
        "print('Hello Word')\n",
        "print('Meu Nome é Giovanna')\n",
        "print('Isso é um teste...')"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Teste de Soma, o jogo da velha é o simbolos para fazer comentarios no código\n",
        "\n",
        "num1 = 6\n",
        "num2 = 9\n",
        "\n",
        "soma = num1 + num2\n",
        "\n",
        "print('A soma dos números {0} e {1}, é {2}' . format (num1, num2, soma))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Gx-afTwwJ4k1",
        "outputId": "880c7e06-2ac7-463d-d6a8-1fb34b9f0046"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "A soma dos números 6 e 9, é 15\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Teste com Input e com subtração\n",
        "\n",
        "num1 = input('Digite o primeiro valor:')\n",
        "num2 = input('Digite o segundo valor: ')\n",
        "\n",
        "subt = float(num1) - float(num2)\n",
        "\n",
        "print('O resultado da subtração, com os números {0} e {1} é {2}' . format (num1, num2, subt))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xy7IN3dxLvHB",
        "outputId": "fc51a0b9-e4e6-406d-ce6a-0417e7e1ac45"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o primeiro valor:1\n",
            "Digite o segundo valor: 1\n",
            "O resultado da subtração, com os números 1 e 1 é 0.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Exercicio da Árvore de Natal apenas utilizando print\n",
        "\n",
        "print('     *')\n",
        "print('    ***')\n",
        "print('   *****')\n",
        "print('  *******')\n",
        "print(' *********')\n",
        "print('     *')\n",
        ""
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yy6CvS4INyWc",
        "outputId": "766888be-038a-4296-f160-5907bc742fd4"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "     *\n",
            "    ***\n",
            "   *****\n",
            "  *******\n",
            " *********\n",
            "     *\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Multipliacação\n",
        "\n",
        "num1 = 2\n",
        "num2 = 3\n",
        "\n",
        "print(num1 * num2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8zb79czFTlXC",
        "outputId": "b40ade2d-f91c-4dea-d817-0bfb823d5d36"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "6\n"
          ]
        }
      ]
    }
  ]
}