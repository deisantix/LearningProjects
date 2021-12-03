public class Conta {
    private String titular;
    private double saldo;

    public Conta() {
        this.saldo = 0.0;
    }

    public Conta(String titular, double saldo) {
        this.titular = titular; this.saldo = saldo;
    }

    public String getTitular() {
        return this.titular;
    }

    public double getSaldo() {
        return this.saldo;
    }

    public void setSaldo(double novoSaldo) {
        this.saldo = novoSaldo;
    }
}
