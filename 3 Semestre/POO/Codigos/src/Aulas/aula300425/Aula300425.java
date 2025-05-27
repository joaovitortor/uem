package aula300425;

public class Aula300425 {

    public static void main(String[] args) {
        Carro c1 = new Carro("Esportivo", "Vermelho", "AAAA 000", 4);
        
        System.out.println("\nCarro \n");
        System.out.println("Cor: " + c1.getCor());
        System.out.println("Portas: " + c1.getNumPortas());
        System.out.println("Placa: " + c1.getPlaca());
        System.out.println("Tipo: " + c1.getTipo());
        
        Carro c2 = new Carro();
        c1.setCor("Vermelho");
        c1.setNumPortas(4);
        c1.setPlaca("AAAA 012");
        c1.setTipo("Esportivo");
        
        Carro c3 = new Carro("SUV", "Preto");
        c3.setNumPortas(4);
        c3.setPlaca("AAA000");
        
        Pessoa p1 = new Pessoa();
        
    }
    
}
