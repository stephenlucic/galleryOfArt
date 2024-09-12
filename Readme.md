![](https://cdn.hashnode.com/res/hashnode/image/upload/v1636780048014/niLN2J80j.png)

![](https://img.shields.io/github/stars/pandao/editor.md.svg) ![](https://img.shields.io/github/forks/pandao/editor.md.svg) ![](https://img.shields.io/github/tag/pandao/editor.md.svg) ![](https://img.shields.io/github/release/pandao/editor.md.svg) ![](https://img.shields.io/github/issues/pandao/editor.md.svg) ![](https://img.shields.io/bower/v/editor.md.svg)

# GalleryOfArt

Este proyecto es una aplicación web de galería de arte que permite la compra y venta de obras de arte. Está desarrollado utilizando el framework **Django** y **SQLite** como base de datos.

## Características

- Visualización de galerías de arte.
- Sistema de compra y venta de obras de arte.
- Gestión de usuarios (autenticación y autorización).
- Soporte para agregar, editar y eliminar obras de arte.
- Interfaz amigable para la visualización de las obras disponibles.

## Requisitos

Antes de comenzar, asegúrate de tener los siguientes requisitos instalados en tu sistema:

- Python 3.x
- Django 4.x
- SQLite (incluido en Python)

## Instalación

Sigue estos pasos para configurar el proyecto localmente:

- Clona este repositorio en tu máquina local:  
```
git clone https://github.com/stephenlucic/galleryOfArt.git
 ```
- Crea un entorno virtual y activa:
```
python -m venv venv
venv\Scripts\activate # En MacOs usa `source env/bin/activate` 
```
- Instala las dependencias:
`pip install -r requeriments.txt`

- Realiza las migraciones de la base de datos:
```
python manage.py migrate
```
- Inicia el servidor local:
```
python manage.py runserver
```

## Modo de uso

#### Añadir Obras de Arte
Para añadir una nueva obra de arte, necesitarás iniciar sesión como administrador y dirigirte a la sección de administración de Django (http://127.0.0.1:8000/admin) o utilizar los usuarios con permisos correspondientes

#### Comprar Obras de Arte
Los usuarios registrados podrán navegar por las distintas galerías y comprar las obras disponibles.

#### Funcionalidades Adicionales
- Autenticación de usuarios: Los usuarios pueden registrarse, iniciar sesión y gestionar su perfil.
- Gestión de inventario: Los administradores pueden gestionar las obras de arte disponibles en la plataforma.
