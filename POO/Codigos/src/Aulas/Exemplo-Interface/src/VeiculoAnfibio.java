public class VeiculoAnfibio implements Carro, Barco{

    @Override
    public void PuxarFreioDeMao(){
        System.out.println("Puxar freio de mão");
    }    
    
    @Override
    public void jogarAncora(){
        System.out.println("Jogar Ancora");
    }
}
