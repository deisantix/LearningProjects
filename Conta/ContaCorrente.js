import { Conta } from "./Conta.js"

export class ContaCorrente extends Conta {
    
    constructor(agencia, cliente, saldo) {
        super(agencia, cliente, 0);
    }

    saca(valor) {
        const valorASacar = valor * 1.1;
        super.saca(valorASacar);
    }
}