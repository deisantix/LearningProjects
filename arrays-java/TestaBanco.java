// Exercício 08
public class TestaBanco {
    public static void main(String[] args) {
        Banco bb = new Banco("Banco do Brasil", 1203);
        
        for(int i = 0; i < 5; i++) {
            Conta c = new Conta(("Cliente " + (i + 1)), ((i + 1) * 100));
            bb.adicionaConta(c);

            bb.imprimeArrayConta();
            System.out.println("Espaços disponíveis: " + bb.getContasDisponiveis());
            System.out.println("Próxima posição a ser usada: " + bb.primeiraPosicaoVazia());
            System.out.println();
        }

        bb.mostraContas();

        // Testando o método bb.contem(conta)
        Conta david = new Conta("David", 5000.0);
        bb.adicionaConta(david);

        Conta samuel = new Conta("Samuel", 12.0);

        // é pra retornar true
        System.out.println(bb.contem(david)); // retorna true

        // é pra retornar false
        System.out.println(bb.contem(samuel)); // retorna false
        
    }
}
