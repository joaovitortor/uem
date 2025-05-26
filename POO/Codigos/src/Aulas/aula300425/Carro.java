package aula300425;

public class Carro {
    String tipo, cor, placa;
    int numPortas;

    public Carro(String tipo, String cor, String placa, int numPortas) {
        this.tipo = tipo;
        this.cor = cor;
        this.placa = placa;
        this.numPortas = numPortas;
    }
    
    public Carro(){
        super();
    }

    public Carro(String tipo, String cor) {
        this.tipo = tipo;
        this.cor = cor;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

    public String getPlaca() {
        return placa;
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }

    public int getNumPortas() {
        return numPortas;
    }

    public void setNumPortas(int numPortas) {
        this.numPortas = numPortas;
    }
    
    
}
