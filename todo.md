## Index

- [Index](#index)
  - [Notas para el lector](#notas-para-el-lector)
  - [Implementaciones esenciales y prioridades](#implementaciones-esenciales-y-prioridades)
  - [Futuras implementaciones](#futuras-implementaciones)

### Notas para el lector

Este documento describe las funcionalidades esenciales y futuras implementaciones de la aplicación de gestión de presupuestos. Cabe destacar que este documento es un trabajo en progreso y puede ser modificado en el futuro para incluir información adicional relevante, ya sea en cuanto a la descripción de las funcionalidades, su implementación técnica o consideraciones adicionales.

Se recomienda a los lectores revisar periódicamente este documento para estar al día con las últimas modificaciones y actualizaciones.

### Implementaciones esenciales y prioridades

**1. Implementar MongoDB API:**

- **Descripción:** Crear una interfaz de programación de aplicaciones (API) que permita interactuar con la base de datos MongoDB. La API debe proporcionar los siguientes puntos finales:

  - Insertar un gasto del presupuesto
  - Actualizar un gasto del presupuesto
  - Eliminar un gasto del presupuesto
  - Mostrar historial de gastos
  - Insertar y actualizar nuevo presupuesto

- **Implementación:**
  - Utilizar el controlador oficial de MongoDB para el lenguaje de programación elegido.
    - **Se estará utilizando `pymongo` versión '4.6.3'.** ✅
  - Definir los puntos finales para cada operación de la API.
  - Implementar la lógica para cada punto final, incluyendo la validación de datos, la interacción con la base de datos y la gestión de errores.
  - Asegurar la seguridad de la API mediante la autenticación y autorización adecuadas.

**2. Funcionalidades sin sistema de usuarios:**

- **Nota:** Las funcionalidades descritas en la sección [Implementaciones esenciales y prioridades](#implementaciones-esenciales-y-prioridades) no requieren un sistema de usuarios en esta etapa. La implementación del sistema de usuarios se abordará en una fase posterior.

**3. Consideraciones adicionales:**

- **Documentación:** Es importante documentar la API de forma clara y concisa, incluyendo ejemplos de uso, códigos de respuesta y errores potenciales.
- **Pruebas:** Implementar pruebas unitarias y de integración para garantizar el correcto funcionamiento de la API.
- **Despliegue:** Elegir una estrategia adecuada para desplegar la API en un entorno de producción, como un servidor web o una plataforma en la nube.

### Futuras implementaciones

**1. Base de datos de usuarios:**

- **Descripción:** Crear una base de datos para almacenar información sobre los usuarios, como nombres, correos electrónicos, contraseñas y roles.

- **Implementación:**
  - Diseñar el esquema de la base de datos de usuarios.
  - Implementar las operaciones CRUD (Crear, Leer, Actualizar y Eliminar) para la gestión de datos de usuarios.
  - Asegurar la seguridad de la base de datos mediante el cifrado de contraseñas y otras medidas de protección.

**2. Manejo de usuarios:**

- **Descripción:** Integrar el sistema de usuarios con la gestión de presupuestos. Los usuarios deben poder crear, editar y eliminar sus propios presupuestos, así como ver los presupuestos de otros usuarios según los permisos asignados.

- **Implementación:**
  - Implementar la autenticación y autorización de usuarios en la API.
  - Asociar cada presupuesto a un usuario o grupo de usuarios.
  - Aplicar controles de acceso para limitar el acceso a los presupuestos en función de los roles de los usuarios.

**3. API's extras:**

- **Descripción:** Definir y desarrollar API's adicionales que complementen la funcionalidad principal de la aplicación. Estas API's podrían incluir:

  - Generación de informes de gastos
  - Exportación de datos a diferentes formatos
  - Integración con otras aplicaciones

- **Implementación:**
  - Realizar un análisis de requerimientos para determinar las API's extras necesarias.
  - Diseñar y desarrollar las API's extras de acuerdo con las mejores prácticas de desarrollo de software.
  - Documentar y probar las API's extras para garantizar su correcto funcionamiento.

**4. Reunión:**

- **Descripción:** Se recomienda realizar una reunión para discutir los detalles de las API's extras y definir los próximos pasos en el desarrollo de la aplicación.

- **Objetivos:**
  - Definir los requisitos específicos de las API's extras.
  - Asignar responsabilidades para el desarrollo de las API's extras.
  - Establecer un cronograma para la implementación de las API's extras.

**5. Consideraciones finales:**

- La priorización de las funcionalidades descritas en este documento puede ajustarse según las necesidades específicas del proyecto.
- Es importante mantener una comunicación fluida entre todos los involucrados en el desarrollo de la aplicación.
- Se recomienda adoptar una metodología de desarrollo ágil para adaptarse a los cambios y responder a las necesidades del proyecto de manera eficiente.
