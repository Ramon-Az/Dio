import java.util.Scanner;

public class Desafio{
    public static void main(String[] args) {
        Scanner leitorDeEntradas = new Scanner(System.in);
        float valorSalario = leitorDeEntradas.nextFloat();
        float valorBeneficios = leitorDeEntradas.nextFloat();
        
        float valorImposto = 0;
        
        if (valorSalario >= 0 && valorSalario <= 1100) {
            valorImposto = valorSalario * 0.05F;
        } else if (valorSalario <= 2500) {
            valorImposto = valorSalario * 0.10F;
        } else {
            valorImposto = valorSalario * 0.15F;
        }
        
        float saida = (valorSalario - valorImposto) + valorBeneficios;
        
        System.out.println(String.format("%.2f", saida));
        leitorDeEntradas.close();
    }
}
