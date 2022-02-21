import { Cliente } from "./Cliente.js";
import { Diretor } from "./Funcionario/Diretor.js";
import { SistemaAutenticacao } from "./SistemaAutenticacao.js"

function main() {
    const diretor = new Diretor("Rodrigo", 12345678910, 10000);
    diretor.cadastrarSenha("123456");

    const cliente = new Cliente("Laís", 1234567911, "1234");

    console.log(SistemaAutenticacao.login(diretor, "123456"));
}

main();