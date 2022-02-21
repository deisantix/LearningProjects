import { Funcionario } from "./Funcionario.js";

export class Gerente extends Funcionario {
    
    #bonificacao = 1.1;

    constructor(nome, cpf, salario) {
        super(nome, cpf, salario);
    }
}