package aula140525;

public class Agenda {
    private int dia, mes, ano;
    private String anotacao;
    
    void anote(int dia, int mes, int ano, String anotacao){
        this.dia = dia;
        this.mes = mes;
        this.ano = ano;
        this.anotacao = anotacao;
        ValidaData();
    }
    
    void ValidaData() {
        if (dia < 1 || dia > 31 || mes < 1 || mes > 12){
            this.dia = 0;
            this.mes = 0;
            this.ano = 0;
            this.anotacao = "Data inválida";
        }
    }
}
