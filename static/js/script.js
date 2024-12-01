function validarCPF(cpf) {
    if (cpf.length !== 11 || /^(\d)\1+$/.test(cpf)) return false; // CPF inválido

    let soma = 0, resto;

    for (let i = 1; i <= 9; i++) soma += parseInt(cpf[i - 1]) * (11 - i);
    resto = (soma * 10) % 11;
    if (resto === 10 || resto === 11) resto = 0;
    if (resto !== parseInt(cpf[9])) return false;

    soma = 0;
    for (let i = 1; i <= 10; i++) soma += parseInt(cpf[i - 1]) * (12 - i);
    resto = (soma * 10) % 11;
    if (resto === 10 || resto === 11) resto = 0;
    return resto === parseInt(cpf[10]);
}


function showPlanDescription() {
    const select = document.getElementById("plan_select");
    const description = document.getElementById("plan_description");
    const planValue = document.getElementById("id_plano");

    // Definir a descrição com base na opção selecionada
    if (select.value === "basic") {
        description.innerHTML = `Basic Plan: A simple plan for beginners.`;
        planValue.value = 1; 
    } else if (select.value === "premium") {
        description.innerHTML = "Premium Plan: Includes more features and services.";
        planValue.value = 2; 
    } else if (select.value === "vip") {
        description.innerHTML = "VIP Plan: All-inclusive, top-tier benefits.";
        planValue.value = 3; 
    }

    // Exibir a descrição
    description.style.display = "block";
}


// document.getElementById("cpf_usuario").addEventListener("blur", function () {
//     const cpf = this.value.replace(/[^\d]+/g, ""); // Remove caracteres não numéricos

//     if (!validarCPF(cpf)) {
//         alert("Invalid CPF. Please check and try again.");
//         this.value = ""; // Limpa o campo
//     }
// });

// document.querySelector("form").addEventListener("submit", function (event) {
//     const cpfInput = document.getElementById("cpf_usuario");
//     const cpfLimpo = cpfInput.value.replace(/\D/g, ""); // Remove tudo que não é número
//     cpfInput.value = cpfLimpo; // Substitui pelo valor limpo
// });

document.querySelector("form").addEventListener("submit", function (event) {
    const senha = document.getElementById("senha").value;
    const confirmarSenha = document.getElementById("confirmar-senha").value;

    // Verifica se a senha tem pelo menos 8 caracteres
    if (senha.length < 8) {
        alert("Password must be at least 8 characters long.");
        event.preventDefault(); // Impede o envio do formulário
        return;
    }

    // Verifica se a confirmação da senha é igual à senha
    if (senha !== confirmarSenha) {
        alert("Passwords do not match. Please check and try again.");
        event.preventDefault(); // Impede o envio do formulário
        return;
    }
});


document.getElementById("senha").addEventListener("blur", function () {
    if (this.value.length < 8) {
        this.classList.add("error");
        this.classList.remove("success");
    } else {
        this.classList.add("success");
        this.classList.remove("error");
    }
});

document.getElementById("confirmar-senha").addEventListener("blur", function () {
    const senha = document.getElementById("senha").value;

    if (this.value !== senha) {
        this.classList.add("error");
        this.classList.remove("success");
    } else {
        this.classList.add("success");
        this.classList.remove("error");
    }
});

document.querySelector("form").addEventListener("submit", function (event) {
    const telefone = document.getElementById("telefone").value;

    // Remove caracteres não numéricos
    const telefoneLimpo = telefone.replace(/\D/g, "");

    // Verifica se o telefone tem 10 ou 11 dígitos
    if (telefoneLimpo.length < 10 || telefoneLimpo.length > 11) {
        alert("Phone number must have 10 or 11 digits.");
        event.preventDefault(); // Impede o envio do formulário
        return;
    }
});

document.getElementById("telefone").addEventListener("blur", function () {
    const telefone = this.value.replace(/\D/g, ""); // Remove caracteres não numéricos

    if (telefone.length < 10 || telefone.length > 11) {
        this.classList.add("error");
        alert("Invalid phone number. It must have 10 or 11 digits.");
    } else {
        this.classList.remove("error");
    }
});

document.getElementById("telefone").addEventListener("input", function () {
    const telefone = this.value.replace(/\D/g, ""); // Remove caracteres não numéricos
    if (telefone.length <= 10) {
        this.value = telefone.replace(/(\d{2})(\d{4})(\d{0,4})/, "($1) $2-$3");
    } else {
        this.value = telefone.replace(/(\d{2})(\d{5})(\d{0,4})/, "($1) $2-$3");
    }
});

// function showSuccessMessage() {
//     const successMessage = document.getElementById('success_message');
//     successMessage.style.display = 'flex';

//     // Esconde a mensagem após 3 segundos
//     setTimeout(function() {
//         successMessage.style.display = 'none';
//     }, 3000);
// }

// const form = document.getElementById('form_action');

// // Adiciona o evento de envio do formulário
// form.addEventListener('submit', function(event) {
//     //lógica para enviar o formulário via AJAX - implementar
//     showSuccessMessage();
// });