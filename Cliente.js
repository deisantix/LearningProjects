export class Cliente {
    #nome;
    #cpf;
    #senha;

    constructor(adicioNome, adicioCpf, adicioSenha) {
        this.#nome = adicioNome;
        this.#cpf = adicioCpf;
        this.#senha = adicioSenha;
    }

    get nome() {
        return this.#nome;
    }

    get cpf() {
        return this.#cpf;
    }

    get senha() {
        return this.#senha;
    }

    autenticar(senha) {
        return senha === this.#senha;
    }
}