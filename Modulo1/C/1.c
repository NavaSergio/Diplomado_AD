/*
 * Tema 1: Instalación de un Entorno de Desarrollo en C
 *
 * Este programa de ejemplo muestra cómo instalar y configurar un entorno de desarrollo en C
 * en diferentes sistemas operativos (Windows, macOS, Linux).
 *
 * Autor: Jose Jesus Rocha Quezada   -  chuche@cimat.mx
 * Modulo 1: Introducción a C  - Tronco Comun
 */


// Comentario en una línea
#include <stdio.h> // El comentario funciona también al final de la línea 

// Función para instalar y configurar GCC en Windows
void instalar_gcc_windows() {
    printf("Instalando GCC en Windows...\n");
    printf("1. Descargar MinGW desde https://sourceforge.net/projects/mingw/\n");
    printf("2. Instalar MinGW siguiendo las instrucciones del instalador.\n");
    printf("3. Configurar las variables de entorno:\n");
    printf("   - Agregar la ruta de MinGW (por ejemplo, C:\\MinGW\\bin) a la variable de entorno PATH.\n");
    printf("4. Verificar la instalación:\n");
    printf("   - Abrir la línea de comandos y ejecutar 'gcc --version'.\n");
    printf("GCC instalado y configurado correctamente en Windows.\n");
}

// Función para instalar y configurar GCC en macOS
void instalar_gcc_macos() {
    printf("Instalando GCC en macOS...\n");
    printf("1. Verificar si GCC ya está instalado:\n");
    printf("   - Abrir la terminal y ejecutar 'gcc --version'.\n");
    printf("2. Si no está instalado, instalar Xcode Command Line Tools:\n");
    printf("   - Ejecutar 'xcode-select --install' en la terminal.\n");
    printf("3. Verificar la instalación:\n");
    printf("   - Ejecutar 'gcc --version' en la terminal.\n");
    printf("GCC instalado y configurado correctamente en macOS.\n");
}

// Función para instalar y configurar GCC en Linux
void instalar_gcc_linux() {
    printf("Instalando GCC en Linux...\n");
    printf("1. Verificar si GCC ya está instalado:\n");
    printf("   - Abrir la terminal y ejecutar 'gcc --version'.\n");
    printf("2. Si no está instalado, instalar GCC usando el gestor de paquetes:\n");
    printf("   - Ejecutar 'sudo apt-get install gcc' en Ubuntu.\n");
    printf("3. Verificar la instalación:\n");
    printf("   - Ejecutar 'gcc --version' en la terminal.\n");
    printf("GCC instalado y configurado correctamente en Linux.\n");
}

// Función para configurar un IDE en Windows
void configurar_ide_windows() {
    printf("Configurando un IDE en Windows...\n");
    printf("1. Descargar e instalar Code::Blocks desde http://www.codeblocks.org/downloads\n");
    printf("2. Configurar Code::Blocks para usar GCC:\n");
    printf("   - En Code::Blocks, ir a Settings > Compiler y seleccionar 'GNU GCC Compiler'.\n");
    printf("3. Verificar la configuración:\n");
    printf("   - Crear un nuevo proyecto y compilar un programa simple.\n");
    printf("IDE configurado correctamente en Windows.\n");
}

// Función para configurar un IDE en macOS
void configurar_ide_macos() {
    printf("Configurando un IDE en macOS...\n");
    printf("1. Descargar e instalar Xcode desde la App Store.\n");
    printf("2. Configurar Xcode para usar GCC:\n");
    printf("   - En Xcode, crear un nuevo proyecto y seleccionar 'Command Line Tool'.\n");
    printf("3. Verificar la configuración:\n");
    printf("   - Compilar y ejecutar un programa simple.\n");
    printf("IDE configurado correctamente en macOS.\n");
}

// Función para configurar un IDE en Linux
void configurar_ide_linux() {
    printf("Configurando un IDE en Linux...\n");
    printf("1. Descargar e instalar Visual Studio Code desde https://code.visualstudio.com/\n");
    printf("2. Instalar la extensión de C/C++ en VS Code:\n");
    printf("   - En VS Code, ir a Extensions y buscar 'C/C++'.\n");
    printf("3. Configurar VS Code para usar GCC:\n");
    printf("   - Crear un archivo de configuración 'tasks.json' para compilar con GCC.\n");
    printf("4. Verificar la configuración:\n");
    printf("   - Compilar y ejecutar un programa simple.\n");
    printf("IDE configurado correctamente en Linux.\n");
}

int main() {
    printf("Instalación y configuración de un entorno de desarrollo en C\n");

    // Instalación de GCC en diferentes sistemas operativos
    instalar_gcc_windows();
    instalar_gcc_macos();
    instalar_gcc_linux();

    // Configuración de un IDE en diferentes sistemas operativos
    configurar_ide_windows();
    configurar_ide_macos();
    configurar_ide_linux();

    printf("Proceso de instalación y configuración completado.\n");
    return 0;
}