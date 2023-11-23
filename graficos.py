import matplotlib.pyplot as plt

#primeiro gráfico
x = [2,3,4,5,6,7,8,9]
y = [9,2,8,3,7,4,6,5]

plt.plot(x,y, color="green")
plt.scatter(x,y, color ="red")
plt.title("Evolução das vendas")
plt.xlabel("Tempo")
plt.ylabel("Vendas")
plt.legend(["Previsão","Verificado"])
plt.grid()

plt.show()

#segundo gráfico
x = [2,3,4,5,6,7,8,9]
y = [9,2,8,3,7,4,6,5]

plt.plot(x, y, "b--")
plt.scatter(x, y, marker="*", color="red")
plt.title("Evolução das vendas")
plt.xlabel("Tempo")
plt.ylabel("Vendas")
plt.legend(["Previsão","Verificado"])
plt.grid()

plt.show()

#terceiro gráfico
x = [1,2,3,4,5,6,7,8,9]
y1 = [1,3,5,3,1,3,5,3,1]
y2 = [2,4,6,4,2,4,6,4,2]

plt.plot(x, y2, color="blue", label="Produção")
plt.plot(x, y1, color="orange", label="Demanda")

plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.title("Produção e demanda ao longo do tempo")

plt.legend()
plt.show()

#quarto gráfico
x = [2,3,4,5,6,7,8,9]
y = [9,2,8,3,7,4,6,5]

plt.plot(x,y, color="black")
plt.bar(x,y, color ="gray")
plt.title("Evolução das vendas")

plt.show()

#quinto gráfico
x1 = [1,3,4,5,6,7,9]
y1 = [4,7,2,4,7,8,3]

x2 = [2,4,6,8,10]
y2 = [5,6,2,6,2]

plt.bar(x1, y1, label="Empresa A", color="blue")
plt.bar(x2, y2, label="Empresa B", color="green")
plt.plot()

plt.xlabel("Indice de satisfação")
plt.ylabel("Número de clientes")
plt.title("Comparativo de desempenho entre empresas")
plt.legend()

plt.show()
