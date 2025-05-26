package aulaheranca;

public class Terrestre extends Transporte{
    protected int numeroDeRodas;
    
    public Terrestre(){
        
    }
    
    public Terrestre(int capacidade, int numeroDeRodas){
        super(capacidade); //método construtor da classe transporte
        this.numeroDeRodas = numeroDeRodas;
        
    }

    public int getNumeroDeRodas() {
        return numeroDeRodas;
    }

    public void setNumeroDeRodas(int numeroDeRodas) {
        this.numeroDeRodas = numeroDeRodas;
    }
    
}
