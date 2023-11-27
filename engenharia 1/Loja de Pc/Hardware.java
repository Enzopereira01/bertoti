package Loja;

public class Hardware {
	private String processador;
	private String coller;
	private String placa_v;
	private String placa_m;
	
	public Hardware(String processador,String coller,String placa_v,String placa_m) {
		this.processador = processador ;
		this.coller = coller ;
		this.placa_v = placa_v;
		this.placa_m = placa_m;	
	}
	public String getProcessador() {
		return processador;
	}
	public void setProcessador(String processador) {
		this.processador = processador;
	}
	public String getColler() {
		return coller;
	}
	public void setColler(String coller) {
		this.coller = coller;
	}
	public String getPlaca_v() {
		return placa_v;
	}
	public void setPlaca_v(String placa_v) {
		this.placa_v = placa_v;
	}
	public String getPlaca_m() {
		return placa_m;
	}
	public void setPlaca_mae(String placa_m) {
		this.placa_m = placa_m;
	}

	public boolean comparar (Hardware hardware) {
			if (this.processador.equals(hardware.processador) &&
			this.coller.equals(hardware.coller) &&		
			this.placa_v.equals(hardware.placa_v) &&		
			this.placa_m.equals(hardware.placa_m)) {
				return true;
			}
			else {
				return false;
			}
	}
	
	
}

