// Simulação de usuários cadastrados
const users = {
    gabrieli: "senha123",
    bob: "senha456"
};

document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault(); // Evita o envio do formulário padrão

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (users[username] && users[username] === password) {
        alert("Login bem-sucedido!");
    } else {
        document.getElementById('error-message').innerText = "Credenciais inválidas!";
    }
});
