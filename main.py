# ==============================================
# MINI-CRM ORIENTADO A OBJETOS
# ==============================================

# Classe base
class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def exibir_informacoes(self):
        """Método polimórfico que será sobrescrito pelas subclasses."""
        return f"Nome: {self.nome} | Email: {self.email} | Telefone: {self.telefone}"


# Subclasse Cliente
class Cliente(Pessoa):
    def __init__(self, nome, email, telefone, empresa, status="Ativo"):
        super().__init__(nome, email, telefone)
        self.empresa = empresa
        self.status = status

    def exibir_informacoes(self):
        """Sobrescrita do método da classe base."""
        return (f"[CLIENTE] {self.nome} | Empresa: {self.empresa} | "
                f"Status: {self.status} | Email: {self.email}")


# Subclasse Funcionario
class Funcionario(Pessoa):
    def __init__(self, nome, email, telefone, cargo):
        super().__init__(nome, email, telefone)
        self.cargo = cargo

    def exibir_informacoes(self):
        """Sobrescrita do método da classe base."""
        return (f"[FUNCIONÁRIO] {self.nome} | Cargo: {self.cargo} | "
                f"Email: {self.email}")


# Classe gerenciadora do CRM
class CRM:
    def __init__(self):
        self.cadastros = []

    def adicionar_pessoa(self, pessoa):
        self.cadastros.append(pessoa)
        print(f"{pessoa.nome} foi adicionado(a) ao sistema.")

    def listar_cadastros(self):
        print("\n=== LISTA DE CADASTROS ===")
        for pessoa in self.cadastros:
            print(pessoa.exibir_informacoes())

    def buscar_por_nome(self, nome):
        print(f"\n🔎 Buscando por: {nome}")
        encontrados = [p for p in self.cadastros if nome.lower() in p.nome.lower()]
        if encontrados:
            for p in encontrados:
                print(p.exibir_informacoes())
        else:
            print("Nenhum registro encontrado.")


# ==============================================
# TESTE DO SISTEMA
# ==============================================
if __name__ == "__main__":
    crm = CRM()

    # Criando clientes
    c1 = Cliente("Maria Silva", "maria@email.com", "99999-1111", "Tech Solutions")
    c2 = Cliente("João Pedro", "joao@email.com", "98888-2222", "EcoPower", status="Inativo")

    # Criando funcionários
    f1 = Funcionario("Ana Costa", "ana@empresa.com", "97777-3333", "Gerente de Contas")
    f2 = Funcionario("Carlos Lima", "carlos@empresa.com", "96666-4444", "Vendedor")

    # Adicionando ao CRM
    crm.adicionar_pessoa(c1)
    crm.adicionar_pessoa(c2)
    crm.adicionar_pessoa(f1)
    crm.adicionar_pessoa(f2)

    # Listando e buscando
    crm.listar_cadastros()
    crm.buscar_por_nome("carlos")
