public class TestaArrays {
    public static void main(String[] args) {
        
        // Exercício 01
        Conta[] contas = new Conta[10];

        for (int i = 0; i < 10; i++) {
            Conta d = new Conta();
            d.setSaldo((i + 1) * 100);
            
            contas[i] = d;
        }

        for (Conta i : contas) {
            System.out.println(i.getSaldo());
        }
        System.out.println();

        // Exercício 02
        double soma, media;
        soma = 0;

        for (Conta conta : contas) {
            soma += conta.getSaldo();
        }
        media = soma / 10;

        System.out.println("Média dos saldos: " + media);
    }
}