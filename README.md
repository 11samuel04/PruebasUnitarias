# Tarea: Pruebas Unitarias con pytest y Análisis de Cobertura con coverage
Este proyecto demuestra cómo realizar pruebas unitarias utilizando pytest y cómo analizar la cobertura del código utilizando coverage. Se proporcionan dos archivos principales:

## Archivo main.py
Contiene tres funciones simples para ser probadas:

### Funciones en main.py
#### sum(x, y):

- ***Descripción***: Esta función suma dos números.
- ***Implementación***:

```python
def sum(x, y):
    return x + y

```
#### es_mayor_que(numero_1, numero_2):

- ***Descripción***: Esta función verifica si numero_1 es mayor que numero_2.
- ***Implementación:***
```python
def es_mayor_que(numero_1, numero_2):
    return numero_1 > numero_2
```

#### login(usuario, contrasena)
- ***Descripción***: Esta función verifica si el usuario y la contraseña proporcionados coinciden con un par específico.
- ***Implementación***:
```python
Copiar código
def login(usuario, contrasena):
    if (usuario == "Metodologia" and contrasena == "710011C"):
        return True
    else:
        return False
```
## Archivo test_main.py
Contiene pruebas unitarias para las funciones definidas en main.py utilizando pytest:

### Pruebas en test_main.py
#### test_sum():

- ***Descripción***: Prueba la función sum(x, y) para verificar si suma correctamente dos números.
- ***Implementación:***
```python
def test_sum():
    assert sum(2, 5) == 7
```
#### test_sum2():
- ***Descripción***: Otra prueba de la función sum(x, y) para verificar su funcionalidad con otros valores.
- ***Implementación***:
```python
def test_sum2():
    assert sum(4, 6) == 10
```
#### test_login_pass()
- ***Descripción:*** Prueba la función es_mayor_que(numero_1, numero_2) para asegurarse de que devuelve correctamente si numero_1 es mayor que numero_2.
- ***Implementación:***
```python
def test_es_mayor_que():
    assert es_mayor_que(10, 2)
```
#### test_login_pass():

- ***Descripción:*** Prueba la función login(usuario, contrasena) para asegurarse de que permite el acceso con credenciales válidas.
- ***Implementación:***
```python
def test_login_pass():
    login_passes = login("Metodologia", "710011C")
    assert login_passes
```
#### test_login_fail():

- ***Descripción:*** Prueba la función login(usuario, contrasena) para asegurarse de que rechaza el acceso con credenciales inválidas.
- ***Implementación:***
```python
def test_login_fail():
    login_fails = login("Metodologias", "710012C")
    assert not login_fails
```
## Ejecución de Pruebas Unitarias y Análisis de Cobertura
Para ejecutar las pruebas unitarias y analizar la cobertura del código, se utilizaron los siguientes comandos en la terminal:

- **pytest -v:**

Ejecuta todas las pruebas unitarias definidas en test_main.py y muestra la salida detallada (-v para verbose).
- **coverage run -m pytest:**

Ejecuta pytest mientras mide la cobertura de código usando coverage.
- **coverage report:**

Muestra un informe detallado de la cobertura del código en la terminal.
- **coverage html:**

Genera un informe HTML interactivo que muestra la cobertura del código.

## Resultados del informe
A continuación se presentan los resultados del análisis de cobertura del código:

```plaintext
Name           Stmts   Miss  Cover
----------------------------------
main.py            8      0   100%
test_main.py      17      0   100%
----------------------------------
TOTAL             25      0   100%
```
### main.py:
- Contiene 8 líneas en total.
- Todas las líneas están cubiertas por las pruebas unitarias, lo que significa que todas las líneas de código fueron ejecutadas al menos una vez durante las pruebas.
- Cobertura del 100%.
### test_main.py:
- Contiene 17 líneas en total.
- Todas las líneas están cubiertas por las pruebas unitarias, lo que significa que todas las líneas de código fueron ejecutadas al menos una vez durante las pruebas.
- Cobertura del 100%.
### Total:
- En conjunto, el proyecto tiene 25 líneas de código.
- Todas las líneas están cubiertas por las pruebas unitarias.
- Cobertura total del 100%.

Estos resultados indican que todas las funciones y líneas de código en ambos archivos (main.py y test_main.py) están completamente probadas y ejecutadas según lo esperado durante el análisis de cobertura.


