"""La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en
función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes
que lleva."""
extra ="mozarrella y tomate"

pizza = input("¿Deseas una pizza vegetariana?  s(si), n(no) ")

if pizza == "s":
    ingredientesv=input("Elige uno de los ingredinetes disponibles:\n  p(pimiento) t(tofu): ")
    if ingredientesv =='p':
        print(f"Tus ingredinetes son Pimiento, {extra}")
    elif ingredientesv == 't':
        print(f"Tus ingredinetes son Tofu, {extra}")
    else:
        print("Ingrediente incorrecto, intente de nuevo")

if pizza == "n":
    ingredientesv=input("Elige uno de los ingredinetes disponibles:\n  p(peperoni) j(jamon) s(salmon): ")
    if ingredientesv =='p':
        print(f"Tus ingredinetes son Peperoni, {extra}")
    elif ingredientesv == 'j':
        print(f"Tus ingredinetes son Jamon, {extra}")
    elif ingredientesv == 's':
        print(f"Tus ingredinetes son Salmon, {extra}")
    else:
        print("Ingrediente incorrecto, intente de nuevo")
    