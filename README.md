# 🧩 Mini-CRM com Flask e Programação Orientada a Objetos

Um **Mini-CRM (Customer Relationship Management)** desenvolvido em **Python + Flask**, aplicando os princípios da **Programação Orientada a Objetos (POO)** — com **herança, polimorfismo, atributos e métodos**.

O projeto conta com uma **interface web simples** para cadastrar, visualizar e gerenciar **clientes** e **funcionários**.

---

## 🚀 Funcionalidades

- ✅ Cadastrar **clientes** e **funcionários**
- 📋 Listar todos os cadastros
- 🔍 Buscar pessoas pelo nome (na versão com backend em POO)
- 💡 Aplicação dos conceitos de **Herança** e **Polimorfismo**
- 🌐 Interface web desenvolvida com **Flask** e **Bootstrap**

---

## 🧱 Estrutura do Projeto
- `app.py`: Aplicação principal Flask.
- `models.py`: Classes e lógica orientada a objetos.
- `templates/`:
    - `base.html`: Template base (layout principal).
    - `index.html`: Página inicial (lista de cadastros).
    - `add.html`: Formulário para adicionar novo cadastro.

---

## 🧠 Conceitos de POO Utilizados
Conceito       | Implementação
---------------|---------------------------------------------------------------------------
Classe Base    | Pessoa
Herança	       | Cliente(Pessoa) e Funcionario(Pessoa)
Polimorfismo   | Método exibir_informacoes( ) com comportamento diferente em cada subclasse
Encapsulamento | Atributos acessados apenas por meio de métodos das classes
Abstração      | Representação simplificada de entidades do mundo real

---

## 🎨 Tecnologias Utilizadas

- Python 3.10+
- Flask
- HTML5 + Bootstrap 5
- Orientação a Objetos (POO)

---

## 🖼️ Capturas de Tela (opcional)
