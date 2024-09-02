from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time  # Importa o módulo time para usar sleep

@given('que estou na página de login')
def step_given_na_pagina_de_login(context):
    context.browser = webdriver.Chrome()  # Inicia o WebDriver para Chrome
    context.browser.get("http://localhost:8000/index.html")
    time.sleep(2)  # Pausa de 2 segundos para ver o navegador abrir

@when('eu insiro "{username}" como nome de usuário e "{password}" como senha')
def step_when_inserir_credenciais(context, username, password):
    context.browser.find_element(By.ID, 'username').send_keys(username)
    time.sleep(1)  # Pausa de 1 segundo após inserir o nome de usuário
    context.browser.find_element(By.ID, 'password').send_keys(password)
    time.sleep(1)  # Pausa de 1 segundo após inserir a senha

@when('clico no botão de login')
def step_when_clicar_no_botao_de_login(context):
    context.browser.find_element(By.TAG_NAME, 'button').click()
    time.sleep(2)  # Pausa de 2 segundos para ver o clique no botão

@then('devo ver um alerta de login bem-sucedido')
def step_then_ver_alerta_de_sucesso(context):
    alert = context.browser.switch_to.alert
    assert alert.text == "Login bem-sucedido!"
    time.sleep(2)  # Pausa de 2 segundos para ver o alerta de sucesso
    alert.accept()
    context.browser.quit()

@then('devo ver uma mensagem de erro "{mensagem}"')
def step_then_ver_mensagem_de_erro(context, mensagem):
    error_message = context.browser.find_element(By.ID, 'error-message').text
    assert error_message == mensagem
    time.sleep(2)  # Pausa de 2 segundos para ver a mensagem de erro
    context.browser.quit()
