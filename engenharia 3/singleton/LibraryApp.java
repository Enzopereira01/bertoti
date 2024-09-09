// LibraryApp.java
public class LibraryApp {
    public static void main(String[] args) {
        Library library = new Library();
        
        // Adiciona alguns livros à biblioteca
        library.addBook(new Book("1984", "George Orwell"));
        library.addBook(new Book("To Kill a Mockingbird", "Harper Lee"));

        // Lista os livros da biblioteca
        library.listBooks();
    }
}
