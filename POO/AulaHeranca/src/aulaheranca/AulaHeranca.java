package aulaheranca;

public class AulaHeranca {

    public static void main(String[] args) {
        Automovel carro = new Automovel();
        Automovel moto = new Automovel();
        
        carro.setNumeroDePlaca("AAA-000");
        carro.setNumeroDePortas(4);
        carro.setCapacidade(5);
        carro.setNumeroDeRodas(4);
        
        moto.setNumeroDePlaca("BBB-111");
        moto.setCapacidade(2);
        moto.setNumeroDePortas(0);
        moto.setNumeroDeRodas(2);
        
        carro.getAutomovel();
        moto.getAutomovel();
        
    }
    
}
