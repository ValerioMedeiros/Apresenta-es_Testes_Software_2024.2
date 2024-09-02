Feature: Funcionalidade de Login  # Certifique-se de que essa linha é exatamente assim.

  Scenario: Login bem-sucedido com credenciais válidas
    Given que estou na página de login
    When eu insiro "gabrieli" como nome de usuário e "senha123" como senha
    And clico no botão de login
    Then devo ver um alerta de login bem-sucedido

  Scenario: Falha no login com credenciais inválidas
    Given que estou na página de login
    When eu insiro "gabrieli" como nome de usuário e "senhaErrada" como senha
    And clico no botão de login
    Then devo ver uma mensagem de erro "Credenciais inválidas!"
