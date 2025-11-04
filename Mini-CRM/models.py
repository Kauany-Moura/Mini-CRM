# ==============================================
# models.py — Lógica Orientada a Objetos do Mini-CRM
# ==============================================

class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def exibir_informacoes(self):
        return f"{self.nome} ({self.email})"


class Cliente(Pessoa):
    def __init__(self, nome, email, telefone, empresa, status="Ativo"):
        super().__init__(nome, email, telefone)
        self.empresa = empresa
        self.status = status

    def exibir_informacoes(self):
        return f"[CLIENTE] {self.nome} - {self.empresa} ({self.status})"


class Funcionario(Pessoa):
    def __init__(self, nome, email, telefone, cargo):
        super().__init__(nome, email, telefone)
        self.cargo = cargo

    def exibir_informacoes(self):
        return f"[FUNCIONÁRIO] {self.nome} - {self.cargo}"


class CRM:
    def __init__(self):
        self.cadastros = []

    def adicionar_pessoa(self, pessoa):
        self.cadastros.append(pessoa)

    def listar_cadastros(self):
        return self.cadastros

    def buscar_por_nome(self, nome):
        return [p for p in self.cadastros if nome.lower() in p.nome.lower()]
