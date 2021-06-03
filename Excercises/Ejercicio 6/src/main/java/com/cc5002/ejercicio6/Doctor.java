package com.cc5002.ejercicio6;
import static java.lang.System.out;

public class Doctor {

    private String nombre;
    private String exp;
    private String region;
    private String comuna;
    private String especialidad;
    private String twitter;
    private String email;
    private String celular;

    public Doctor(
            String nombre, String exp, String region,
            String comuna, String especialidad,
            String twitter, String email, String celular
    ) {
        this.nombre = nombre;
        this.exp = exp;
        this.region = region;
        this.comuna = comuna;
        this.especialidad = especialidad;
        this.twitter = twitter;
        this.email = email;
        this.celular = celular;
    }

    public String getNombre() {
        return nombre;
    }

    public String getExp() {
        return exp;
    }

    public String getRegion() {
        return region;
    }

    public String getComuna() {
        return comuna;
    }

    public String getEspecialidad() {
        return especialidad;
    }

    public String getTwitter() {
        return twitter;
    }

    public String getEmail() {
        return email;
    }

    public String getCelular() {
        return celular;
    }
}