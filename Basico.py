{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNCdWEVjVgKxcT+FumKbEQw"
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
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PbyVVZdVE54b",
        "outputId": "3fc8eb78-fe6c-416b-e165-361731b0b44f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite seu nome:kkkk\n",
            "kkkk\n",
            "<class 'str'>\n",
            "7\n",
            "<class 'int'>\n"
          ]
        }
      ],
      "source": [
        "a = input(\"Digite seu nome:\")\n",
        "print(a)\n",
        "print(type(a))\n",
        "\n",
        "b = int(7)\n",
        "print(b)\n",
        "print(type(b))"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = int (input(\"Digite o primeiro valor: \"))\n",
        "b = int (input(\"Digite o segundo valor: \"))\n",
        "c = int (input(\"Digite o terceiro valor: \"))\n",
        "\n",
        "print(a+b+c)\n",
        "print(a-b-c)\n",
        "print(a*b*c)\n",
        "print(a/b/c)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "10eod2WaOzBK",
        "outputId": "b3da4feb-b78f-4470-e3d8-d758dd68a04f"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o primeiro valor: 1\n",
            "Digite o segundo valor: 1\n",
            "Digite o terceiro valor: 1\n",
            "3\n",
            "-1\n",
            "1\n",
            "1.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "p1 = float (input(\"Digite a primeira nota: \"))\n",
        "p2 = float (input(\"Digite a segunda nota: \"))\n",
        "p3 = float (input(\"Digite a terceira nota: \"))\n",
        "\n",
        "print((p1+p2+p3) / 3 )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LNGHzJvUSwNU",
        "outputId": "3a05601f-d040-4f6a-e477-1c4f7d1913ee"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a primeira nota: 4\n",
            "Digite a segunda nota: 5\n",
            "Digite a terceira nota: 6\n",
            "5.0\n"
          ]
        }
      ]
    }
  ]
}
