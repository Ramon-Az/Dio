using System;

public class Desafio {
    public static void Main(){
        float valorSalario = float.Parse(Console.ReadLine());
        float valorBeneficios = float.Parse(Console.ReadLine());
        
        float valorImposto = 0;
        
        if (valorSalario >= 0 && valorSalario <= 1100) {
            valorImposto = valorSalario * 0.05F;
        } else if (valorSalario <= 2500) {
            valorImposto = valorSalario * 0.10F;
        } else {
            valorImposto = valorSalario * 0.15F;
        }
        
        float saida = (valorSalario - valorImposto) + valorBeneficios;
        Console.WriteLine(saida.ToString("0.00"));
    }
}
