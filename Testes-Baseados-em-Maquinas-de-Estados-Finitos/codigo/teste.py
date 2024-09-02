from portao import FSM, inserir_chave, girar_chave, abrir_portao, fechar_portao, trancar_portao, destrancar_portao
import portao

estado_inicial = portao.fechado

def teste_fsm():
    estado = estado_inicial
    estado = inserir_chave(estado)
    assert estado == 'Chave Inserida', f"Erro: O portão deveria estar em 'Chave Inserida' ao inserir a chave, mas está {estado}."

    estado = girar_chave(estado)
    assert estado == portao.aberto, f"Erro: O portão deveria estar aberto após girar a chave, mas está {estado}."

    estado = abrir_portao(estado)
    assert estado == portao.em_uso, f"Erro: O portão deveria estar em uso após abrir o portão, mas está {estado}."

    estado = fechar_portao(estado)
    assert estado == portao.aberto, f"Erro: O portão deveria estar aberto após fechar o portão, mas está {estado}."

    estado = girar_chave(estado)
    assert estado == portao.trancado, f"Erro: O portão deveria estar trancado após girar a chave, mas está {estado}."

    estado = destrancar_portao(estado)
    assert estado == portao.aberto, f"Erro: O portão deveria estar aberto após destrancar, mas está {estado}."

    estado = girar_chave(estado)
    assert estado == portao.trancado, f"Erro: O portão deveria estar trancado após girar a chave novamente, mas está {estado}."

    estado = estado_inicial
    estado = abrir_portao(estado)
    assert estado == portao.fechado, f"Erro: O portão deveria permanecer fechado ao tentar abri-lo sem inserir a chave, mas está {estado}."

    estado = estado_inicial
    estado = inserir_chave(estado)
    assert estado == 'Chave Inserida', f"Erro: O portão deveria estar em 'Chave Inserida', mas está {estado}."

    estado = girar_chave(estado)
    assert estado == portao.aberto, f"Erro: O portão deveria estar aberto após girar a chave, mas está {estado}."

    estado = girar_chave(estado)
    assert estado == portao.trancado, f"Erro: O portão deveria estar trancado após girar a chave novamente, mas está {estado}."

    estado = destrancar_portao(estado)
    assert estado == portao.aberto, f"Erro: O portão deveria estar aberto após destrancar o portão, mas está {estado}."

    estado = estado_inicial
    estado = inserir_chave(estado)
    estado = girar_chave(estado)
    estado = girar_chave(estado) 

    estado = abrir_portao(estado)
    assert estado == portao.trancado, f"Erro: O portão deveria permanecer trancado ao tentar abri-lo enquanto trancado, mas está {estado}."

    print("Todos os testes foram concluídos com sucesso!")

teste_fsm()
