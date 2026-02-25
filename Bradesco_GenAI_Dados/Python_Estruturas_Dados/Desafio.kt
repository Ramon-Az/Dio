object ReceitaFederal {
    fun calculadoraImposto(salario: Double): Double{
        val aliquota = when {
            (salario >= 0 && salario <= 1100) -> 0.05
            (salario > 1100 && salario <= 2500) -> 0.10
            (salario > 2500) -> 0.15
            else -> TODO("Criar condições para as aliquotas")
        }
        return salario * aliquota
    }
}

fun main(){
    val valorSalario = readLine()!!.toDouble();
    val valorBeneficio = readLine()!!.toDouble();
    
    val valorImposto = ReceitaFederal.calculadoraImposto(valorSalario);
    val saida = (valorSalario - valorBeneficio) + valorBeneficio
    
    print(String.format("%.2f", saida));
}