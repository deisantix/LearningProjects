import { Conta } from "./Conta.js";

export class ContaPoupanca extends Conta {

    constructor(agencia, cliente, saldo) {
        super(agencia, cliente, saldo);
    }

    saca(valor) {
        const valorASacar = valor * 1.02;
        super.saca(valorASacar);
    }
}