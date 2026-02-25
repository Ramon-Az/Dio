// readline: módulo do Node.js para ler dados do usuário
// createInterface: cria uma interface de comunicação
// process.stdin: entrada padrão (teclado)
// process.stdout: saída padrão (tela)
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// rl.question: exibe a mensagem e aguarda resposta
// salario: recebe o texto digitado pelo usuário
// parseFloat: converte o texto em número decimal
rl.question('Digite o valor do salário: R$ ', (salario) => {
    const valorSalario = parseFloat(salario);
    
    rl.question('Digite o valor dos benefícios: R$ ', (beneficio) => {
        const valorBeneficio = parseFloat(beneficio);
        
        const valorImposto = calcularImposto(valorSalario);
        const saida = (valorSalario - valorImposto) + valorBeneficio;
        console.log("O salário descontado os impostos: R$ " + saida.toFixed(2));
        rl.close();
    });
});

// Define a alíquota (taxa) do imposto baseada no salário:
// Até R$ 1100: 5%
// De R$ 1100 até R$ 2500: 10%
// Acima de R$ 2500: 15%
// Retorna o valor do imposto (salário × alíquota)
function calcularImposto(salario) {
    let aliquota;
    if (salario >= 0 && salario <= 1100) {
        aliquota = 0.05;
    } else if (salario > 1100 && salario <= 2500) {
        aliquota = 0.10;
    } else {
        aliquota = 0.15;
    }
    const imposto = salario * aliquota;
    console.log("O valor, do imposto é: R$" + imposto.toFixed(2));
    return imposto;
}