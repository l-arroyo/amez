[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9881913&assignment_repo_type=AssignmentRepo)

[![Actions Status](https://github.com/DWES-LE/conference-cms-wagtail-lucas-y-miguel/actions/workflows/pruebas.yml/badge.svg)](https://github.com/DWES-LE/conference-cms-wagtail-lucas-y-miguel/actions/workflows/pruebas.yml)

# CMS Conferencia template

El objetivo de la tarea es crear una página web para una conferencia con el CMS Wagtail.
Este es un trabajo en grupo. 
Podéis replicar alguno de los modelos que se muestran en la sección de análisis o crear uno propio con un tema que os interese.

## Análisis
Estudia algunas webs de conferencias para hacerte una idea:
* https://www.tarugoconf.com/
* https://pydata.org/seattle2023/
* https://2023.djangocon.eu/
* https://ep2022.europython.eu/
* https://rubyconf.org/
* https://birmingham.wordcamp.org/2023/
* https://2022.drupalcamp.es/

Analizad el contenido de las webs y las funcionalidades que ofrecen. Los típos de páginas que se suelen tener son:
* Home (página principal con la información más importante y que interesará a los visitantes)
* Sobre la conferencia (historia, objetivos, etc.)
* Programa (charlas, talleres, etc.)
* Ponentes (nombre, foto, bio, etc.)
* Patrocinadores (logo, enlace, etc.)
* Contacto (formulario de contacto, dirección, mapa, etc.)
* Blog (noticias, artículos, etc.)

---

## Proceso
* Dedidid la estructura que va a tener vuestra conferencia (árbol)
* Diseñad los modelos que vais a necesitar. Cuáles serán páginas y cuáles contenio que se mostrará en una página pero que no es una página en sí. 
* Repartid las tareas y recordad siempre el flujo de trabajo:
  * Usad ramas
  * Haced pull request para integrar los cambios
  * Antes de empezar a trabajar: `git status` y `git pull`
  * Al terminar: `git commit` y `git push`
* Diseñad la página principal
* Id creando los modelos y sus plantillas y probando que funcionan bien.
* Cread los tests que sean necesarios para asegurar que todo funciona correctamente.
* Cread páginas con datos y generad un volcado (`dumpdata`).

---

## Tareas equipo
### Diseño:
- [X] Añadir tema bootstrap _(Lucas)_
- [ ] Ajustar el tema bootstrap a la página blog_index.html y blog_page.html _(Miguel)_
### Página home:
- [X] Partials ESENCIALES: hero, nav, footer _(Lucas)_
- [ ] Partials EXTRA: botones, links, imágenes...
- [X] Información (texto, imágenes, etc.) _(Miguel y Lucas)_
### Página del Evento _(80's Party)_
- [X] Concepto
- [ ] Artistas invitados _(Ponentes)_
- [ ] Información de interés
- [X] Fecha y Lugar
- [ ] Programación

### Página de Integrantes de la asociación _(miebros)_
- [ ] Crear modelo (añadir campo de listado de miembros con galería de imágenes, nombre y descripción) _(Lucas)_
- [ ] Importar temas de bootstrap para el listado de miembros _(Miguel)_

### Contacto
- [ ] Crear modelo _(Lucas)_
- [ ] Formulario de contacto
- [ ] Redes sociales
### Blog
- [ ] Bootstrap en el listado de entradas _(Miguel)_
- [X] Entradas _(Miguel y Lucas)_
- [ ] Añadir banners a la derecha para unirse al canal de discord y redes sociales _(Miguel)_