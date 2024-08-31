class FSM:
    def __init__(self, estados, acoes, transicoes, estado_inicial):
        self.estados = estados
        self.acoes = acoes
        self.transicoes = transicoes
        self.estado_atual = estado_inicial

    def transition(self, estado, acao):
        if (estado, acao) in self.transicoes:
            return self.transicoes[(estado, acao)]
        return estado


fechado = 'Fechado'
aberto = 'Aberto'
trancado = 'Trancado'
em_uso = 'Em Uso'

eventos = ['inserir_chave', 'girar_chave', 'abrir_portao', 'fechar_portao', 'trancar_portao', 'destrancar_portao']

estado_inicial = fechado

def inserir_chave(estado):
    if estado == fechado:
        return 'Chave Inserida'
    return estado

def girar_chave(estado):
    if estado == 'Chave Inserida':
        return aberto
    elif estado == aberto:
        return trancado
    elif estado == trancado:
        return aberto
    return estado

def abrir_portao(estado):
    if estado == aberto:
        return em_uso
    return estado

def fechar_portao(estado):
    if estado == em_uso:
        return aberto
    return estado

def trancar_portao(estado):
    if estado == aberto:
        return trancado
    return estado

def destrancar_portao(estado):
    if estado == trancado:
        return aberto
    return estado

estados = {fechado, aberto, trancado, em_uso, 'Chave Inserida'}
acoes = {inserir_chave, girar_chave, abrir_portao, fechar_portao, trancar_portao, destrancar_portao}

transicoes = {
    (fechado, inserir_chave): 'Chave Inserida',
    ('Chave Inserida', girar_chave): aberto,
    (aberto, girar_chave): trancado,
    (trancado, girar_chave): aberto,
    (aberto, abrir_portao): em_uso,
    (em_uso, fechar_portao): aberto,
    (aberto, trancar_portao): trancado,
    (trancado, destrancar_portao): aberto,
}

modelo = FSM(estados, acoes, transicoes, estado_inicial)

def simular_fsm(modelo, eventos):
    estado_atual = modelo.estado_atual
    print(f"Estado inicial: {estado_atual}")
    for evento in eventos:
        acao = globals()[evento]
        estado_novo = modelo.transition(estado_atual, acao)
        print(f"Evento: {evento} | Estado atual: {estado_atual} -> Novo estado: {estado_novo}")
        estado_atual = estado_novo

simular_fsm(modelo, ['inserir_chave', 'girar_chave', 'abrir_portao', 'fechar_portao', 'trancar_portao', 'destrancar_portao'])
