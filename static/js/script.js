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
