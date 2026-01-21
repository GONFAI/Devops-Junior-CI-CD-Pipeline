![CI](https://github.com/GONFAI/devops-junior-ci-cd-pipeline/actions/workflows/ci.yml/badge.svg)

# 🚀 DevOps Learning Project – From Zero to CI/CD

Este repositorio documenta mi proceso de aprendizaje práctico en **DevOps**, desde los **fundamentos** hasta la implementación de **automatización, contenedores y pipelines CI/CD**, utilizando **herramientas gratuitas y open-source**.

El objetivo principal es **aprender haciendo**, aplicando buenas prácticas reales usadas en equipos DevOps.

---

## 🎯 Objetivo del Proyecto

* Entender el flujo completo **Dev → Build → Test → Deploy**
* Aplicar fundamentos DevOps antes de automatizar
* Construir un proyecto real que pueda mostrarse en GitHub
* Prepararme para un **rol DevOps Junior**

---

## 🧠 ¿Qué hace este proyecto?

Este proyecto implementa un flujo **DevOps** real a partir de una aplicación sencilla, enfocándose en la automatización y validación continua:

* Aplicación **Flask** con endpoints básicos:
  * `/` → estado de la aplicación
  * `/health` → health check
* Pruebas automatizadas con **pytest**
* Imagen **Docker multi-stage**
* Ejecución de pruebas **durante el build de Docker**
* Pipeline de **CI con GitHub Actions**
* Ejecución local usando **Docker** y **Docker Compose**
* Imagen publicada en **Docker Hub**

---

## 🧱 Alcance (Roadmap)

Este proyecto se desarrollará por fases:

### ✅ Fase 1 – Fundamentos

* Control de versiones con Git
* Flujo de trabajo con ramas
* Documentación clara (README)

### ⏳ Fase 2 – Contenedores

* Crear una aplicación simple
* Dockerizar la aplicación
* Ejecutarla localmente con Docker
* Orquestación local con Docker Compose

### ⏳ Fase 3 – CI/CD

* Pipeline con GitHub Actions
* Ejecución automática de pruebas
* Build automático de imagen Docker
* Validación continua en cada push y pull request

### ⏳ Fase 4 – Cloud (opcional)

* Simulación de despliegue
* Infraestructura como código (conceptual)

---

## 🔄 Flujo CI/CD Implementado

graph LR
A[Code] --> B[GitHub]
B --> C[GitHub Actions]
C --> D[Tests]
D --> E[Build Docker Image]
E --> F[Push to Docker Hub]
F --> G[Docker Compose Runtime]

## Detalle del flujo:
1. Push o Pull Request al repositorio
2. GitHub Actions ejecuta automáticamente:
   * Checkout del código
   * Instalación de dependencias
   * Ejecución de pruebas automatizadas (pytest)
   * Build de la imagen Docker (Buildx + cache)
3. El pipeline falla si alguna validación no se cumple

---

## 🛠️ Tecnologías (en progreso)

* Git & GitHub
* Docker (multi-stage builds)
* Docker Compose
* GitHub Actions (CI)
* Python / Flask
* Pytest
* Bash / Shell scripting
* Linux
* Cloud (conceptos)

---

## 📂 Estructura del Proyecto (actual)

```
.
├── README.md
├── app/ # Aplicación Flask
├── tests/ # Pruebas automatizadas
├── docker/ # Dockerfile multi-stage
├── docker-compose.yml # Orquestación local
├── scripts/ # Scripts de automatización
└── .github/workflows/ # Pipelines CI/CD
```

---

## ▶️ Ejecución Local

Ejecutar la aplicación usando Docker Compose:
bash
docker compose up --build

La aplicación quedará disponible en:

http://localhost:5000
http://localhost:5000/health

---

## 📚 Recursos Gratuitos Utilizados

* Documentación oficial
* GitHub Docs
* Docker Docs
* Laboratorios gratuitos
* Práctica local

---

## 👨‍💻 Autor

**Jose David Gonzalez Mendoza**
DevOps Junior en formación
📍 Aprendizaje autodidacta y práctico

---

## ⭐ Estado del Proyecto

🟢 Funcional — en evolución para agregar despliegue y cloud
