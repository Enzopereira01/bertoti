package Loja;

public class Computador {
	
	private String gabinete;
	private Hardware especificacao;
	
	public Computador (String gabinete ,Hardware especificacao) {
		super();
		this.gabinete = gabinete;
		this.especificacao = especificacao;
	}
	
	
	public Hardware getEspecificacao() {
		return especificacao;
	}
	public void setEspecificacao(Hardware especificacao) {
		this.especificacao = especificacao;
	}
	public String getGabinete() {
		return gabinete;
	}
	public void setGabinete(String gabinete) {
		this.gabinete = gabinete;
	}
}
