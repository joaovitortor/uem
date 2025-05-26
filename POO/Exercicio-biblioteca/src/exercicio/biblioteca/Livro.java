package exercicio.biblioteca;

public class Livro {
    private String titulo, autores, area, editora, edicao;
    private int ano, numeroFolhas;

    public Livro(){
        super();
    }
    
    public Livro(String titulo, String autores, String area, String editora, String edicao, int ano, int numeroFolhas) {
        this.titulo = titulo;
        this.autores = autores;
        this.area = area;
        this.editora = editora;
        this.edicao = edicao;
        this.ano = ano;
        this.numeroFolhas = numeroFolhas;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getAutores() {
        return autores;
    }

    public void setAutores(String autores) {
        this.autores = autores;
    }

    public String getArea() {
        return area;
    }

    public void setArea(String area) {
        this.area = area;
    }

    public String getEditora() {
        return editora;
    }

    public void setEditora(String editora) {
        this.editora = editora;
    }

    public String getEdicao() {
        return edicao;
    }

    public void setEdicao(String edicao) {
        this.edicao = edicao;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public int getNumeroFolhas() {
        return numeroFolhas;
    }

    public void setNumeroFolhas(int numeroFolhas) {
        this.numeroFolhas = numeroFolhas;
    }
    
    public void getLivro(){
        System.out.println("Título: " + getTitulo());
        System.out.println("Autores: " + getAutores());
        System.out.println("Área: " + getArea());
        System.out.println("Editora: " + getEditora());
        System.out.println("Edicao: " + getEdicao());
        System.out.println("Ano: " + getAno());
        System.out.println("Número de folhas: " + getNumeroFolhas());
    }
    
}
