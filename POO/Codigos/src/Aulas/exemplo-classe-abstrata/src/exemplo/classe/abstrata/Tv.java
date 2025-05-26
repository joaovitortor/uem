/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package exemplo.classe.abstrata;

/**
 *
 * @author joaov
 */
public class Tv extends Eletrodomestico{
    private int tamanho, canal, volume;
    
    public Tv(int tamanho, int voltagem){
        super(false, voltagem);
        this.tamanho = tamanho;
        this.canal = 0;
        this.volume = 0;
    }
    
    @Override
    public void Ligar(){
        this.setLigado(True);
        this.setVolume(5);
    }

    public int getTamanho() {
        return tamanho;
    }

    public void setTamanho(int tamanho) {
        this.tamanho = tamanho;
    }

    public int getCanal() {
        return canal;
    }

    public void setCanal(int canal) {
        this.canal = canal;
    }

    public int getVolume() {
        return volume;
    }

    public void setVolume(int volume) {
        this.volume = volume;
    }
    
    
    
}
