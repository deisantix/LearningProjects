import { Funcionario } from "./Funcionario.js";

export class Diretor extends Funcionario {
    
    #bonificacao = 2;
    
    constructor(nome, cpf, salario) {
        super(nome, cpf, salario);

    }
}