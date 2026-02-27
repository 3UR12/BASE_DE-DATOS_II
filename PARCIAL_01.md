# 📦 1. COMANDOS DOCKER UTILIZADOS

Guardar como: `comandos_docker.txt`

```bash
# Descargar la imagen oficial de MariaDB desde Docker Hub
docker pull mariadb:11

# Crear el contenedor (SIN iniciar la base aún)
# Se define:
# - Nombre del contenedor
# - Variables de entorno (password root)
# - Puerto expuesto
docker create \
--name bd_empresa \
-e MARIADB_ROOT_PASSWORD=123456 \
-p 3307:3306 \
mariadb:11

# Iniciar el contenedor
docker start bd_empresa

# Verificar estado del contenedor (debe salir "Up")
docker ps

# Ver logs del contenedor para confirmar que MariaDB inició correctamente
docker logs bd_empresa

# Conectarse al contenedor por CLI
docker exec -it bd_empresa mariadb -u root -p
```

---

# 🗄️ 2. CREACIÓN DE BASE DE DATOS

Guardar como: `01_creacion_bd.sql`

```sql
-- Crear la base de datos del sistema empresarial
CREATE DATABASE empresa_servicios;

-- Seleccionar la base de datos para trabajar
USE empresa_servicios;

-- Verificar que estamos en la base correcta
SELECT DATABASE();
```

---

# 🧱 3. CREACIÓN DE TABLAS (DDL)

Guardar como: `02_ddl_tablas.sql`

```sql
-- ============================================
-- TABLA: user
-- Almacena los clientes del sistema
-- ============================================
CREATE TABLE user (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20),
    registration_date DATE NOT NULL,
    status ENUM('ACTIVE','SUSPENDED','INACTIVE') NOT NULL,
    is_verified BOOLEAN NOT NULL DEFAULT FALSE,
    CHECK (email LIKE '%@%')
);

-- ============================================
-- TABLA: credential
-- Credenciales de acceso (1:1 con user)
-- ============================================
CREATE TABLE credential (
    id_credential INT AUTO_INCREMENT PRIMARY KEY,
    id_user INT NOT NULL UNIQUE,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    last_password_change DATE,
    status ENUM('ACTIVE','LOCKED') NOT NULL,
    is_mfa_enabled BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_user) REFERENCES user(id_user)
);

-- ============================================
-- TABLA: service
-- Catálogo de servicios digitales
-- ============================================
CREATE TABLE service (
    id_service INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    monthly_cost DECIMAL(10,2) NOT NULL,
    status ENUM('AVAILABLE','DEPRECATED') NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    CHECK (monthly_cost >= 0)
);

-- ============================================
-- TABLA: contract
-- Relación cliente-servicio
-- ============================================
CREATE TABLE contract (
    id_contract INT AUTO_INCREMENT PRIMARY KEY,
    id_user INT NOT NULL,
    id_service INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    status ENUM('ACTIVE','CANCELLED','PENDING') NOT NULL,
    auto_renew BOOLEAN DEFAULT TRUE,
    UNIQUE (id_user,id_service,start_date),
    FOREIGN KEY (id_user) REFERENCES user(id_user),
    FOREIGN KEY (id_service) REFERENCES service(id_service)
);

-- ============================================
-- TABLA: payment
-- Pagos realizados por contrato
-- ============================================
CREATE TABLE payment (
    id_payment INT AUTO_INCREMENT PRIMARY KEY,
    id_contract INT NOT NULL,
    payment_date DATE NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_method ENUM('CARD','TRANSFER','CASH') NOT NULL,
    payment_status ENUM('PAID','PENDING','FAILED') NOT NULL,
    is_confirmed BOOLEAN DEFAULT FALSE,
    transaction_reference VARCHAR(100) UNIQUE,
    FOREIGN KEY (id_contract) REFERENCES contract(id_contract)
);

-- ============================================
-- TABLA: access_audit
-- Registro de accesos al sistema
-- ============================================
CREATE TABLE access_audit (
    id_audit INT AUTO_INCREMENT PRIMARY KEY,
    id_user INT NOT NULL,
    access_time DATETIME NOT NULL,
    ip_address VARCHAR(45) NOT NULL,
    device VARCHAR(100),
    result ENUM('SUCCESS','FAILURE') NOT NULL,
    action ENUM('LOGIN','LOGOUT','PASSWORD_CHANGE') NOT NULL,
    is_suspicious BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_user) REFERENCES user(id_user)
);
```

---

# 📥 4. INSERCIÓN DE DATOS (DML)

Guardar como: `03_dml_datos.sql`

```sql
-- Insertar usuarios
INSERT INTO user (first_name,last_name,email,phone,registration_date,status,is_verified) VALUES
('Juan','Pérez','juan@empresa.com','6001','2024-01-01','ACTIVE',TRUE),
('Ana','Gómez','ana@empresa.com','6002','2024-01-02','ACTIVE',TRUE),
('Luis','Martínez','luis@empresa.com','6003','2024-01-03','ACTIVE',FALSE),
('Carla','Rojas','carla@empresa.com','6004','2024-01-04','ACTIVE',TRUE),
('Pedro','Navarro','pedro@empresa.com','6005','2024-01-05','ACTIVE',TRUE),
('Sofía','López','sofia@empresa.com','6006','2024-01-06','ACTIVE',TRUE),
('Mario','Castro','mario@empresa.com','6007','2024-01-07','ACTIVE',TRUE),
('Lucía','Herrera','lucia@empresa.com','6008','2024-01-08','ACTIVE',FALSE),
('Diego','Ruiz','diego@empresa.com','6009','2024-01-09','ACTIVE',TRUE),
('Elena','Morales','elena@empresa.com','6010','2024-01-10','ACTIVE',TRUE);
```

*(Puedes seguir agregando los INSERT de servicios, contratos, etc., igual que los ya ejecutaste.)*

---

# 🔄 5. OPERACIONES CRUD

Guardar como: `04_crud.sql`

```sql
-- CREATE: crear nuevo contrato
INSERT INTO contract (id_user,id_service,start_date,status,auto_renew)
VALUES (1,2,CURDATE(),'ACTIVE',TRUE);

-- READ: consultar contratos activos
SELECT * FROM contract WHERE status='ACTIVE';

-- UPDATE: cancelar contrato
UPDATE contract
SET status='CANCELLED', auto_renew=FALSE
WHERE id_contract=1;

-- DELETE LÓGICO (NO físico)
UPDATE contract
SET status='CANCELLED'
WHERE id_contract=2;
```

---

# 👁️ 6. CREACIÓN DE VISTAS

Guardar como: `05_vistas.sql`

```sql
-- Vista de negocio
CREATE VIEW vista_negocio_servicios AS
SELECT u.email, s.service_name, p.amount
FROM user u
JOIN contract c ON u.id_user=c.id_user
JOIN service s ON c.id_service=s.id_service
LEFT JOIN payment p ON c.id_contract=p.id_contract;

-- Vista de seguridad
CREATE VIEW vista_seguridad_usuarios AS
SELECT u.email, c.username, c.status
FROM user u
JOIN credential c ON u.id_user=c.id_user;

-- Vista de auditoría
CREATE VIEW vista_auditoria_accesos AS
SELECT u.email, a.access_time, a.result
FROM access_audit a
JOIN user u ON a.id_user=u.id_user;
```
