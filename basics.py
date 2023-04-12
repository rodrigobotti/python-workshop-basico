# ***************************
# **    ASSUNTOS GERAIS    **
# ***************************

# - a linguagem tem o que é chamado de "indentação significativa" -- blocos são definidos via indentação diferentemente do java que define via chaves { }
# - os espaços de indentação são por padrão "tab de 4 espaços" -- é possível mudar, mas não se pode misturar tamanhos diferentes no mesmo projeto, isso causa erro de execução
# - tudo no python são objetos, incluindo tipos primitivos, funções, métodos e classes
# - arquivos python são chamados de módulos. diferentemente do java, um arquivo não precisa definir uma classe. você pode ter múltiplas classes e funções soltas. é equivalente a como é feito em javascript, mas você não precisa exportar as coisas, **tudo** é exportado.
# - é possível fazer strings dinâmicas usando interpolação. é possível fazer via concatenação usando `+` igual o java, mas não precisa -- f"Olá, {name}!"


def print_section(title: str):
    border = "*" * (len(title) + 12)
    print(f"\n{border}\n**    {title.upper()}    **\n{border}\n")


def print_divider():
    print("-" * 100)


# ************************************
# **    RESUMO CLASSES E OBJETOS    **
# ************************************

print_section("resumo classes e objetos")


class User:
    # note que atributos não tem modificadores de visibilidade (`private, protected, public`).
    # Diferentemente do `java` todos os atributos de um objeto em python são publicos!
    # existe uma convenção de se colocar _ no começo de atributos que devem ser tratados como privados
    # exemplo _username, mas isso **não faz o atributo ser privado!** isso só sinaliza pra quem está usando o objeto que
    # "ow, esse atributo aqui não foi feito pra ser usado diretamente hein...faz isso não!"
    # mas nada da linguagem garante que isso vai ser respeitado
    id: int
    username: str
    is_admin: bool

    # construtor: precisa se chamar __init__
    # precisa receber como primeiro argumento o `self`
    # o `self` é exatamente a mesma coisa que o `this` do java
    # mas diferentemente do java, ele não é implicito, você precisa definir o método recebendo ele como parâmetro para usá-lo
    def __init__(self, id: int, username: str, is_admin: bool):
        self.id = id
        self.is_admin = is_admin
        self.username = username
        # note que não precisa declarar o atributo ali no corpo da classe
        # bata setar no self aqui no construtor
        self.display_name = f"{self.id} {self.username}"

    # método especial que pode ser reescrito por qualquer classe
    # equivalente ao `toString` do java
    # note que diferentemente do java não precisa dizer que está fazendo override `@Override`
    # (não é exatamente equivalente ao `toString`, para mais informações sugiro pesquisar sobre os métodos __str__ e __repr__)
    def __repr__(self) -> str:
        return f"User(id={self.id},username={self.username},is_admin={self.is_admin})"

    def metodo_de_exemplo(self, admin_increment: int):
        if self.is_admin:
            print(f"Sou admin: id+{admin_increment} = {self.id + admin_increment}")
        else:
            print("Não sou admin :(")


# herança: aqui é equivalente ao `class AnonymousUser extends User` do java
class AnonymousUser(User):
    def __init__(self):
        super().__init__(id=0, username="anonimous", is_admin=False)

    # note que diferentemente do java não precisa dizer que está fazendo override `@Override`
    def metodo_de_exemplo(self, admin_increment: int):
        super().metodo_de_exemplo(admin_increment)
        print("Sou anonimo!")


# instanciando:
a_user = User(id=1, username="bora@ze", is_admin=True)
anom_user = AnonymousUser()

print("a_user: {a_user}")
print("anom_user: {anom_user}")

# invocando métodos
a_user.metodo_de_exemplo(3)
anom_user.metodo_de_exemplo(admin_increment=2)

# **********************
# **    DECORATORS    **
# **********************

print_section("decorators")

# 1 - Decorator que quando aplicado faz `printar` os argumentos e o retorno da função decorada


# recebe uma funcao como argumento
# retorna uma nova funcao como retorno
def loga_tudo(fn):
    # fn é a função que está sendo decorada, ou seja, é a função que vai ter o @logo_tudo escrito em cima dela

    def decorada(*args, **kargs):
        print(f"[decorada]: argumentos são {args} e {kargs}")

        # invocando a função decorada
        # note que poderiamos manipular tanto os argumentos passados para ela
        # quanto o valor que ela retorna
        resultado = fn(*args, **kargs)

        print(f"[decorada]: resultado é {resultado}")

        return resultado

    # retornando a função
    return decorada


@loga_tudo
def add(a, b):
    print("estou dentro do add!")
    return a + b


print_divider()
add(1, 2)

print_divider()
add(b=2, a=1)

print_divider()
add(1, b=2)

# 2 - Decorator que quando aplicado faz `printar` os argumentos e o retorno da função decorada
# o decorator deve receber como parametro uma `label` que deve ser usada nas mensagens printadas


def loga_tudo_com_label(label: str):
    # como é um decorator parametrizado
    # aqui rola um pulo do gato...
    # o que temos que retornar é [... bateria ...] um outro decorator [... barulho de explosão no fundo ...]
    # logo temos uma função que:
    # - recebe uma label como argumento
    # - retorna uma função que:
    #   - recebe uma função como argumento
    #   - retorna uma função
    # [... outro barulho de explosão ...]

    def parametrizada(fn):
        def decorada(*args, **kargs):
            print(f"[{label}]: argumentos são {args} e {kargs}")

            # invocando a função decorada
            # note que poderiamos manipular tanto os argumentos passados para ela
            # quanto o valor que ela retorna
            resultado = fn(*args, **kargs)

            print(f"[{label}]: resultado é {resultado}")

            return resultado

        return decorada

    # retornando o decorator interno
    return parametrizada


@loga_tudo_com_label("multiplicação maneira")
def mult(a, b):
    return a * b


print_divider()
mult(2, 3)

print_divider()
mult(b=2, a=3)

print_divider()
mult(2, b=3)

# **************************
# **    COMPREHENSIONS    **
# **************************

print_section("comprehensions")

all_users = [
    User(id=1, username="aaaa@mail.com", is_admin=True),
    User(id=2, username="bbbb@mail.com", is_admin=False),
    User(id=3, username="cccc@mail.com", is_admin=True),
    User(id=4, username="dddd@mail.com", is_admin=False),
    User(id=5, username="eeee@mail.com", is_admin=True),
    AnonymousUser(),
    AnonymousUser(),
]

# 1 - lista do display_name de todos usuarios admin
admin_usernames = [
    user.display_name  # valor projetado: pega propriedade `username`
    for user in all_users  # iteração: para cada `user` da lista `all_users`
    if user.is_admin  # filtro
]

print_divider()
print(f"admin_usernames: {admin_usernames}")

# equivalente a:
admin_usernames = []
for user in all_users:
    if user.is_admin:
        admin_usernames.append(user.username)

print_divider()
print(f"admin_usernames: {admin_usernames}")

# 2 - dicionário de id para username para os usuarios que não são admin
non_admin_map = {user.id: user.username for user in all_users if not user.is_admin}

print_divider()
print(f"non_admin_map: {non_admin_map}")

# equivalente a:
non_admin_map = dict()
for user in all_users:
    if not user.is_admin:
        non_admin_map[user.id] = user.username

print_divider()
print(f"non_admin_map: {non_admin_map}")

# 3 - set (conjunto) dos ids de todos usuários
ids = {user.id for user in all_users}

print_divider()
print(f"ids: {ids}")

# equivalente a:
ids = set()
for user in all_users:
    ids.add(user.id)

print_divider()
print(f"ids: {ids}")

# executando esse arquivo, veremos o seguinte print:
#
# ************************************
# **    RESUMO CLASSES E OBJETOS    **
# ************************************
#
# a_user: {a_user}
# anom_user: {anom_user}
# Sou admin: id+3 = 4
# Não sou admin :(
# Sou anonimo!
#
# **********************
# **    DECORATORS    **
# **********************
#
# ----------------------------------------------------------------------------------------------------
# [decorada]: argumentos são (1, 2) e {}
# estou dentro do add!
# [decorada]: resultado é 3
# ----------------------------------------------------------------------------------------------------
# [decorada]: argumentos são () e {'b': 2, 'a': 1}
# estou dentro do add!
# [decorada]: resultado é 3
# ----------------------------------------------------------------------------------------------------
# [decorada]: argumentos são (1,) e {'b': 2}
# estou dentro do add!
# [decorada]: resultado é 3
# ----------------------------------------------------------------------------------------------------
# [multiplicação maneira]: argumentos são (2, 3) e {}
# [multiplicação maneira]: resultado é 6
# ----------------------------------------------------------------------------------------------------
# [multiplicação maneira]: argumentos são () e {'b': 2, 'a': 3}
# [multiplicação maneira]: resultado é 6
# ----------------------------------------------------------------------------------------------------
# [multiplicação maneira]: argumentos são (2,) e {'b': 3}
# [multiplicação maneira]: resultado é 6
#
# **************************
# **    COMPREHENSIONS    **
# **************************
#
# ----------------------------------------------------------------------------------------------------
# admin_usernames: ['1 aaaa@mail.com', '3 cccc@mail.com', '5 eeee@mail.com']
# ----------------------------------------------------------------------------------------------------
# admin_usernames: ['aaaa@mail.com', 'cccc@mail.com', 'eeee@mail.com']
# ----------------------------------------------------------------------------------------------------
# non_admin_map: {2: 'bbbb@mail.com', 4: 'dddd@mail.com', 0: 'anonimous'}
# ----------------------------------------------------------------------------------------------------
# non_admin_map: {2: 'bbbb@mail.com', 4: 'dddd@mail.com', 0: 'anonimous'}
# ----------------------------------------------------------------------------------------------------
# ids: {0, 1, 2, 3, 4, 5}
# ----------------------------------------------------------------------------------------------------
# ids: {0, 1, 2, 3, 4, 5}
