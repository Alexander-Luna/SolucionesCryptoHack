
# 🛡️ Soluciones CryptoHack

[![GitHub Last Commit](https://img.shields.io/github/last-commit/alexander-luna/solucionescryptohack)](https://github.com/Alexander-Luna/SolucionesCryptoHack)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
![License](https://img.shields.io/badge/License-MIT-green)

Este repositorio contiene soluciones a los desafíos de [CryptoHack](https://cryptohack.org/), una plataforma educativa que te ayuda a aprender y dominar conceptos fundamentales de criptografía.

> 💡 **Nota:** Este repositorio está diseñado con fines educativos. Se recomienda intentar resolver los desafíos por tu cuenta antes de revisar las soluciones.

**Autor:** [Alexander Luna](https://github.com/Alexander-Luna)  

<img src="https://cryptohack.org/static/img/main.png" width="300" align="right" alt="CryptoHack Logo">

---

## 📋 Contenidos
- [Requisitos](#requisitos)
- [Configuración](#configuración)
- [Estructura del Repositorio](#estructura-del-repositorio)
- [Desafíos Resueltos](#desafíos-resueltos)
- [Contribuir](#contribuir)
- [Licencia](#licencia)

---

## ⚙️ Requisitos

Antes de comenzar, asegúrate de tener instalados los siguientes componentes en tu máquina:

- **Python 3.8+**: Recomendado para compatibilidad.
- **pip**: Para gestionar las dependencias del proyecto.
- **Git**: Para clonar el repositorio.

---

## 🚀 Configuración

Sigue estos pasos para configurar el proyecto en tu máquina local:

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/Alexander-Luna/SolucionesCryptoHack.git
   cd tu-repositorio
   ```

2. **Crea un entorno virtual:**
   ```bash
   python3 -m venv myenv
   ```

3. **Activa el entorno virtual:**
   - **Linux/macOS:**
     ```bash
     source myenv/bin/activate
     ```
   - **Windows:**
     ```bash
     .\myenv\Scripts\activate
     ```

4. **Instala las dependencias necesarias:**
   ```bash
   pip install -r requirements.txt
   ```

5. **¡Listo!** Ahora puedes explorar las soluciones en el repositorio.

---

## 📁 Estructura del Repositorio

El repositorio está organizado de la siguiente manera:

```plaintext
├── solutions/
│   ├── 1_Introduction/
│   │   ├── 1_Theme1
│   │   │   ├── Solucion1.py
│   │   │   ├── Solucion2.py
│   │   │   └── SolucionN.py
│   │   ├── 2_Theme2
│   │   │   ├── Solucion1.py
│   │   │   ├── Solucion2.py
│   │   │   └── SolucionN.py
│   │   ├── N_ThemeN
│   │   │   ├── Solucion1.py
│   │   │   ├── Solucion2.py
│   │   │   └── SolucionN.py
│   ├── 2_General/
│   │   ├── 1_Theme1
│   │   │   ├── Solucion1.py
│   │   │   ├── Solucion2.py
│   │   │   └── SolucionN.py
│   │   ├── 2_Theme2
│   │   │   ├── Solucion1.py
│   │   │   ├── Solucion2.py
│   │   │   └── SolucionN.py
│   │   ├── N_ThemeN
│   │   │   ├── Solucion1.py
│   │   │   ├── Solucion2.py
│   │   │   └── SolucionN.py
│   └── 3_SymmetricCiphers/
│   │   ├── 1_Theme1
│   │   │   ├── Solucion1.py
│   │   │   ├── Solucion2.py
│   │   │   └── SolucionN.py
│   │   ├── 2_Theme2
│   │   │   ├── Solucion1.py
│   │   │   ├── Solucion2.py
│   │   │   └── SolucionN.py
│   │   ├── N_ThemeN
│   │   │   ├── Solucion1.py
│   │   │   ├── Solucion2.py
│   │   │   └── SolucionN.py
├── requirements.txt
├── LICENSE
└── README.md
```

### Carpetas principales:
- **solutions/**: Contiene subcarpetas para cada categoría de desafíos (Introducción, Cifrado Clásico, Criptografía Moderna, etc.).
- **tests/**: Pruebas automatizadas para verificar las soluciones.
- **requirements.txt**: Lista de dependencias necesarias para ejecutar las soluciones.

---

## 🧩 Desafíos Resueltos

Este repositorio abarca las siguientes categorías de desafíos de CryptoHack:

1. **Introducción**
   - XOR básico
   - Aritmética modular

2. **Cifrado Clásico**
   - Cifrado César
   - Cifrado Vigenère

3. **Criptografía Moderna**
   - RSA
   - Curvas elípticas

*Se irán añadiendo más soluciones periódicamente. ¡Mantente atento a nuevas actualizaciones!*

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Si deseas contribuir, sigue estos pasos:

1. Haz un fork de este repositorio.
2. Crea una rama para tu característica o corrección de errores:
   ```bash
   git checkout -b feature/nueva-caracteristica
   ```
3. Realiza tus cambios y confirma los commits:
   ```bash
   git commit -m "Agrega nueva característica"
   ```
4. Haz un push de tus cambios al repositorio remoto:
   ```bash
   git push origin feature/nueva-caracteristica
   ```
5. Abre un Pull Request en el repositorio principal.

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo [LICENSE](LICENSE) para más información.

---

Si tienes sugerencias o encuentras algún error, no dudes en abrir un [issue](https://github.com/Alexander-Luna/SolucionesCryptoHack/issues). 😊