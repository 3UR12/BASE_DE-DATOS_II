<div align="center">
  <img src="images/logo.png" alt="Logo del Taller" width="200">
  
  # BASES DE DATOS II
  ## TALLER N°1
  
  **EURIS RODRIGUEZ 8-1013-2315**
</div>

---

## 📋 **Problema #1: Identificación del tipo de cardinalidad**

Una universidad maneja la siguiente información:
- Un estudiante puede estar inscrito en varias materias.
- Una materia puede tener muchos estudiantes inscritos.

### **📝 Preguntas:**

1. **¿Qué tipo de relación existe entre Estudiante y Materia?**  
R: Existe una relación de muchos a muchos N:M.

2. **¿Cuál es la cardinalidad de esta relación?**  
R: N:M (Muchos a muchos).

3. **¿Por qué no sería correcto modelar como 1:1 o 1:N?**  
R: Porque según el enunciado un estudiante puede estar inscrito en muchas materias y una materia puede tener muchos estudiantes, la relación 1:1 diría que un estudiante solo puede tener una materia, de la misma manera que una materia solo puede tener un estudiante, cuando debería ser que muchos estudiantes pueden estar inscritos en muchas materias.  
En cuanto a 1:N, tampoco esta correcto porque limitaría a que muchas materias solo pueden tener 1 solo estudiante inscrito cuando debería tener muchos estudiantes inscritos en muchas materias.

4. **Dibuja cómo se vería la cardinalidad usando una de las simbologías explicadas en clase.**

<div align="center">
  <img src="images/problema1.png" alt="Diagrama cardinalidad Estudiante-Materia" width="400">
  <br>
  <em>Figura 1: Relación N:M entre Estudiante y Materia</em>
</div>

---

## 📋 **Problema #2: Cardinalidad aplicada en el modelo entidad-relación**

Con base en el siguiente escenario:
- Un cliente puede realizar muchos pedidos.
- Cada pedido pertenece a un solo cliente.
- Un pedido no puede existir sin un cliente.

### **📝 Preguntas:**

1. **Indica la cardinalidad entre Cliente y Pedido.**  
R: Uno a muchos 1:N

2. **Especifica si la participación del Pedido es total u opcional.**  
R: Un pedido no puede existir sin un cliente, basado en esto diría que total.

3. **Dibuja cómo se vería la cardinalidad usando una de las simbologías explicadas en clase.**

<div align="center">
  <img src="images/problema2.png" alt="Diagrama cardinalidad Cliente-Pedido" width="400">
  <br>
  <em>Figura 2: Relación 1:N entre Cliente y Pedido</em>
</div>

---

### **🔍 Indique cuáles son los tipos de cardinalidad:**
a. ✅ Relación 1-1.  
b. Relación 0-0.  
c. Relación R-r.  
d. ✅ Relación 1-N.  
e. ✅ Relación N-M.  

**Respuesta correcta: a, d, e**  
**NOTA:** Selección múltiple

---

## 📊 **II PARTE - Normalización - 30 puntos**

Basándonos en los siguientes enunciados, aplique el concepto de normalización:

### **1. Desea realizar la normalización N1 o primera forma normal (FN) de la siguiente tabla.**

<div align="center">
  <img src="images/tabla1questions.png" alt="Tabla para normalización 1FN" width="500">
</div>

**¿Cómo lo haría?**

<div align="center">
  <img src="images/problema3.png" alt="Solución normalización 1FN" width="500">
  <br>
  <em>Figura 3: Solución de la primera forma normal</em>
</div>

R: Según la norma N1, cada celda debe tener un solo valor y sin grupos repetitivos, en este caso la columna cuentas no sigue esa regla, por ende, se agrega otras filas para que cada una solo ocupe una, el dni se duplica para que la clave primaria se use con la combinación de dni y cuenta.

---

### **2. Desea realizar la normalización 2FN o segunda forma normal de la siguiente tabla.**

<div align="center">
  <img src="images/tabla2questions.png" alt="Tabla para normalización 2FN" width="500">
</div>

<div align="center">
  <img src="images/problema4.png" alt="Solución normalización 2FN" width="500">
  <br>
  <em>Figura 4: Solución de la segunda forma normal</em>
</div>

---

### **3. ¿Cuál sería la diferencia entre la 1FN y la 2FN?**

R: según yo la diferencia es que el 1fn no permite listas en una celda, o más de un valor en una celda, su finalidad es que cada celda solo tenga un dato y 2fn separa los datos repetidos innecesariamente, para eso crea otra tabla para los datos que no necesitan toda la clave, o sea que cada dato que no tenga clave de penda de la clave primaria, los organiza por categorías para no repetir.

---

### **4. Desea realizar la normalización 3FN o tercera forma normal de la siguiente tabla.**

<div align="center">
  <img src="images/tabla3questions.png" alt="Tabla para normalización 3FN" width="500">
</div>

<div align="center">
  <img src="images/problema5.png" alt="Solución normalización 3FN" width="500">
  <br>
  <em>Figura 5: Solución de la tercera forma normal</em>
</div>

---

### **5. Si analizando un caso práctico se encontrara en el paso de la 2ª FN, ¿qué debería comprobar usted para seguir normalizando hasta la 3ª FN?**

R: Necesitaria comprobar si hay datos que dependan de otros, ejemplo si hay una columna de departamentos de UDELAS y otra en la misma tabla de nombre de departamento, rhhh, ventas, marketing ect, el departamento siempre va a dictar por defecto el nombre, o sea si es departamento D00 y en Nombre_departamento esta ventas, ya se que cualquiera que tenga D00 va a estar en ventas entonces esas 2 columnas se deben separa en 2 tablas que es la normalización 3FN, una para los empleados donde diga el departamento y otra dedepartamentos donde diga el nombre del departamento.

---

## 🔗 **III PARTE - Diagrama entidad-relación - 50 puntos**

### **📂 Parte A**

#### **1. Diseño de relación Cliente-Cuentas Bancarias**

**¿Cómo plantearía el análisis de poder realizar un diagrama entidad-relación?**  
R: Primero me concentraría en identificar las entidades principales, en este caso serían Cliente y Cuenta bancaria.  
Luego vería qué atributos tiene cada una: para el Cliente serían nombre, apellidos y cédula y para la cuenta serían código único de cuenta, número de cuenta y dinero contenido.  
Después analizaría la relación entre ellas. Veo que un cliente puede tener varias cuentas bancarias, pero cada cuenta pertenece a un solo cliente esto asumiendo cuentas individuales, eso me da una relación uno a muchos (1:N).  
Para conectarlas en la base de datos, usaría la cédula del cliente como referencia en la tabla de Cuentas. Así, cuando necesite saber qué cliente tiene una cuenta, o qué cuentas tiene un cliente, puedo hacer esa relación directamente.  
Con eso ya tengo la base para hacer el diagrama: dos entidades, sus atributos, y una relación 1:N entre ellas.

#### **2. Sistema de Gestión de Inversiones**

**¿Qué entidades encuentra y de qué tipo?**  
R: Las entidades que encuentro son:  
Las entidades que encuentro son Acción, en esta va el nombre, nif, siglas, domicilio y la lista de cotización con fecha y hora, Cliente, aunque no dan sus atributos, se menciona que es quien tiene la cartera y hace órdenes y Orden, esta registra las operaciones de compra y venta.  
De tipo serían todas entidades fuertes porque cada una tiene su identificador único, aunque la cotización que se menciona podría verse como parte de Acción o como algo aparte, pero relacionado.

---

### **📂 Parte B**

**Pasos para diagramas ER:**
1. Seleccionar entidades, tipología y atributos (incluyendo claves primarias)
2. Conectar entidades mediante relaciones representadas con rombos
3. Especificar cardinalidad para cada relación
4. Buscar la solución más eficiente

---

## 🏥 **Problema #3: Sistema de gestión de citas médicas**

Una clínica privada desea implementar un sistema para administrar sus pacientes, médicos y citas.

**Detalle:**
- Un paciente puede tener muchas citas.
- Un médico puede atender muchas citas.
- Cada cita corresponde a un solo paciente y un solo médico.
- Una cita tiene: fecha, hora y motivo.
- Un médico puede existir en el sistema aunque aún no tenga citas asignadas.

### **📝 Solución:**

1. **Identificar las entidades principales.**  
R: Paciente, Médico y Cita.  
Paciente: atributos como ID, nombre, teléfono.  
Médico: ID, nombre, especialidad.  
Cita: fecha, hora, motivo.

2. **Determinar las relaciones entre ellas.**  
R: El paciente tiene cita y el médico atiende la cita.

3. **Definir la cardinalidad y la participación.**  
R: Paciente: Cita: (1, N) un paciente puede tener muchas citas.  
Médico: Cita: (1, N) un médico atiende muchas citas.  
Cita: Paciente y Médico: (1,1) porque cada cita es de un paciente y un médico.  
Participación: Médico puede existir sin citas, Paciente también puede no tener citas aún, Cita necesita obligatoriamente un paciente y un médico para existir.

4. **Diagrama entidad-relación:**

<div align="center">
  <img src="images/problema6.png" alt="Diagrama ER Sistema de Citas Médicas" width="600">
  <br>
  <em>Figura 6: Diagrama ER para sistema de citas médicas</em>
</div>

---

## 🛒 **Problema #4: Sistema de ventas de una tienda en línea**

Una tienda en línea quiere controlar a sus clientes, productos y ventas.

**Detalle:**
- Un cliente puede realizar muchas ventas.
- Cada venta pertenece a un solo cliente.
- Una venta puede incluir varios productos.
- Un producto puede aparecer en muchas ventas.
- De cada producto vendido se debe registrar la cantidad y el precio de venta.
- Un producto puede existir aunque aún no se haya vendido.

### **📝 Solución:**

1. **Identificar todas las entidades involucradas.**  
R: Cliente: ID, nombre, dirección.  
Producto: ID, nombre, precio.  
Venta: número de venta, fecha, total.

2. **Detectar relaciones y cardinalidades.**  
R: Cliente realiza Venta: (1, N) porque un cliente hace muchas ventas, cada venta es de un cliente.  
Venta incluye Producto: (N, M) porque una venta puede tener varios productos y un producto puede estar en varias ventas.

3. **Resolver la relación N:M entre Venta y Producto.**  
R: Se hace una tabla DetalleVenta que lleve el id de venta y el id de producto, cantidad vendida y el precio de venta en ese momento.

4. **Modelar correctamente los atributos dependientes de la relación.**  
R: Cantidad y precio de venta no van en Producto ni en Venta, van en la tabla DetalleVenta porque dependen de cada venta concreta.

---

<div align="center">
  <strong>🎯 FIN DEL TALLER</strong>
  <br>
  <em>Se deberá subir el desarrollo del taller; se debe subir en el repositorio llamado "BASE_DE DATOS_II" en la carpeta de "TALLER_01", adjuntando el documento y los diagramas en el Moodle.</em>
</div>
