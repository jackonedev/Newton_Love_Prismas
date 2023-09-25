# Newton Loves Prismas

## Descripción

El siguiente proyecto trata de procesar un fichero de texto plano (.txt) para generar un corpus de texto que pueda ser utilizado para entrenar un modelo de NLP (Natural Language Processing). El fichero de texto utilizado es la historia de Sherlock Holmes.

## Objetivo

Implementar un transformer ya entrenado para traducir el texto. Implementar un algoritmo que consuma recursos de la GPU y utilice threading para optimizar el tiempo de procesamiento y los recursos computacionales.

## Modelo utilizado

https://huggingface.co/Helsinki-NLP/opus-mt-en-es

## Ejemplo de procesamiento de texto:

```
FRAGMENTO 1: ES UNA LINEA COMPLETAMENTE EN MAYUSCULAS

Este es el contenido del fragmento 1. No
importa si existen saltos de linea
provocados. El programa se enfoca en
separar los párrafos en funcion del doble
salto de linea.

Por lo tanto estamos dentro del segundo
párrafo del fragmento 1. Cáda párrafo
corresponde a un elemento dentro de un
pandas.DataFrame.

FRAGMENTO 2: ES OTRA LINEA COMPLETAMENTE EN MAYUSCULAS

Este segundo fragmenta se almacenará de
forma independiente al resto de los
fragmentos. Por lo tanto, cada fragmento
se almacenara en un fichero .txt diferente.

FRAGMENTO 3: ES OTRA LINEA COMPLETAMENTE EN MAYUSCULAS


Este fragmento tiene un triple salto de linea
que será corregidoc.

Este es la segunda linea del fragmento 3.
Por lo tanto es otra fila del DataFrame corpus
en la columna llamada fragment_03.
```

En este ejemplo, dentro de la carpeta /output se guardarán de forma ordenada los siguientes ficheros:

```
data/output/{fecha}/{#}/fragment_01.txt
data/output/{fecha}/{#}/fragment_02.txt
data/output/{fecha}/{#}/fragment_03.txt
data/output/{fecha}/{#}/corpus_01.pkl
data/output/{fecha}/{#}/corpus_02.pkl
data/output/{fecha}/{#}/corpus_03.pkl
data/output/{fecha}/{#}/corpus_df.pkl
```

En donde {fecha} corresponde a la fecha de ejecución del programa y {#} corresponde a un número que se incrementa para independizar los ficheros de salida de cada ejecución.

Cada fichero .pkl corresponde a un pandas.DataFrame con el procesamiento de cada fragmento. El fichero corpus_df.pkl corresponde a la concatenación de todos los fragmentos.

## Advertencia

El programa aún no está optimizado, y tal cual está diseñado ahora va a tardar varios días en procesar todo el texto.
Se está trabajando en la optimización y control de flujo para que la ejecución pueda ser asistida por humanos.
