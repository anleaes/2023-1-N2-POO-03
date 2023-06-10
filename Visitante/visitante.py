class Visitante:
    def __init__(self, nome, cpf, numero_celular):
        self.nome = nome
        self.cpf = cpf
        self.numero_celular = numero_celular

# Criação do objeto visitante
visitante = Visitante("João", "123456789", "987654321")

# Exemplo de uso dos atributos do objeto
print("Nome:", visitante.nome)
print("CPF:", visitante.cpf)
print("Número de celular:", visitante.numero_celular)