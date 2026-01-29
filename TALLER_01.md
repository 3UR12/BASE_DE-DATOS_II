![Logo del Taller](images/logo.png)
# BASES DE DATOS II
## TALLER N°1

**EURIS RODRIGUEZ 8-1013-2315**

---

## Problema #1: Identificación del tipo de cardinalidad

Una universidad maneja la siguiente información:
- Un estudiante puede estar inscrito en varias materias.
- Una materia puede tener muchos estudiantes inscritos.

### Preguntas:

1. **¿Qué tipo de relación existe entre Estudiante y Materia?**  
   **R:** Existe una relación de muchos a muchos N:M.

2. **¿Cuál es la cardinalidad de esta relación?**  
   **R:** N:M (Muchos a muchos).

3. **¿Por qué no sería correcto modelar como 1:1 o 1:N?**  
   **R:** Porque según el enunciado un estudiante puede estar inscrito en muchas materias y una materia puede tener muchos estudiantes, la relación 1:1 diría que un estudiante solo puede tener una materia, de la misma manera que una materia solo puede tener un estudiante, cuando debería ser que muchos estudiantes pueden estar inscritos en muchas materias.  
   En cuanto a 1:N, tampoco está correcto porque limitaría a que muchas materias solo pueden tener 1 solo estudiante inscrito cuando debería tener muchos estudiantes inscritos en muchas materias.

4. **Dibuja cómo se vería la cardinalidad usando una de las simbologías explicadas en clase.**  
   **R:**  
Estudiante —(0,N)—<>—(0,N)— Materia

text

---

## Problema #2: Cardinalidad aplicada en el modelo entidad-relación

Con base en el siguiente escenario:
- Un cliente puede realizar muchos pedidos.
- Cada pedido pertenece a un solo cliente.
- Un pedido no puede existir sin un cliente.

### Preguntas:

1. **Indica la cardinalidad entre Cliente y Pedido.**  
**R:** Uno a muchos 1:N

2. **Especifica si la participación del Pedido es total u opcional.**  
**R:** Un pedido no puede existir sin un cliente, basado en esto diría que total.

3. **Dibuja cómo se vería la cardinalidad usando una de las simbologías explicadas en clase.**  
**R:**  
Cliente —(1,1)—<>—(0,N)— Pedido

text

---

### Indique cuáles son los tipos de cardinalidad:
a. Relación 1-1.  
b. Relación 0-0.  
c. Relación R-r.  
d. Relación 1-N.  
e. Relación N-M.  

**NOTA:** Selección múltiple

---

## II PARTE - Normalización - 30 puntos

Basándonos en los siguientes enunciados, aplique el concepto de normalización:

### 1. Desea realizar la normalización N1 o primera forma normal (FN) de la siguiente tabla.

**¿Cómo lo haría?**

**R:** Según la norma N1, cada celda debe tener un solo valor y sin grupos repetitivos, en este caso la columna cuentas no sigue esa regla, por ende, se agrega otras filas para que cada una solo ocupe una, el dni se duplica para que la clave primaria se use con la combinación de dni y cuenta.

### 2. Desea realizar la normalización 2FN o segunda forma normal de la siguiente tabla.

*(Nota: Se necesitaría ver la tabla específica para dar una respuesta detallada)*

### 3. ¿Cuál sería la diferencia entre la 1FN y la 2FN?

**R:** Según yo la diferencia es que el 1FN no permite listas en una celda, o más de un valor en una celda, su finalidad es que cada celda solo tenga un dato y 2FN separa los datos repetidos innecesariamente, para eso crea otra tabla para los datos que no necesitan toda la clave, o sea que cada dato que no tenga clave de penda de la clave primaria, los organiza por categorías para no repetir.

### 4. Desea realizar la normalización 3FN o tercera forma normal de la siguiente tabla.

*(Nota: Se necesitaría ver la tabla específica para dar una respuesta detallada)*

### 5. Si analizando un caso práctico se encontrara en el paso de la 2ª FN, ¿qué debería comprobar usted para seguir normalizando hasta la 3ª FN?

**R:** Necesitaría comprobar si hay datos que dependan de otros, ejemplo si hay una columna de departamentos de UDELAS y otra en la misma tabla de nombre de departamento, rrhh, ventas, marketing etc, el departamento siempre va a dictar por defecto el nombre, o sea si es departamento D00 y en Nombre_departamento está ventas, ya se que cualquiera que tenga D00 va a estar en ventas entonces esas 2 columnas se deben separar en 2 tablas que es la normalización 3FN, una para los empleados donde diga el departamento y otra de departamentos donde diga el nombre del departamento.

---

## III PARTE - Diagrama entidad-relación - 50 puntos

### Parte A

Basándose en los enunciados, analice y resuelva las siguientes preguntas:

#### 1. Usted comienza a trabajar como administrador de bases de datos y le piden que, por favor, diseñe la relación entre un cliente y sus cuentas bancarias, brindándole los siguientes datos. Cuentas bancarias: código de cuenta (único), número de cuenta, dinero contenido en ella y, por otra parte, nombre, apellidos y cédula del cliente.

**¿Cómo plantearía el análisis de poder realizar un diagrama entidad-relación?**

**R:** Primero me concentraría en identificar las entidades principales, en este caso serían Cliente y Cuenta bancaria.  
Luego vería qué atributos tiene cada una: para el Cliente serían nombre, apellidos y cédula y para la cuenta serían código único de cuenta, número de cuenta y dinero contenido.  
Después analizaría la relación entre ellas. Veo que un cliente puede tener varias cuentas bancarias, pero cada cuenta pertenece a un solo cliente esto asumiendo cuentas individuales, eso me da una relación uno a muchos (1:N).  
Para conectarlas en la base de datos, usaría la cédula del cliente como referencia en la tabla de Cuentas. Así, cuando necesite saber qué cliente tiene una cuenta, o qué cuentas tiene un cliente, puedo hacer esa relación directamente.  
Con eso ya tengo la base para hacer el diagrama: dos entidades, sus atributos, y una relación 1:N entre ellas.

#### 2. Realizando su labor diaria de diseñador de base de datos, se encuentra con el siguiente planteamiento: Una empresa de gestión de inversiones desea crear una base de datos para manejar la cartera de acciones y órdenes de compraventa de sus clientes. Para cada una de las acciones se guarda el nombre de la empresa, su NIF, siglas y domicilio. Además, se almacenan las cotizaciones de las acciones, con la fecha y hora de la cotización.

**¿Qué entidades encuentra y de qué tipo?**

**R:** Las entidades que encuentro son:
- **Acción**: en esta va el nombre, nif, siglas, domicilio y la lista de cotización con fecha y hora.
- **Cliente**: aunque no dan sus atributos, se menciona que es quien tiene la cartera y hace órdenes.
- **Orden**: esta registra las operaciones de compra y venta.

De tipo serían todas entidades fuertes porque cada una tiene su identificador único, aunque la cotización que se menciona podría verse como parte de Acción o como algo aparte, pero relacionado.

### Parte B

Realice los diagramas entidad-relación con alguna de las herramientas o en papel.

Tomar en cuenta que para realizar un diagrama entidad-relación y resolver las distintas situaciones reales se debe seguir una serie de pasos:
1. Seleccionar las distintas entidades, así como su tipología y sus atributos; el atributo clave de cada entidad o posibles atributos clave.
2. Una entidad se relaciona con otra mediante conectores y relaciones representadas con rombos.
3. Toda relación debe llevar indicada una cardinalidad. Debe buscarse la mejor conjunción de elementos para obtener la solución más eficiente; para ello, ante situaciones más complicadas, se recurrirá a nuevos elementos, los cuales se describen a continuación.

---

#### Problema #3: Sistema de gestión de citas médicas

Una clínica privada desea implementar un sistema para administrar sus pacientes, médicos y citas.

**Detalle:**
- Un paciente puede tener muchas citas.
- Un médico puede atender muchas citas.
- Cada cita corresponde a un solo paciente y un solo médico.
- Una cita tiene: fecha, hora y motivo.
- Un médico puede existir en el sistema aunque aún no tenga citas asignadas.

**Solucione los siguientes puntos:**

1. **Identificar las entidades principales.**  
**R:** Paciente, Médico y Cita.  
Paciente: atributos como ID, nombre, teléfono.  
Médico: ID, nombre, especialidad.  
Cita: fecha, hora, motivo.

2. **Determinar las relaciones entre ellas.**  
**R:** El paciente tiene cita y el médico atiende la cita.

3. **Definir la cardinalidad y la participación.**  
**R:** 
- Paciente: Cita: (1, N) un paciente puede tener muchas citas.
- Médico: Cita: (1, N) un médico atiende muchas citas.
- Cita: Paciente y Médico: (1,1) porque cada cita es de un paciente y un médico.
- Participación: Médico puede existir sin citas, Paciente también puede no tener citas aún, Cita necesita obligatoriamente un paciente y un médico para existir.

4. **Dibujar el diagrama entidad-relación correctamente.**  
*(Diagrama en texto simplificado)*
Paciente —(1,N)—<>—(1,1)— Cita —(1,1)—<>—(1,N)— Médico

text

---

#### Problema #4: Sistema de ventas de una tienda en línea

Una tienda en línea quiere controlar a sus clientes, productos y ventas.

**Detalle:**
- Un cliente puede realizar muchas ventas.
- Cada venta pertenece a un solo cliente.
- Una venta puede incluir varios productos.
- Un producto puede aparecer en muchas ventas.
- De cada producto vendido se debe registrar la cantidad y el precio de venta.
- Un producto puede existir aunque aún no se haya vendido.

**Solucione los siguientes puntos:**

1. **Identificar todas las entidades involucradas.**  
**R:** 
- Cliente: ID, nombre, dirección.
- Producto: ID, nombre, precio.
- Venta: número de venta, fecha, total.

2. **Detectar relaciones y cardinalidades.**  
**R:** 
- Cliente realiza Venta: (1, N) porque un cliente hace muchas ventas, cada venta es de un cliente.
- Venta incluye Producto: (N, M) porque una venta puede tener varios productos y un producto puede estar en varias ventas.

3. **Resolver la relación N:M entre Venta y Producto.**  
**R:** Se hace una tabla DetalleVenta que lleve el id de venta y el id de producto, cantidad vendida y el precio de venta en ese momento.

4. **Modelar correctamente los atributos dependientes de la relación.**  
**R:** Cantidad y precio de venta no van en Producto ni en Venta, van en la tabla DetalleVenta porque dependen de cada venta concreta.

---

**Se deberá subir el desarrollo del taller; se debe subir en el repositorio llamado "BASE_DE DATOS_II" en la carpeta de "TALLER_01", adjuntando el documento y los diagramas en el Moodle.**
