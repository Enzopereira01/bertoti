package Loja;

import java.util.LinkedList;
import java.util.List;

public class Loja {
	
	private List<Computador> computadores = new LinkedList<Computador>();
	
	public Loja(List<Computador> computadores) {
		this.computadores = computadores;
	}
	
	public void cadasPc(Computador pc) {
		computadores.add(pc) ;
	}

	public List<Computador> procurarPcHardware(Hardware hardware){		
		List<Computador> pcEncontrados = new LinkedList<Computador>();
		
		for (Computador pc : pcEncontrados) {
			if(pc.getEspecificacao().comparar(hardware)) pcEncontrados.add(pc);
		}
		return pcEncontrados;
	}
	
	public Computador procurarGabinete(String gabinete){		
		for (Computador pc: computadores) {
			if (pc.getGabinete().equals(gabinete))
				return pc;
		}
		return null;
	}
	
	public List<Computador> getComputadores(){
		return computadores;
	}
}
