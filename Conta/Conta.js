import { Cliente } from "../Cliente.js";

export class Conta {
    static numeroDeContas = 0;

    #agencia;
    #cliente;
    #saldo;

    constructor(agencia, cliente, saldo) {
        this.#agencia = agencia;
        this.cliente = cliente;
        this.#saldo = saldo;

        Conta.numeroDeContas++;
    }

    get cliente() {
        return this.#cliente;
    }
    
    get saldo() {
        return this.#saldo;
    }

    set cliente(addCliente) {
        if(addCliente instanceof Cliente) {
            this.#cliente = addCliente;
        }
    }

    saca(valor) {
        valor = valor.toFixed(2);

        if(valor >= this.#saldo) {
            return;
        }
        this.#saldo -= valor;
    }

    deposita(valor) {
        if(valor <= 0) {
            return;
        }
        this.#saldo += valor;
    }

    transferir(valor, outraConta) {
        const valorSacado = this.saca(valor);
        outraConta.deposita(valorSacado);
    }
}