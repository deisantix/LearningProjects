// TESTANDO AUMENTO E REALOCAMENTO DA ARRAY
public class TestaBanco02 {
    public static void main(String[] args) {
        Banco bb = new Banco("Banco do Brasil", 1203);
        
        for(int i = 0; i <= 10; i++) { // loop for vai 1 a mais doq deveria
            Conta c = new Conta(("Cliente " + (i + 1)), ((i + 1) * 100));
            bb.adicionaConta(c); // ao chegar no índice 10, aumenta a array para +5 espaços

            bb.imprimeArrayConta();
            System.out.println("Espaços disponíveis: " + bb.getContasDisponiveis());
            System.out.println("Próxima posição a ser usada: " + bb.primeiraPosicaoVazia());
            System.out.println();
        }

        bb.imprimeArrayConta();
    }
}
