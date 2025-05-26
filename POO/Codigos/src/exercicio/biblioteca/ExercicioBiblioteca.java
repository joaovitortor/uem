package exercicio.biblioteca;

public class ExercicioBiblioteca {

    public static void main(String[] args) {
        Usuario u1 = new Usuario("João Bidoia", "(44) 99706-5042", 'M', 20);
        Livro l1 = new Livro("Nix", "Nathan Hill", "Romance", "Intrinseca", "3", 2019, 650);
        Emprestimo e1 = new Emprestimo("26/05/2025", "13:30", l1, u1);
        e1.imprimirEmprestimo();
    }
    
}
