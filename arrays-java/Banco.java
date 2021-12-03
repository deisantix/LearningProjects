// Exercício 04
public class Banco {
    private String nomeDoBanco;
    private int numeroDoBanco;
    private Conta[] contasDoBanco = new Conta[10];
    private int posicaoDisponivel = 0;

    public Banco(String novoNome, int novoNumero) {
        this.nomeDoBanco = novoNome; this.numeroDoBanco = novoNumero;
    }

    public String getNomeDoBanco() {
        return this.nomeDoBanco;
    }

    public int getNumeroDoBanco() {
        return this.numeroDoBanco;
    }

    public int getContasDisponiveis() {
        return this.contasDoBanco.length - this.posicaoDisponivel;
    }

    // Exercício 05
    public boolean adicionaConta(Conta c) {
        // Exercício 06:
        // Embora eu ache que em problemas pequenos, um loop que
        // procura a primeira posição vazia seja mais fácil de implementar,
        // em projetos grandes, pode se tornar lento e ineficiente.
        // Então imaginei que um programa que já sabe onde colocar a informação
        // sem ter que passar por todo esse processo a cada chamada da método
        // seja mais eficiente.
        if(this.posicaoDisponivel == this.contasDoBanco.length) {
            this.realocaContas();

        }
        this.contasDoBanco[posicaoDisponivel] = c;
        this.posicaoDisponivel += 1;

        // Exercício 09
        return true;
    }

    public void imprimeArrayConta() {
        for (Conta i : contasDoBanco) {
            System.out.println(i);
        }
    }

    // Exercicio 07:
    // Pude aproveitar o atributo this.posicaoDisponivel
    public int primeiraPosicaoVazia() {
        if(this.posicaoDisponivel == this.contasDoBanco.length) {
            return -1;
        }
        return this.posicaoDisponivel;
    }

    // Exercício 10
    public void mostraContas() {
        int i = 0;
        for(Conta conta : contasDoBanco) {
            if(conta == null) {
                return;
            }

            System.out.println("Conta na posição: " + i);
            System.out.println("Titular: " + conta.getTitular());
            System.out.println("Saldo: " + conta.getSaldo());
            System.out.println();

            i++;
        }
    }

    // Exercício 11
    public boolean contem(Conta conta) {
        for(Conta i : contasDoBanco) {
            if(i == conta) {
                return true;
            }
        }
        return false;
    }

    // DESAFIO OPCIONAL:
    // realocar contas da lista para uma maior
    private void realocaContas() {
        Conta[] contasDoBancoMaior = new Conta[this.contasDoBanco.length + 5];

        for(int i = 0; i < contasDoBanco.length; i++) {
            contasDoBancoMaior[i] = contasDoBanco[i];
        }
        contasDoBanco = contasDoBancoMaior;
    }
}
