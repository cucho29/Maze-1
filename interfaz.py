import tkinter as tk
import mysql.connector
from tkinter import font
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
  
# Lista de usuarios válidos
usuarios_validos = ["Luz", "Daniela", "Angel"]

# Función para verificar las credenciales de inicio de sesión
def verificar_credenciales():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    
    if usuario in usuarios_validos and contrasena == "contraseña":
        mostrar_interfaz_principal()
    else:
        messagebox.showerror("Error", "Credenciales incorrectas")

def mostrar_codigo_postal():
    ventana_codigo_postal = tk.Tk()
    ventana_codigo_postal.title("Módulo de Código Postal")
    ventana_codigo_postal.configure(bg="#FFC7A8")

    etiqueta_codigo_postal = tk.Label(ventana_codigo_postal, text="Código Postal:")
    etiqueta_codigo_postal.pack()
    entrada_codigo_postal = tk.Entry(ventana_codigo_postal)
    entrada_codigo_postal.pack()

    etiqueta_ciudad = tk.Label(ventana_codigo_postal, text="Ciudad:")
    etiqueta_ciudad.pack()
    entrada_ciudad = tk.Entry(ventana_codigo_postal)
    entrada_ciudad.pack()

    etiqueta_estado = tk.Label(ventana_codigo_postal, text="Estado:")
    etiqueta_estado.pack()
    entrada_estado = tk.Entry(ventana_codigo_postal)
    entrada_estado.pack()

    def guardar_codigo_postal():
        zip = entrada_codigo_postal.get()
        z_city = entrada_ciudad.get()
        z_state = entrada_estado.get()
        
        consulta = "INSERT INTO zips (zip, z_city, z_state) VALUES (%s, %s, %s)"
        
        try:
            conexion, cursor = conectar()
            cursor.execute(consulta, (zip, z_city, z_state))
            conexion.commit()
            messagebox.showinfo("Éxito", "Código Postal, Ciudad y Estado guardados correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar los datos: {str(e)}")
        finally:
            if conexion:
                conexion.close()

    boton_guardar = tk.Button(ventana_codigo_postal, text="Guardar Datos", command=guardar_codigo_postal, bg="#A6E8FF")
    boton_guardar.pack()

    ventana_codigo_postal.mainloop()    

def mostrar_productos():
    ventana_productos = tk.Tk()
    ventana_productos.title("Módulo de Productos")
    ventana_productos.configure(bg="#FFC7A8")

    etiqueta_nombre_producto = tk.Label(ventana_productos, text="Nombre del Producto:")
    etiqueta_nombre_producto.pack()
    entrada_nombre_producto = tk.Entry(ventana_productos)
    entrada_nombre_producto.pack()

    etiqueta_marca_producto = tk.Label(ventana_productos, text="Marca del Producto:")
    etiqueta_marca_producto.pack()
    entrada_marca_producto = tk.Entry(ventana_productos)
    entrada_marca_producto.pack()

    etiqueta_descripcion_producto = tk.Label(ventana_productos, text="Descripción del Producto:")
    etiqueta_descripcion_producto.pack()
    entrada_descripcion_producto = tk.Entry(ventana_productos)
    entrada_descripcion_producto.pack()

    etiqueta_precio_producto = tk.Label(ventana_productos, text="Precio del Producto:")
    etiqueta_precio_producto.pack()
    entrada_precio_producto = tk.Entry(ventana_productos)
    entrada_precio_producto.pack()

    def guardar_producto():
        nombre_producto = entrada_nombre_producto.get()
        marca_producto = entrada_marca_producto.get()
        descripcion_producto = entrada_descripcion_producto.get()
        precio_producto = entrada_precio_producto.get()
        
        consulta = "INSERT INTO products (p_name, p_brand, p_descrip, p_price) VALUES (%s, %s, %s, %s)"
        
        try:
            conexion, cursor = conectar()
            cursor.execute(consulta, (nombre_producto, marca_producto, descripcion_producto, precio_producto))
            conexion.commit()
            messagebox.showinfo("Éxito", "Producto guardado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar el producto: {str(e)}")
        finally:
            if conexion:
                conexion.close()

    boton_guardar = tk.Button(ventana_productos, text="Guardar Producto", command=guardar_producto, bg="#A6E8FF")
    boton_guardar.pack()

    ventana_productos.mainloop()

    ver_grafico_productos_precios()


def mostrar_clientes():
    ventana_clientes = tk.Tk()
    ventana_clientes.title("Módulo de Clientes")
    ventana_clientes.configure(bg="#FFC7A8")

    etiqueta_nombre_cliente = tk.Label(ventana_clientes, text="Primer Nombre del Cliente:")
    etiqueta_nombre_cliente.pack()
    entrada_nombre_cliente = tk.Entry(ventana_clientes)
    entrada_nombre_cliente.pack()

    etiqueta_apellido1_cliente = tk.Label(ventana_clientes, text="Primer Apellido del Cliente:")
    etiqueta_apellido1_cliente.pack()
    entrada_apellido1_cliente = tk.Entry(ventana_clientes)
    entrada_apellido1_cliente.pack()

    etiqueta_apellido2_cliente = tk.Label(ventana_clientes, text="Segundo Apellido del Cliente:")
    etiqueta_apellido2_cliente.pack()
    entrada_apellido2_cliente = tk.Entry(ventana_clientes)
    entrada_apellido2_cliente.pack()

    etiqueta_calle_cliente = tk.Label(ventana_clientes, text="Calle del Cliente:")
    etiqueta_calle_cliente.pack()
    entrada_calle_cliente = tk.Entry(ventana_clientes)
    entrada_calle_cliente.pack()

    etiqueta_no_exterior_cliente = tk.Label(ventana_clientes, text="Número Exterior del Cliente:")
    etiqueta_no_exterior_cliente.pack()
    entrada_no_exterior_cliente = tk.Entry(ventana_clientes)
    entrada_no_exterior_cliente.pack()

    etiqueta_no_interior_cliente = tk.Label(ventana_clientes, text="Número Interior del Cliente:")
    etiqueta_no_interior_cliente.pack()
    entrada_no_interior_cliente = tk.Entry(ventana_clientes)
    entrada_no_interior_cliente.pack()

    etiqueta_colonia_cliente = tk.Label(ventana_clientes, text="Colonia del Cliente:")
    etiqueta_colonia_cliente.pack()
    entrada_colonia_cliente = tk.Entry(ventana_clientes)
    entrada_colonia_cliente.pack()

    etiqueta_zip_cliente = tk.Label(ventana_clientes, text="Código Postal del Cliente:")
    etiqueta_zip_cliente.pack()
    entrada_zip_cliente = tk.Entry(ventana_clientes)
    entrada_zip_cliente.pack()

    etiqueta_correo_cliente = tk.Label(ventana_clientes, text="Correo Electrónico del Cliente:")
    etiqueta_correo_cliente.pack()
    entrada_correo_cliente = tk.Entry(ventana_clientes)
    entrada_correo_cliente.pack()

    etiqueta_telefono_cliente = tk.Label(ventana_clientes, text="Número de Teléfono del Cliente:")
    etiqueta_telefono_cliente.pack()
    entrada_telefono_cliente = tk.Entry(ventana_clientes)
    entrada_telefono_cliente.pack()

    def guardar_cliente():
        nombre_cliente = entrada_nombre_cliente.get()
        apellido1_cliente = entrada_apellido1_cliente.get()
        apellido2_cliente = entrada_apellido2_cliente.get()
        calle_cliente = entrada_calle_cliente.get()
        no_exterior_cliente = entrada_no_exterior_cliente.get()
        no_interior_cliente = entrada_no_interior_cliente.get()
        colonia_cliente = entrada_colonia_cliente.get()
        zip_cliente = entrada_zip_cliente.get()
        correo_cliente = entrada_correo_cliente.get()
        telefono_cliente = entrada_telefono_cliente.get()
        
        consulta = "INSERT INTO clients (c_fname, c_sname1, c_sname2, c_street, c_noext, c_noint, c_col, c_zip, c_email, c_phone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        try:
            conexion, cursor = conectar()
            cursor.execute(consulta, (nombre_cliente, apellido1_cliente, apellido2_cliente, calle_cliente, no_exterior_cliente, no_interior_cliente, colonia_cliente, zip_cliente, correo_cliente, telefono_cliente))
            conexion.commit()
            messagebox.showinfo("Éxito", "Datos del Cliente guardados correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar los datos del Cliente: {str(e)}")
        finally:
            if conexion:
                conexion.close()

    boton_guardar = tk.Button(ventana_clientes, text="Guardar Cliente", command=guardar_cliente, bg="#A6E8FF")
    boton_guardar.pack()

    ventana_clientes.mainloop()

def mostrar_ordenes():
    ventana_ordenes = tk.Tk()
    ventana_ordenes.title("Módulo de Órdenes")
    ventana_ordenes.configure(bg="#FFC7A8")

    etiqueta_id_orden = tk.Label(ventana_ordenes, text="ID de la Orden:")
    etiqueta_id_orden.pack()
    entrada_id_orden = tk.Entry(ventana_ordenes)
    entrada_id_orden.pack()

    etiqueta_id_cliente = tk.Label(ventana_ordenes, text="ID del Cliente:")
    etiqueta_id_cliente.pack()
    entrada_id_cliente = tk.Entry(ventana_ordenes)
    entrada_id_cliente.pack()

    etiqueta_estado_orden = tk.Label(ventana_ordenes, text="Estado de la Orden:")
    etiqueta_estado_orden.pack()
    entrada_estado_orden = tk.Entry(ventana_ordenes)
    entrada_estado_orden.pack()

    etiqueta_fecha_orden = tk.Label(ventana_ordenes, text="Fecha de la Orden:")
    etiqueta_fecha_orden.pack()
    entrada_fecha_orden = tk.Entry(ventana_ordenes)
    entrada_fecha_orden.pack()

    etiqueta_total_orden = tk.Label(ventana_ordenes, text="Total de la Orden:")
    etiqueta_total_orden.pack()
    entrada_total_orden = tk.Entry(ventana_ordenes)
    entrada_total_orden.pack()

    def guardar_orden():
        id_orden = entrada_id_orden.get()
        id_cliente = entrada_id_cliente.get()
        estado_orden = entrada_estado_orden.get()
        fecha_orden = entrada_fecha_orden.get()
        total_orden = entrada_total_orden.get()

        consulta = "INSERT INTO orders (id_order, id_cliente, o_status, o_date, o_total) VALUES (%s, %s, %s, %s, %s)"
        
        try:
            conexion, cursor = conectar()
            cursor.execute(consulta, (id_orden, id_cliente, estado_orden, fecha_orden, total_orden))
            conexion.commit()
            messagebox.showinfo("Éxito", "Orden guardada correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar la orden: {str(e)}")
        finally:
            if conexion:
                conexion.close()

    boton_guardar = tk.Button(ventana_ordenes, text="Guardar Orden", command=guardar_orden, bg="#A6E8FF")
    boton_guardar.pack()

    ventana_ordenes.mainloop()

def mostrar_detalle_ordenes():
    ventana_detalle_ordenes = tk.Tk()
    ventana_detalle_ordenes.title("Módulo de Detalle de Órdenes")
    ventana_detalle_ordenes.configure(bg="#FFC7A8")

    etiqueta_id_orden = tk.Label(ventana_detalle_ordenes, text="ID de la Orden:")
    etiqueta_id_orden.pack()
    entrada_id_orden = tk.Entry(ventana_detalle_ordenes)
    entrada_id_orden.pack()

    etiqueta_id_producto = tk.Label(ventana_detalle_ordenes, text="ID del Producto:")
    etiqueta_id_producto.pack()
    entrada_id_producto = tk.Entry(ventana_detalle_ordenes)
    entrada_id_producto.pack()

    etiqueta_cantidad = tk.Label(ventana_detalle_ordenes, text="Cantidad del Producto:")
    etiqueta_cantidad.pack()
    entrada_cantidad = tk.Entry(ventana_detalle_ordenes)
    entrada_cantidad.pack()

    etiqueta_total = tk.Label(ventana_detalle_ordenes, text="Total de la Orden:")
    etiqueta_total.pack()
    entrada_total = tk.Entry(ventana_detalle_ordenes)
    entrada_total.pack()

    def guardar_detalle_orden():
        id_orden = entrada_id_orden.get()
        id_producto = entrada_id_producto.get()
        cantidad = entrada_cantidad.get()
        total = entrada_total.get()

        consulta = "INSERT INTO order_details (id_order, id_product, od_amount, od_total) VALUES (%s, %s, %s, %s)"
        
        try:
            conexion, cursor = conectar()
            cursor.execute(consulta, (id_orden, id_producto, cantidad, total))
            conexion.commit()
            messagebox.showinfo("Éxito", "Detalle de la Orden guardado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar el detalle de la orden: {str(e)}")
        finally:
            if conexion:
                conexion.close()

    boton_guardar = tk.Button(ventana_detalle_ordenes, text="Guardar Detalle de la Orden", command=guardar_detalle_orden, bg="#A6E8FF")
    boton_guardar.pack()

    ventana_detalle_ordenes.mainloop()

def ver_grafico_productos_precios():

    conexion = mysql.connector.connect(
        user="jc",
        password="jc123",
        host="localhost",
        database="farmacia2_db"
    )
    curso = conexion.cursor()

    query = "SELECT p_name, p_price FROM products"
    curso.execute(query)

    resultados = curso.fetchall()

    nombres_productos = [resultado[0] for resultado in resultados]
    precios_productos = [resultado[1] for resultado in resultados]

    colores = plt.cm.viridis(np.linspace(0, 1, len(nombres_productos)))  

    plt.figure(figsize=(12, 6))
    plt.bar(nombres_productos, precios_productos, color=colores)
    plt.xlabel("Nombre del Producto")
    plt.ylabel("Precio del Producto")
    plt.title("Precios de Productos")
    plt.xticks(rotation=90) 

    plt.tight_layout()
    plt.show()

def mostrar_grafico():
    ventana_grafico = tk.Tk()
    ventana_grafico.configure(bg="#FFC7A8")
    ventana_grafico.title("Gráfico de Precios de Productos")
    boton_ver_grafico = tk.Button(ventana_grafico, text="Ver Gráfico", command=ver_grafico_productos_precios, bg="#A6E8FF")
    boton_ver_grafico.pack()
    ventana_grafico.mainloop()

def ver_grafico_order_details():
    conexion = mysql.connector.connect(
        user="jc",
        password="jc123",
        host="localhost",
        database="farmacia2_db"
    )
    curso = conexion.cursor()

    query = "SELECT id_order, id_product, od_amount, od_total FROM order_details"
    curso.execute(query)

    resultados = curso.fetchall()

    id_order = [resultado[0] for resultado in resultados]
    id_product = [resultado[1] for resultado in resultados]
    od_amount = [resultado[2] for resultado in resultados]
    od_total = [resultado[3] for resultado in resultados]

    colores = plt.cm.viridis(np.linspace(0, 1, len(id_order)))

    plt.figure(figsize=(12, 6))
    plt.bar(id_order, od_total, color=colores)
    plt.xlabel("ID del Pedido")
    plt.ylabel("Total del Pedido")
    plt.title("Totales de Pedidos")
    plt.xticks(rotation=90)

    plt.tight_layout()
    plt.show()

def mostrar_grafico_order_details():
    ventana_grafico = tk.Tk()
    ventana_grafico.configure(bg="#FFC7A8")
    ventana_grafico.title("Gráfico de Total Gastado de Pedidos")
    boton_ver_grafico = tk.Button(ventana_grafico, text="Ver Gráfico", command=ver_grafico_order_details, bg="#A6E8FF")
    boton_ver_grafico.pack()
    ventana_grafico.mainloop()

def mostrar_interfaz_principal():
    ventana_inicio.destroy()  

    ventana_principal = tk.Tk()
    ventana_principal.title("Interfaz Principal")
    ventana_principal.geometry("800x600")
    ventana_principal.configure(bg="#FF768A") 

    etiqueta_bienvenida = tk.Label(ventana_principal, text="¡Bienvenido al sistema!", font=("Helvetica", 20))
    etiqueta_bienvenida.pack(pady=20)

    boton_codigo_postal = tk.Button(ventana_principal, text="Código Postal", command=mostrar_codigo_postal, bg="#1BEBFF")
    boton_codigo_postal.pack(pady=20)

    boton_productos = tk.Button(ventana_principal, text="Productos", command=mostrar_productos, bg="#1BEBFF")
    boton_productos.pack(pady=20)

    boton_clientes = tk.Button(ventana_principal, text="Clientes", command=mostrar_clientes, bg="#1BEBFF")
    boton_clientes.pack(pady=20)

    boton_ordenes = tk.Button(ventana_principal, text="Órdenes", command=mostrar_ordenes, bg="#1BEBFF")
    boton_ordenes.pack(pady=20)

    boton_ordenes = tk.Button(ventana_principal, text="Detalle de Ordenes", command=mostrar_detalle_ordenes, bg="#1BEBFF")
    boton_ordenes.pack(pady=20)  

    boton_ordenes = tk.Button(ventana_principal, text="Grafica de Productos", command=mostrar_grafico, bg="#1BEBFF")
    boton_ordenes.pack(pady=20)  

    boton_ordenes = tk.Button(ventana_principal, text="Grafica de Pedidos", command=mostrar_grafico_order_details, bg="#1BEBFF")
    boton_ordenes.pack(pady=20)    

    boton_cerrar_sesion = tk.Button(ventana_principal, text="Cerrar Sesión", command=ventana_principal.quit, bg="White")
    boton_cerrar_sesion.pack()

    ventana_principal.mainloop()

def conectar():
    try:
        conexion = mysql.connector.connect(user="jc", password="jc123",
                             host="localhost",
                            database='farmacia2_db',
                            port='3306')
        cursor = conexion.cursor()
        return conexion, cursor
        print("MySQL connection was successful!")
    except mysql.connector.Error as error:
         print("Failed to connect to MySQL:", error)
         return None,None

ventana_inicio = tk.Tk()
ventana_inicio.title("Inicio de Sesión")
ventana_inicio.geometry("400x300")
ventana_inicio.configure(bg="#FF768A")

label_usuario = tk.Label(ventana_inicio, text="Usuario:")
label_usuario.pack(pady=10)
entry_usuario = tk.Entry(ventana_inicio)
entry_usuario.pack(pady=5)

label_contrasena = tk.Label(ventana_inicio, text="Contraseña:")
label_contrasena.pack(pady=10)
entry_contrasena = tk.Entry(ventana_inicio, show="*")
entry_contrasena.pack(pady=5)

boton_iniciar_sesion = tk.Button(ventana_inicio, text="Iniciar Sesión", command=verificar_credenciales)
boton_iniciar_sesion.pack(pady=20)

ventana_inicio.mainloop()