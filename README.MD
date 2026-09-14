Datos Utiliza el dataset:
Cafe Sales – Dirty Data for Cleaning Training

Actividad
Realiza una práctica donde:
  Cargues e inspecciones la base.
  Identifiques los principales problemas de calidad.
  Apliques técnicas de limpieza y transformación.
  Justifiques las decisiones tomadas.
  Exportes una versión limpia de la base.


Tabla resumen:
Problema encontrado  |  Registros afectados  |  Acción realizada  |  Justificación

Muchas filas con datos UNKNOWN o  ERROR | No medido | Eliminacion de filas con 2 o mas datos invalidos | Un alto contenido de datos invalidos compromete la credibilidad de la informacion

Tipo de dato string en valores Quantity, Price per unit, Total spent, Transaction date |  No medido| Se conviertieron Quantity a int, price y total a float, y Date a datetime | Para trabajar correctamente con las cifras.

Muchos datos vacios, o con inconsistencias | No medido | Las columnas numericas se llenaron con la media y las categoricas fueron eliminadas | Los datos no se pueden dejar vacios porque conllevan a inconsistencia en el analisis entre columnas.






Descripción del procedimiento;
Para realizar la limpieza de los datos porporcionados se siguio una metodologia de 13 pasos:

1. Se importaron las librerias para manejar los archivos y operciones necesarias (pandas, numpy y matplotlib.pyplot)

2. Se cargo el dataframe a la memoria con ayuda de pandas, para trabajar con el

3. Se hizo una verificacion de las columnas, para ver si existia alguna duplicada y que fuera inecesaria, sin embargo en este caso solo habia 8, y todas no funcionaban, por lo que no hubo cambios

4. Se eliminaron filas duplicadas, con .drop_duplicates

5 y 6. Se eliminaron las filas inservibles. Aqui mi criterio fue, que si la fila tenia menos del 80% de los datos ó si 2 o mas campos contenien un error o un dato desconocido, se eliminaria la fila para mantener la credibilidad de los datos

7. Estandarizar las categorias de cada columna. En el dataset, afortunadamente ya estaban estandarizadas las categorias correctamente, solo exixtian datos UNKNOWN y ERROR en varias columnas, pero estas se limpiarian mas tarde.

8. Verificar errores en datos numericos: las categorias  Quantity, Price per unit, Total spent, Transaction date , se encontraban con tipo de dato string, y estas fueron cambiadas a int, float y datetime con ayuda de pandas, para trabajar correctamente con las cantidades

9. Tratamiento de datos vacios: Para este paso opte por rellenar todos los datos vacios de mis columnas numerias con la media. y para las columnas categoricas, las filas fueron eliminadas.
  ##En este paso dude mucho si fue correcto la eliminacion de las filas con datos categoricos faltantes, ya que disminuyó bastante la cantidad dee datos

10. Verificar que no existan valores nulos: Implimir con print(df.isnull().sum()), en este caso ya se habia corregido, por lo que no hubo cambios

11. Remover duplicados: De nuevo se utilizo drop duplicates como segunod filtro

12.  Retirar o corregir valores atipicos: Se utilizo el metodo IQR (rango intercuartilico) en las  columnas numericas para identificarlos y eliminarlos

13. Exportar los datos: Antes de exportarlos se realizó una verificacion final para imprimir un resumen de el resultado de nuestros datos, mostrando la cantidad de valores UNKNOWN Y ERROR, La informacion final del dataframe y sus dimensiones, asi como, sus primeras filas (head). Yfinalmente se exportaron los datos a un CSV.
