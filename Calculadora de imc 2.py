{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4aa3a242-ba48-4f62-94bf-ea1db79b334d",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Nombre: juan\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'juan'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#pedir datos al usuario\n",
    "input('Nombre:')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3c153c73-f315-4f86-8dc8-e83d8258603c",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Nombre juan\n"
     ]
    }
   ],
   "source": [
    "nombre = input('Nombre')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "47a36fcd-82cb-4113-816a-9f7dea08df52",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Apellido Paterno: perez\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'perez'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "input('Apellido Paterno:')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "392818b7-818e-4ea9-9e19-2f03b5ba1fa2",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Apellido Paterno: perez\n"
     ]
    }
   ],
   "source": [
    "apellidopaterno = input('Apellido Paterno:')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6e417d09-0a21-4b2f-8a18-42dd74099fb8",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'perez'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "apellidopaterno"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "8ac34c07-af59-4776-bdaa-16d9762ced92",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Apellido Materno: ramires\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'ramires'"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "input('Apellido Materno:')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "cf020184-d599-46a1-b324-0d1407290433",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Apellido Materno ramires\n"
     ]
    }
   ],
   "source": [
    "apellidomaterno = input('Apellido Materno')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "1259d1db-3bea-405d-b3a3-25d407d530fa",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'ramires'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "apellidomaterno"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "1511c015-e7c8-4339-a1f9-1cf35a1f890f",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Edad: 28\n"
     ]
    }
   ],
   "source": [
    "cond = False\n",
    "while cond == False:\n",
    "    try:\n",
    "        edad = input('Edad:')\n",
    "        if edad is not None:\n",
    "            edad = float(edad)\n",
    "            if edad < 1:\n",
    "                print('Ingresa Un Numero Valido')\n",
    "            else:\n",
    "                cond = True\n",
    "        else:\n",
    "            print('Ingresa Un Numero Valido')\n",
    "    except ValueError:\n",
    "        print('Ingresa Un Numero Valido')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "87d35cc2-7f59-4614-b05d-0242dacff86e",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Peso En Kg: 74\n"
     ]
    }
   ],
   "source": [
    "cond = False\n",
    "while cond == False:\n",
    "    try:\n",
    "        peso = input('Peso En Kg:')\n",
    "        if peso is not None:\n",
    "            peso = float(peso)\n",
    "            if peso <1:\n",
    "                print('Ingresa un Numero Valido')\n",
    "            else:\n",
    "                cond = True\n",
    "        else:\n",
    "            print('Ingresa Un Numero Valido')\n",
    "    except ValueError:\n",
    "        print('Ingresa Un Numero Valido')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "970dbfe8-9926-490f-a95b-90a83ad9fc8c",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Estatura En metros: 1.80\n"
     ]
    }
   ],
   "source": [
    "cond = False\n",
    "while cond == False:\n",
    "    try:\n",
    "        estatura = input('Estatura En metros:')\n",
    "        if estatura is not None:\n",
    "            estatura = float(estatura)\n",
    "            if estatura <1:\n",
    "                print('Ingresa Un Numero Valido')\n",
    "            else:\n",
    "                cond = True\n",
    "        else:\n",
    "            print('Ingresa Un Numero Valido')\n",
    "    except ValueError:\n",
    "        print('Ingresa Un Numero Valido')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "9be3aab7-8c5b-4b0c-8202-715f6a8fec96",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "nombre='juan'\n",
    "apellidopaterno='perez'\n",
    "apellidomaterno='ramires'\n",
    "edad=28\n",
    "peso=74\n",
    "estatura=1.80\n",
    "\n",
    "imc = peso / estatura**2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "3a214b5f-7280-4474-96f7-ae336be204f5",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hola juan perez ramires tu IMS es 22.839506172839506\n"
     ]
    }
   ],
   "source": [
    "print(f'Hola {nombre} {apellidopaterno} {apellidomaterno} tu IMS es {imc}')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
