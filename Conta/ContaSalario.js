import { Conta } from "./Conta.js";

export class ContaSalario extends Conta {

    constructor(agente, cliente, saldo) {
        super(0, cliente, 0);
    }

    saca(valor) {
        const valorASacar = valor * 1.01;
        super.saca(valorASacar);
    }
}