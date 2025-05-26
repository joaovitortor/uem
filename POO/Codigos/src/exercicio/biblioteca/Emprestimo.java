package exercicio.biblioteca;

public class Emprestimo {
    private String dataEmprestimo, horaEmprestimo;
    private Livro livro;
    private Usuario usuario;

    public Emprestimo(){
        super();
    }
    public Emprestimo(String dataEmprestimo, String horaEmprestimo, Livro livro, Usuario usuario) {
        this.dataEmprestimo = dataEmprestimo;
        this.horaEmprestimo = horaEmprestimo;
        this.livro = livro;
        this.usuario = usuario;
    }
    
    public void realizarEmprestimo(){
        System.out.println("Emprestimo realizado");
    }

    public String getDataEmprestimo() {
        return dataEmprestimo;
    }

    public void setDataEmprestimo(String dataEmprestimo) {
        this.dataEmprestimo = dataEmprestimo;
    }

    public String getHoraEmprestimo() {
        return horaEmprestimo;
    }

    public void setHoraEmprestimo(String horaEmprestimo) {
        this.horaEmprestimo = horaEmprestimo;
    }
    
    
    public void imprimirEmprestimo(){
        System.out.println("Data do emprestimo: " + getDataEmprestimo());
        System.out.println("Hora do espréstimo: " + getHoraEmprestimo());
        System.out.println("Nome do usuário: " + usuario.getNome());
        System.out.println("Nome do livro: " + livro.getTitulo());
    }
}
