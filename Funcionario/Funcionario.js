export class Funcionario {
    
    #nome;
    #cpf;
    #salario;
    #senha;
    #bonificacao = 1;

    constructor(nome, cpf, salario) {
        this.#nome = nome;
        this.#cpf = cpf;
        this.#salario = salario;
    }

    autenticar(senha) {
        return senha === this.#senha;
    }

    cadastrarSenha(novaSenha) {
        this.#senha = novaSenha;
    }
}