package exemplo.classe.abstrata;

public class ExemploClasseAbstrata {

    public static void main(String[] args) {
        Tv tv = new Tv(42, 220);
        
        tv.setLigado(True);
        tv.setCanal(10);
        tv.desligar();
    }
    
}
