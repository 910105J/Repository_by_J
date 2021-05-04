{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Day_210502_Chapter02.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMmspWc0Zh0fhoRG9washcG",
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
        "<a href=\"https://colab.research.google.com/github/910105J/Repository_by_J/blob/Deeplearning/Day_210502_Chapter02.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CQ-QHX9YD9w2",
        "outputId": "bbcd0ab6-e0ea-4b90-bb49-8cb94179fc90"
      },
      "source": [
        "import numpy as np # 별칭 np\n",
        "print(np.__version__) # ver.1.19.5"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "1.19.5\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4Qoe_KFVGF76",
        "outputId": "2d30fcb8-d320-4399-e7be-b39eaee6cd5f"
      },
      "source": [
        "my_arr = np.array([[10, 20, 30], [40, 50, 60]])\n",
        "print(my_arr) # Python 의 2차원배열과 같이 출력된다"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[10 20 30]\n",
            " [40 50 60]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iyHUyav6GmYz",
        "outputId": "a89ed9a4-77a5-4889-d220-8fb3f5ad9869"
      },
      "source": [
        "type(my_arr) # 노트북 코드 셀의 마지막 줄은 print() 함수를 사용하지 않아도 자동으로 결과가 출력된다"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "numpy.ndarray"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BpsTP5SGGm7c",
        "outputId": "5288ccfb-17b3-42fc-ac72-62cf8677069d"
      },
      "source": [
        "my_arr[0][2] # 1번째 행, 3번째 요소 선택"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "30"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ATVX2sgmHOoV",
        "outputId": "b027b4c8-6298-4082-842d-8efdd2e31741"
      },
      "source": [
        "np.sum(my_arr) # np 내장 함수 중 배열의 모든 요소를 더해주는 함수 sum()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "210"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iYy2w3o7HSod"
      },
      "source": [
        "import matplotlib.pyplot as plt # 별칭 plt. 맷플롯립에 대한 설명 > https://matplotlib.org"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 265
        },
        "id": "q1tOT4LeH4Of",
        "outputId": "48de65e2-e343-41b4-8352-5c3ad1c5fc96"
      },
      "source": [
        "plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25]) # x축, y축의 값을 파이썬 리스트로 전달한다. plot > 선 그래프\n",
        "plt.show() # plt 내장 함수 중 화면에 그래프로 출력하는 함수 show()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 265
        },
        "id": "TUnoYin7IXHD",
        "outputId": "e86bbd71-76a9-450b-dc07-e081d3f1a0f7"
      },
      "source": [
        "plt.scatter([1, 2, 3, 4, 5], [1, 4, 9, 16, 25]) # x축, y축의 값을 파이썬 리스트로 전달한다. scatter > 산점도 (점그래프)\n",
        "plt.show() # show 함수를 사용하지 않아도 되지만 사용하면 더 깔끔하고 보기 좋은 그래프가 그려진다"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 269
        },
        "id": "IUTdqFEPI2QU",
        "outputId": "e895f4e1-f595-487a-b17b-59fcee01dd2c"
      },
      "source": [
        "x = np.random.randn(1000) # 표준 정규 분포를 따르는 난수 1,000개를 만듭니다.\n",
        "y = np.random.randn(1000) # 표준 정규 분포를 따르는 난수 1,000개를 만듭니다.\n",
        "plt.scatter(x, y)\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    }
  ]
}