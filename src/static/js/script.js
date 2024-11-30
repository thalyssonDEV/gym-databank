function showPlanDescription() {
    const select = document.getElementById("plan_select");
    const description = document.getElementById("plan_description");

    // Definir a descrição com base na opção selecionada
    if (select.value === "basic") {
        description.innerHTML = `Basic Plan: A simple plan for beginners.`;
    } else if (select.value === "premium") {
        description.innerHTML = "Premium Plan: Includes more features and services.";
    } else if (select.value === "vip") {
        description.innerHTML = "VIP Plan: All-inclusive, top-tier benefits.";
    }

    // Exibir a descrição
    description.style.display = "block";
}
