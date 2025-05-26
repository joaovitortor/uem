package aulaheranca;

public class Automovel extends Terrestre{
    private String numeroDePlaca;
    private int numeroDePortas;
    
    public Automovel(){
        
    }
    
    public Automovel(int capacidade, int numeroDeRodas, String numeroDePlaca, int numeroDePortas){
        super(capacidade, numeroDeRodas);
        this.numeroDePlaca = numeroDePlaca;
        this.numeroDePortas = numeroDePortas;
    }

    public String getNumeroDePlaca() {
        return numeroDePlaca;
    }

    public void setNumeroDePlaca(String numeroDePlaca) {
        this.numeroDePlaca = numeroDePlaca;
    }

    public int getNumeroDePortas() {
        return numeroDePortas;
    }

    public void setNumeroDePortas(int numeroDePortas) {
        this.numeroDePortas = numeroDePortas;
    }
    
    public void getAutomovel(){
        System.out.println("Capacidade: " + this.capacidade);
        System.out.println("Número de portas: " + this.numeroDePortas);
        System.out.println("Número de rodas: " + this.numeroDeRodas);
        System.out.println("Número de placa: " + this.numeroDePlaca + "\n");
    }
        
}