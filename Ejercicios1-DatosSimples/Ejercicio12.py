#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene
#un descuento del 60%. Escribir un programa que comience leyendo el número de
#barras vendidas que no son del día. Después el programa debe mostrar el precio
#habitual de una barra de pan, el descuento que se le hace por no ser fresca y el
#coste final total.
PanVendido = (int(input("¿Cuantas barras de pan de ayer se han vendido? ")))
PVP = float(3.49)
PanAnterior = (PVP-(3.49*0.6))
PrecioTotal = (round(PanAnterior*PanVendido),2)
Redondeo = (round(PanVendido,2))
print("El precio normal del pan es de ", PVP, "€, pero al no ser del dia se hace un 60% de descuento por lo que el precio de la barra de pan seria", Redondeo, "€ y el precio total de las ganancias de esto panes ha sido de: ", PrecioTotal,"€" )