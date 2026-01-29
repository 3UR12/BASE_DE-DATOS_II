
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
